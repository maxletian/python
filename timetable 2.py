import datetime
import tkinter as tk
from tkinter import ttk

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Scheduler")

        self.schedule = {}

        self.create_widgets()

    def create_widgets(self):
        # Date entry
        ttk.Label(self.root, text="Enter Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        # Event entry
        ttk.Label(self.root, text="Enter Event:").grid(row=1, column=0, padx=10, pady=5)
        self.event_entry = ttk.Entry(self.root)
        self.event_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        ttk.Button(self.root, text="Add Event", command=self.add_event).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="View Events", command=self.view_events).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.destroy).grid(row=4, column=0, columnspan=2, pady=10)

    def add_event(self):
        date_str = self.date_entry.get()
        event = self.event_entry.get()

        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date not in self.schedule:
                self.schedule[date] = [event]
            else:
                self.schedule[date].append(event)

            print("Event added successfully!")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def view_events(self):
        date_str = self.date_entry.get()

        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date in self.schedule:
                events = "\n".join(self.schedule[date])
                tk.messagebox.showinfo(f"Events on {date}", events)
            else:
                tk.messagebox.showinfo("No Events", f"No events scheduled on {date}.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def main():
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
