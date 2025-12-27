import tkinter as tk
from time_tracker import TimeTracker
from file_writer import TimesheetWriter

class TimeTrackerUI:
    def __init__(self, root):
        self.root = root
        self.tracker = TimeTracker()
        self.writer = TimesheetWriter()

        self.build_ui()

    def build_ui(self):
        self.start_label = tk.Label(self.root, text="Start: --")
        self.stop_label = tk.Label(self.root, text="Stop: --")
        self.duration_label = tk.Label(self.root, text="Minutes: --")

        self.start_label.grid(row=0, column=0)
        self.stop_label.grid(row=1, column=0)
        self.duration_label.grid(row=2, column=0)

        tk.Button(self.root, text="Start", command=self.on_start).grid(row=0, column=1)
        tk.Button(self.root, text="Stop", command=self.on_stop).grid(row=1, column=1)

    def on_start(self):
        start = self.tracker.start()
        self.start_label.config(text=f"Start: {start}")

    def on_stop(self):
        stop = self.tracker.stop()
        minutes = self.tracker.duration_minutes()

        self.stop_label.config(text=f"Stop: {stop}")
        self.duration_label.config(text=f"Minutes: {minutes:.2f}")
