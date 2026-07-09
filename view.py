import tkinter as tk

class TimeTrackerView:
    def __init__(self, root):
        self.root = root
        self.root.title("Timesheet Filler")

        self.dock_left(width=100)
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Ticket ID").grid(row=0, column=0, sticky="w")
        tk.Label(self.root, text="Description").grid(row=4, column=0, sticky="nw")
        tk.Label(self.root, text="Minutes").grid(row=11, column=0, sticky="w")
        tk.Label(self.root, text="Last Tasks").grid(row=2, column=0, sticky="w")

        self.ticket_entry = tk.Entry(self.root, width=16)
        self.desc_text = tk.Text(self.root, width=14, height=10, wrap="word")
        self.start_entry = tk.Entry(self.root, width=16)
        self.stop_entry = tk.Entry(self.root, width=16)
        self.minutes_entry = tk.Entry(self.root, width=10)

        self.ticket_entry.grid(row=1, column=0, sticky="w", pady = (0, 10))
        self.desc_text.grid(row=5, column=0, sticky="w", pady = (0, 20))
        self.start_entry.grid(row=8, column=0, sticky="w", pady = (3, 10))
        self.stop_entry.grid(row=10, column=0, sticky="w", pady = (3, 10))
        self.minutes_entry.grid(row=12, column=0, sticky="w", pady = (0, 10))

        self.start_btn = tk.Button(self.root, text="Start")
        self.stop_btn = tk.Button(self.root, text="Stop")
        self.add_btn = tk.Button(self.root, text="Add Task")
        self.top_btn = tk.Button(self.root, text="A.O.T. OFF")
        self.cl_btn = tk.Button(self.root, text="⌛", width=5)

        self.start_btn.grid(row=7, column=0, sticky="ew")
        self.stop_btn.grid(row=9, column=0, sticky="ew")
        self.add_btn.grid(row=13, column=0, sticky="ew", pady = (0, 10))
        self.top_btn.grid(row=14, column=0, sticky="ew")
        self.cl_btn.grid(row=12, column=0, sticky="e", pady = (0, 10))

        self.history_sel = tk.Listbox(master=None,cnf={},selectmode=tk.BOTH)
        self.history_sel.grid(row=3, column=0, sticky="nw")

    def get_form_data(self):
        return (
            self.ticket_entry.get(),
            self.desc_text.get("1.0", "end-1c")
        )

    def clear(self):
        self.ticket_entry.delete(0, "end")
        self.desc_text.delete("1.0", "end")
        self.start_entry.delete(0,"end")
        self.stop_entry.delete(0,"end")
        self.minutes_entry.delete(0, "end")
        self.history_sel.delete(0, tk.END)

    def dock_left(self, width=260):
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{screen_height}+0+0")
        self.root.resizable(width=True, height=False)

    def ticket_id_with_counts(self,history_sel_data):
        for history_sel_data_count in history_sel_data:
            self.history_sel.insert(tk.END, history_sel_data_count[0])

    def get_selected_ticket_from_list(self):
        ticket_index = self.history_sel.curselection()
        selected_ticket = ",".join([self.history_sel.get(i) for i in ticket_index])
        return selected_ticket

    def set_selected_ticket_to_list(self,selected_ticket):
        if selected_ticket != "":
            self.ticket_entry.delete(0, "end")
            self.ticket_entry.insert(tk.END, selected_ticket)
        else:
            self.ticket_entry.insert(tk.END, selected_ticket)