import tkinter as tk
from UI import TimeTrackerUI

def main():
    root = tk.Tk()
    app = TimeTrackerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
