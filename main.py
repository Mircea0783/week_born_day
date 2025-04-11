import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def get_day_of_week():
    try:
        # Get the date from the entry field
        date_input = entry_date.get()

        # Parse the date (expecting DD.MM.YYYY)
        date_obj = datetime.strptime(date_input, "%d.%m.%Y")

        # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = date_obj.weekday()
        result = days[day_index]

        # Update the result label
        result_label.config(text=f"The day of the week was: {result}")

    except ValueError:
        # Show error message if date format is invalid
        messagebox.showerror("Invalid Input", "Please enter a valid date in the format DD.MM.YYYY (e.g., 15.07.1983)")


# Create the main window
root = tk.Tk()
root.title("Day of Birth Calculator")
root.geometry("400x200")  # Set window size

# Create and place widgets
# Label for instructions
label_instruction = tk.Label(root, text="Enter your date of birth (DD.MM.YYYY):")
label_instruction.pack(pady=10)

# Entry field for date input
entry_date = tk.Entry(root, width=20)
entry_date.pack(pady=10)

# Button to calculate
calc_button = tk.Button(root, text="Calculate Day", command=get_day_of_week)
calc_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
