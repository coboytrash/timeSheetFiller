import tkinter as tk


class TimeTrackerView:
    def __init__(self, root):
        self.root = root
        self.root.title("Timesheet Filler")
        self.root.minsize(260, 200)
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Ticket ID").grid(row=0, column=0, sticky="w")
        tk.Label(self.root, text="Description").grid(row=1, column=0, sticky="nw")
        tk.Label(self.root, text="Start").grid(row=2, column=0, sticky="w")
        tk.Label(self.root, text="Stop").grid(row=3, column=0, sticky="w")
        tk.Label(self.root, text="Minutes").grid(row=4, column=0, sticky="w")

        self.ticket_entry = tk.Entry(self.root, width=20)
        self.desc_text = tk.Text(self.root, width=20, height=4, wrap="word")
        self.start_label = tk.Label(self.root, text="-")
        self.stop_label = tk.Label(self.root, text="-")
        self.minutes_entry = tk.Entry(self.root, width=10)

        self.ticket_entry.grid(row=0, column=1, sticky="w")
        self.desc_text.grid(row=1, column=1, sticky="w")
        self.start_label.grid(row=2, column=1, sticky="w")
        self.stop_label.grid(row=3, column=1, sticky="w")
        self.minutes_entry.grid(row=4, column=1, sticky="w")

        self.start_btn = tk.Button(self.root, text="Start")
        self.stop_btn = tk.Button(self.root, text="Stop")
        self.add_btn = tk.Button(self.root, text="Add Task")
        self.top_btn = tk.Button(self.root, text="A.O.T. OFF")

        self.start_btn.grid(row=5, column=0, sticky="w")
        self.stop_btn.grid(row=5, column=1, sticky="e")
        self.top_btn.grid(row=6, column=0, sticky="w")
        self.add_btn.grid(row=6, column=1, sticky="e")

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
