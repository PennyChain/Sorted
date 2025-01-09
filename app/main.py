import os
import shutil
import tkinter as tk
from collections import defaultdict

window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()


button = tk.Button(text="My simple app.")
button.bind("Button", handle_button_press)
button.pack()

# Start the event loop.
window.mainloop()