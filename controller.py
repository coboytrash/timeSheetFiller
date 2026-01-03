class TimeTrackerController:
    def __init__(self, model, writer, view):
        self.model = model
        self.writer = writer
        self.view = view
        self.always_on_top = False

        self.bind_events()

    def bind_events(self):
        self.view.start_btn.config(command=self.start_clicked)
        self.view.stop_btn.config(command=self.stop_clicked)
        self.view.add_btn.config(command=self.add_clicked)
        self.view.top_btn.config(command=self.toggle_top)

    def start_clicked(self):
        start = self.model.start()
        self.view.start_label.config(text=start.strftime("%Y-%m-%d %H:%M:%S"))

    def stop_clicked(self):
        stop = self.model.stop()
        minutes = self.model.duration_minutes()
        self.view.stop_label.config(text=stop.strftime("%Y-%m-%d %H:%M:%S"))
        self.view.minutes_label.config(text=f"{minutes:.2f}")

    def add_clicked(self):
        jira, task = self.view.get_form_data()
        minutes = self.model.duration_minutes()

        if minutes is None:
            return

        self.writer.write_entry(
            jira,
            task,
            self.view.start_label.cget("text"),
            self.view.stop_label.cget("text"),
            minutes,
        )
        self.view.clear()

    def toggle_top(self):
        self.always_on_top = not self.always_on_top
        self.view.root.attributes("-topmost", self.always_on_top)
        status = "ON" if self.always_on_top else "OFF"
        self.view.top_btn.config(text=f"A.O.T. {status}")
