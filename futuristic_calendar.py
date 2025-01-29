import tkinter as tk
from tkinter import ttk
import calendar
from tkinter import font as tkfont

class FuturisticCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Futuristic Calendar")
        self.root.geometry("600x500")
        self.root.configure(bg="#0A0F24")  # Dark futuristic background

        # Custom Fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.day_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        self.date_font = tkfont.Font(family="Helvetica", size=12)

        # Variables
        self.year = 2025
        self.month = 1  # Janaury

        # Header Frame
        self.header_frame = tk.Frame(self.root, bg="#1A1F2E")
        self.header_frame.pack(fill="x", padx=20, pady=10)

        # Year and Month Navigation
        self.prev_button = tk.Button(
            self.header_frame,
            text="◀",
            font=self.title_font,
            bg="#2C3240",
            fg="#00FFCC",
            bd=0,
            activebackground="#00FFCC",
            activeforeground="#0A0F24",
            command=self.prev_month,
        )
        self.prev_button.pack(side="left", padx=10)

        self.month_label = tk.Label(
            self.header_frame,
            text=f"{calendar.month_name[self.month]} {self.year}",
            font=self.title_font,
            bg="#1A1F2E",
            fg="#00FFCC",
        )
        self.month_label.pack(side="left", expand=True)

        self.next_button = tk.Button(
            self.header_frame,
            text="▶",
            font=self.title_font,
            bg="#2C3240",
            fg="#00FFCC",
            bd=0,
            activebackground="#00FFCC",
            activeforeground="#0A0F24",
            command=self.next_month,
        )
        self.next_button.pack(side="right", padx=10)

        # Calendar Frame
        self.calendar_frame = tk.Frame(self.root, bg="#0A0F24")
        self.calendar_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create Calendar
        self.create_calendar()

    def create_calendar(self):
        # Clear previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Get calendar data
        cal = calendar.monthcalendar(self.year, self.month)

        # Weekday Headers
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(weekdays):
            label = tk.Label(
                self.calendar_frame,
                text=day,
                font=self.day_font,
                bg="#1A1F2E",
                fg="#00FFCC",
                width=10,
                relief="flat",
            )
            label.grid(row=0, column=i, padx=5, pady=5)

        # Add days to the calendar
        for week_num, week in enumerate(cal, start=1):
            for day_num, day in enumerate(week):
                if day != 0:
                    day_frame = tk.Frame(
                        self.calendar_frame,
                        bg="#1A1F2E",
                        bd=2,
                        relief="flat",
                        highlightbackground="#00FFCC",
                        highlightthickness=1,
                    )
                    day_frame.grid(row=week_num, column=day_num, padx=5, pady=5, sticky="nsew")

                    day_label = tk.Label(
                        day_frame,
                        text=str(day),
                        font=self.date_font,
                        bg="#1A1F2E",
                        fg="#FFFFFF",
                        width=10,
                    )
                    day_label.pack(fill="both", expand=True)

                    # Hover effect
                    day_frame.bind("<Enter>", lambda e, f=day_frame: self.on_hover(f))
                    day_frame.bind("<Leave>", lambda e, f=day_frame: self.on_leave(f))

    def on_hover(self, frame):
        frame.config(bg="#00FFCC")
        for widget in frame.winfo_children():
            widget.config(bg="#00FFCC", fg="#0A0F24")

    def on_leave(self, frame):
        frame.config(bg="#1A1F2E")
        for widget in frame.winfo_children():
            widget.config(bg="#1A1F2E", fg="#FFFFFF")

    def prev_month(self):
        self.month -= 1
        if self.month < 1:
            self.month = 12
            self.year -= 1
        self.update_calendar()

    def next_month(self):
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        self.update_calendar()

    def update_calendar(self):
        self.month_label.config(text=f"{calendar.month_name[self.month]} {self.year}")
        self.create_calendar()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FuturisticCalendarApp(root)
    root.mainloop()