import tkinter as tk
from model import TimeTracker, TimesheetWriter
from view import TimeTrackerView
from controller import TimeTrackerController


def main():
    root = tk.Tk()
    model = TimeTracker()
    writer = TimesheetWriter()
    view = TimeTrackerView(root)
    TimeTrackerController(model, writer, view)
    root.mainloop()


if __name__ == "__main__":
    main()
