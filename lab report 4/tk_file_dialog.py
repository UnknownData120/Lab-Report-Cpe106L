# tk_file_dialog.py

import tkinter as tk
from tkinter import filedialog

def get_text_file():
    """Open a file dialog to select a text file and return the selected file path."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a text file", 
        filetypes=[("Text files", "*.txt")]
    )
    return file_path

if __name__ == '__main__':
    selected_file = get_text_file()
    if selected_file:
        print("Selected file:", selected_file)
    else:
        print("No file selected.")
