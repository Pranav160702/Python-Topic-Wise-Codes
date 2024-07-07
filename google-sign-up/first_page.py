import tkinter as tk
from tkinter import ttk


# Create the main window
root = tk.Tk()
root.title("Create Google Account")
root.geometry('1000x500')
root .iconbitmap('google-sign-up/google_logo_icon_.ico')

# Center the window on the screen
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# Create a frame for the form and apply the style
frame = ttk.Frame(root, padding="20", style="TFrame")
frame.grid(row=0, column=0, padx=20, pady=20)

# Center the frame within the main window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid(row=0, column=0)

# Center the frame contents
for i in range(5):  # Number of rows in the frame
    frame.grid_rowconfigure(i, weight=1)
for i in range(3):  # Number of columns in the frame
    frame.grid_columnconfigure(i, weight=1)

# Title Label
title_label = ttk.Label(frame, text="Create a Google Account", font=("Helvetica", 18), background="white")
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Subtitle Label
subtitle_label = ttk.Label(frame, text="Enter your name", font=("Helvetica", 12), background="white")
subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))

# First Name Label and Entry
first_name_label = ttk.Label(frame, text="First name", background="white")
first_name_label.grid(row=2, column=1, sticky="w", pady=5)
first_name_entry = ttk.Entry(frame)
first_name_entry.grid(row=2, column=2, pady=5, sticky="e")

# Last Name Label and Entry
last_name_label = ttk.Label(frame, text="Last name (optional)", background="white")
last_name_label.grid(row=3, column=1, sticky="w", pady=5)
last_name_entry = ttk.Entry(frame)
last_name_entry.grid(row=3, column=2, pady=5, sticky="e")

# Next Button
next_button = ttk.Button(frame, text="Next")
next_button.grid(row=4, column=2, sticky="e", pady=20)

# Set padding for all child widgets
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)



root.mainloop()

