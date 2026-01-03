import tkinter as tk
from functools import wraps

from timeSheetFiller import always_on_top
from time_tracker import TimeTracker
from file_writer import TimesheetWriter

class TimeTrackerUI:
    def __init__(self, root):
        self.root = root
        self.root.minsize(250, 160)
        self.tracker = TimeTracker()
        self.writer = TimesheetWriter()
        self.aot = AlwaysOnTop()

        self.build_ui()

    def build_ui(self):
        self.ticket_label = tk.Label(self.root, text="Ticket ID: ")
        self.ticket_entry_label = tk.Label(self.root, text="Ticket desc.: ")
        self.start_label = tk.Label(self.root, text="Start: ")
        self.stop_label = tk.Label(self.root, text="Stop: ")
        self.duration_label = tk.Label(self.root, text="Minutes: ")
        self.ticket_entry = tk.Entry(self.root, width=20)
        self.ticket_desc_text = tk.Text(self.root, width=20, height = 5, wrap = "word")
        self.duration_entry = tk.Entry(self.root, width=20)
        tk.Button(self.root, text="Start", command=self.on_start).grid(row=5, column=1, sticky=tk.W)
        tk.Button(self.root, text="Stop", command=self.on_stop).grid(row=5, column=1, sticky=tk.E)
        tk.Button(self.root, text="A.O.T.", command=self.always_on_top).grid(row=5, column=0, sticky=tk.W)

        self.ticket_label.grid(row=0, column=0)
        self.ticket_entry.grid(row=1, column=0)
        self.start_label.grid(row=2, column=0)
        self.stop_label.grid(row=3, column=0)
        self.duration_label.grid(row=4, column=0)
        self.ticket_entry.grid(row=0, column=1, sticky=tk.W)
        self.ticket_desc_text.grid(row=1, column=1, sticky=tk.W)
        self.duration_entry.grid(row=4, column=1, sticky=tk.W)


    def on_start(self):
        start = self.tracker.start()
        self.start_label.config(text=f"Start: {start}")

    def on_stop(self):
        stop = self.tracker.stop()
        minutes = self.tracker.duration_minutes()

        self.stop_label.config(text=f"Stop: {stop}")
        self.duration_label.config(text=f"Minutes: {minutes:.1f}")

    def always_on_top(self):
        aot = self.aot()