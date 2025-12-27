from pathlib import Path

class TimesheetWriter:
    def __init__(self, filename="timeSheetFiller.txt"):
        self.file = Path(filename)

        if not self.file.exists():
            self.file.write_text(
                "JIRA_ID;Task;Start;Stop;Minutes\n",
                encoding="utf-8"
            )

    def write_entry(self, jira, task, start, stop, minutes):
        with self.file.open("a", encoding="utf-8") as f:
            f.write(
                f"{jira};{task};"
                f"{start};{stop};"
                f"{minutes:.2f}\n"
            )
