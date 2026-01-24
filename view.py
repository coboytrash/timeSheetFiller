import tkinter as tk


class TimeTrackerView:
    def __init__(self, root):
        self.root = root
        self.root.title("Timesheet Filler")

        self.dock_left(width=100)
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Ticket ID").grid(row=0, column=0, sticky="w")
        tk.Label(self.root, text="Description").grid(row=2, column=0, sticky="nw")
        tk.Label(self.root, text="Minutes").grid(row=9, column=0, sticky="w")

        self.ticket_entry = tk.Entry(self.root, width=16)
        self.desc_text = tk.Text(self.root, width=14, height=15, wrap="word")
        self.start_label = tk.Label(self.root, text="-")
        self.stop_label = tk.Label(self.root, text="-")
        self.minutes_entry = tk.Entry(self.root, width=10)

        self.ticket_entry.grid(row=1, column=0, sticky="w", pady = (0, 10))
        self.desc_text.grid(row=3, column=0, sticky="w", pady = (0, 20))
        self.start_label.grid(row=6, column=0, sticky="w", pady = (0, 10))
        self.stop_label.grid(row=8, column=0, sticky="w", pady = (0, 10))
        self.minutes_entry.grid(row=10, column=0, sticky="w", pady = (0, 10))

        self.start_btn = tk.Button(self.root, text="Start")
        self.stop_btn = tk.Button(self.root, text="Stop")
        self.add_btn = tk.Button(self.root, text="Add Task")
        self.top_btn = tk.Button(self.root, text="A.O.T. OFF")

        self.start_btn.grid(row=5, column=0, sticky="ew")
        self.stop_btn.grid(row=7, column=0, sticky="ew")
        self.add_btn.grid(row=11, column=0, sticky="ew", pady = (0, 200))
        self.top_btn.grid(row=12, column=0, sticky="w")


    def get_form_data(self):
        return (
            self.ticket_entry.get(),
            self.desc_text.get("1.0", "end-1c")
        )

    def clear(self):
        self.ticket_entry.delete(0, "end")
        self.desc_text.delete("1.0", "end")
        self.start_label.config(text="-")
        self.stop_label.config(text="-")
        self.minutes_entry.delete(0, "end")

    def dock_left(self, width=260):
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{screen_height}+0+0")
        self.root.resizable(width=True, height=False)
