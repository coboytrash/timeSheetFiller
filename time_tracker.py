import tkinter as tk
from datetime import datetime

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def start(self):
        self.start_time = datetime.now()
        return self.start_time

    def stop(self):
        self.stop_time = datetime.now()
        return self.stop_time

    def duration_minutes(self):
        if self.start_time and self.stop_time:
            diff = self.stop_time - self.start_time
            return diff.total_seconds() / 60
        return None
