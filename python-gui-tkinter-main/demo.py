import tkinter as tk
from tkinter import Menu

# Function to be called when a menu item is selected
def dummy_function():
    print("Menu item selected")

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create a menubar
menubar = Menu(root)

# Create a File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=dummy_function)
file_menu.add_command(label="Open", command=dummy_function)
file_menu.add_command(label="Save", command=dummy_function)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

# Create an Edit menu
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=dummy_function)
edit_menu.add_command(label="Redo", command=dummy_function)

# Add Edit menu to the menubar
menubar.add_cascade(label="Edit", menu=edit_menu)

# Create a Help menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=dummy_function)

# Add Help menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu)

# Configure the menubar for the main window
root.config(menu=menubar)

# Add a simple label for the calculator interface (you can replace this with your calculator code)
label = tk.Label(root, text="Calculator Interface Here")
label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
