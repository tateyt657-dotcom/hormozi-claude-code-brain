#!/usr/bin/env python3
"""
Window app for the lead scraper. Double-click start.bat (Windows) or
start.command (Mac), or run:  python lead_scraper_app.py
"""

from __future__ import annotations

import os
import queue
import subprocess
import sys
import tempfile
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, scrolledtext, ttk

HERE = Path(__file__).resolve().parent
SCRAPER = HERE / "lead_scraper.py"


# Fixed light colors so the boxes stay visible in Mac dark mode.
BOX = dict(bg="white", fg="black", insertbackground="black", relief="solid",
           borderwidth=1, highlightthickness=1, highlightbackground="#888888",
           highlightcolor="#3b82f6")


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Lead Scraper")
        self.geometry("820x760")
        self.minsize(640, 600)
        self.proc: subprocess.Popen | None = None
        self.lines: queue.Queue[str] = queue.Queue()
        self.tmp_files: list[str] = []
        self._build()
        self.after(100, self._drain_log)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---------------------------------------------------------------- layout
    def _build(self) -> None:
        pad = {"padx": 10, "pady": 4}
        root = ttk.Frame(self, padding=10)
        root.pack(fill="both", expand=True)

        ttk.Label(root, text="What businesses? (one per line, e.g. roofers)").pack(anchor="w", **pad)
        self.searches = tk.Text(root, height=4, **BOX)
        self.searches.pack(fill="x", **pad)

        ttk.Label(root, text="Locations: cities or ZIP codes (one per line, paste as many as you want)").pack(anchor="w", **pad)
        loc_row = ttk.Frame(root)
        loc_row.pack(fill="x", **pad)
        self.locations = tk.Text(loc_row, height=7, **BOX)
        self.locations.pack(side="left", fill="both", expand=True)
        ttk.Button(loc_row, text="Load file...", command=self._load_locations).pack(side="left", padx=6, anchor="n")

        opts = ttk.Frame(root)
        opts.pack(fill="x", **pad)
        ttk.Label(opts, text="Max per search:").grid(row=0, column=0, sticky="w")
        self.max_var = tk.StringVar(value="120")
        ttk.Spinbox(opts, from_=5, to=200, textvariable=self.max_var, width=6).grid(row=0, column=1, sticky="w", padx=6)
        ttk.Label(opts, text="Wait between searches (sec):").grid(row=0, column=2, sticky="w", padx=(20, 0))
        self.delay_var = tk.StringVar(value="3")
        ttk.Spinbox(opts, from_=0, to=60, textvariable=self.delay_var, width=6).grid(row=0, column=3, sticky="w", padx=6)

        self.no_site = tk.BooleanVar(value=False)
        self.no_emails = tk.BooleanVar(value=False)
        self.headful = tk.BooleanVar(value=False)
        self.restart = tk.BooleanVar(value=False)
        checks = ttk.Frame(root)
        checks.pack(fill="x", **pad)
        ttk.Checkbutton(checks, text="Only businesses with NO real website (web offer leads)", variable=self.no_site).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(checks, text="Skip emails (faster)", variable=self.no_emails).grid(row=0, column=1, sticky="w", padx=20)
        ttk.Checkbutton(checks, text="Show the browser", variable=self.headful).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(checks, text="Redo searches already finished", variable=self.restart).grid(row=1, column=1, sticky="w", padx=20)

        out_row = ttk.Frame(root)
        out_row.pack(fill="x", **pad)
        ttk.Label(out_row, text="Save to:").pack(side="left")
        self.out_var = tk.StringVar(value=str(Path.home() / "Desktop" / "leads.csv"
                                              if (Path.home() / "Desktop").is_dir() else HERE / "leads.csv"))
        ttk.Entry(out_row, textvariable=self.out_var).pack(side="left", fill="x", expand=True, padx=6)
        ttk.Button(out_row, text="Browse...", command=self._pick_out).pack(side="left")

        btns = ttk.Frame(root)
        btns.pack(fill="x", **pad)
        self.start_btn = ttk.Button(btns, text="Start", command=self._start)
        self.start_btn.pack(side="left")
        self.stop_btn = ttk.Button(btns, text="Stop", command=self._stop, state="disabled")
        self.stop_btn.pack(side="left", padx=6)
        ttk.Button(btns, text="Open CSV", command=self._open_csv).pack(side="left")
        self.status = ttk.Label(btns, text="Ready")
        self.status.pack(side="right")

        self.log = scrolledtext.ScrolledText(root, height=16, state="disabled", font=("Courier", 11), **BOX)
        self.log.pack(fill="both", expand=True, **pad)

    # --------------------------------------------------------------- actions
    def _load_locations(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("Text or CSV", "*.txt *.csv"), ("All files", "*.*")])
        if path:
            text = Path(path).read_text(encoding="utf-8", errors="ignore")
            self.locations.insert("end", ("\n" if self.locations.get("1.0", "end").strip() else "") + text.strip())

    def _pick_out(self) -> None:
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if path:
            self.out_var.set(path)

    def _write_tmp(self, text: str) -> str:
        fd, path = tempfile.mkstemp(suffix=".txt", text=True)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        self.tmp_files.append(path)
        return path

    def _start(self) -> None:
        searches = [l.strip() for l in self.searches.get("1.0", "end").splitlines() if l.strip()]
        locations = [l.strip() for l in self.locations.get("1.0", "end").splitlines() if l.strip()]
        if not searches:
            messagebox.showwarning("Lead Scraper", "Type at least one business type, like: roofers")
            return
        cmd = [sys.executable, "-u", str(SCRAPER), self._write_tmp("\n".join(searches)),
               "--max", self.max_var.get(), "--delay", self.delay_var.get(), "--out", self.out_var.get()]
        if locations:
            cmd += ["--locations", self._write_tmp("\n".join(locations))]
        for flag, var in (("--no-website-only", self.no_site), ("--no-emails", self.no_emails),
                          ("--headful", self.headful), ("--restart", self.restart)):
            if var.get():
                cmd.append(flag)

        total = len(searches) * max(len(locations), 1)
        self._clear_log()
        self._append(f"Starting {total} searches...\n")
        flags = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     text=True, encoding="utf-8", errors="replace", creationflags=flags)
        threading.Thread(target=self._read_output, daemon=True).start()
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status.config(text="Running...")

    def _read_output(self) -> None:
        assert self.proc and self.proc.stdout
        for line in self.proc.stdout:
            self.lines.put(line)
        code = self.proc.wait()
        self.lines.put(f"\n__DONE__{code}")

    def _stop(self) -> None:
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            self._append("\nStopping... leads saved so far stay in the CSV.\n")

    def _open_csv(self) -> None:
        path = Path(self.out_var.get())
        if not path.exists():
            messagebox.showinfo("Lead Scraper", "No CSV yet. Run a search first.")
            return
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])

    # -------------------------------------------------------------- log view
    def _drain_log(self) -> None:
        while not self.lines.empty():
            line = self.lines.get()
            if line.startswith("\n__DONE__"):
                code = line.replace("\n__DONE__", "")
                self.status.config(text="Done" if code == "0" else "Stopped")
                self.start_btn.config(state="normal")
                self.stop_btn.config(state="disabled")
                self._cleanup_tmp()
            else:
                self._append(line)
                if line.lstrip().startswith("["):
                    self.status.config(text=line.strip().split("]")[0] + "]")
        self.after(100, self._drain_log)

    def _append(self, text: str) -> None:
        self.log.config(state="normal")
        self.log.insert("end", text)
        self.log.see("end")
        self.log.config(state="disabled")

    def _clear_log(self) -> None:
        self.log.config(state="normal")
        self.log.delete("1.0", "end")
        self.log.config(state="disabled")

    def _cleanup_tmp(self) -> None:
        for path in self.tmp_files:
            try:
                os.remove(path)
            except OSError:
                pass
        self.tmp_files.clear()

    def _on_close(self) -> None:
        self._stop()
        self._cleanup_tmp()
        self.destroy()


if __name__ == "__main__":
    App().mainloop()
