from datetime import datetime
from pathlib import Path


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

    def duration_minutes(self, start=None, stop=None):
        if start != None and stop != None:
            fmt = "%H:%M"
            stop_time = datetime.strptime(stop,fmt)
            start_time = datetime.strptime(start,fmt)
            diff =  stop_time - start_time
        elif self.start_time and self.stop_time:
            diff = self.stop_time - self.start_time
        else:
            diff = None
        return diff.total_seconds() / 60


    def add_date(self):
        self.date_at_add = datetime.now().strftime("%Y-%m-%d")
        return self.date_at_add

    def ticket_id_extractor(self):
        ticket_id_list = []
        with open("timeSheetFiller.txt", "rt") as f:
            for line_number, line in enumerate (f,start=0):
                if line_number >= 1:
                    line = line.split(";",2)
                    if line[0] != "":
                        ticket_id_list.append(line[0])
        return ticket_id_list



class TimesheetWriter:
    HEADER = "JIRA_ID;Task;Start;Stop;Minutes;Actual_date\n"
    def __init__(self, filename="timeSheetFiller.txt"):
        self.file = Path(filename)

    def write_entry(self, jira, task, start, stop, minutes, actual_date):
        if not self.file.exists():
            self._create_file()

        line = (
            f"{jira};"
            f"{task};"
            f"{start};"
            f"{stop};"
            f"{minutes};"
            f"{actual_date}\n"
        )

        with self.file.open("a", encoding="utf-8") as f:
            f.write(line)

    def _create_file(self):
        self.file.write_text(self.HEADER, encoding="utf-8")

