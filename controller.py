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

        self.view.stop_label.config(
            text=stop.strftime("%Y-%m-%d %H:%M:%S")
        )

        if not self.view.minutes_entry.get():
            self.view.minutes_entry.insert(0, f"{minutes:.2f}")

    def add_clicked(self):

        jira, task = self.view.get_form_data()
        start = self.view.start_label.cget("text")
        stop = self.view.stop_label.cget("text")

        minutes = self._get_minutes()
        if minutes is None:
            return  # invalid or missing data

        actual_date = self.model.add_date()

        self.writer.write_entry(
            jira=jira,
            task=task,
            start=start,
            stop=stop,
            minutes=f"{minutes:.2f}",
            actual_date=actual_date,
        )
        self.view.clear()

    def toggle_top(self):
        self.always_on_top = not self.always_on_top
        self.view.root.attributes("-topmost", self.always_on_top)
        status = "ON" if self.always_on_top else "OFF"
        self.view.top_btn.config(text=f"A.O.T. {status}")

    def _get_minutes(self):
        manual = self.view.minutes_entry.get().strip()

        if manual:
            try:
                return float(manual)
            except ValueError:
                return None

        return self.model.duration_minutes()