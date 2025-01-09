import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Pillow library for handling images

# Opprett hovedvinduet
window = tk.Tk()
window.geometry("600x400")
window.title("Sorted")

# Last inn et mappikon (PNG eller GIF)
folder_icon_path = "./images/Folder_icon_1.png"  # Sett inn banen til bildet ditt
folder_icon_img = Image.open(folder_icon_path).resize((32, 32))  # Endre størrelse
folder_icon = ImageTk.PhotoImage(folder_icon_img)


def handle_button_press(event):
    """Lukk programmet når knappen trykkes."""
    window.destroy()


def browse_folder():
    """Åpne en dialogboks for å velge mappe og vise mappeikon og navn."""
    folder_path = filedialog.askdirectory()  # Åpne en mappevalg-dialog
    if folder_path:
        display_folder(folder_path)  # Vis ikon og navn for valgt mappe


def display_folder(folder_path):
    """Vis mappeikon og navnet på den valgte mappen."""
    folder_name = os.path.basename(folder_path)  # Få kun mappenavnet fra path

    # Fjern tidligere elementer fra vinduet
    for widget in folder_frame.winfo_children():
        widget.destroy()

    # Opprett ikon og tekst som vises under hverandre
    icon_label = tk.Label(folder_frame, image=folder_icon)
    icon_label.pack(pady=5)

    folder_name_label = tk.Label(folder_frame, text=folder_name, font=("Arial", 15))
    folder_name_label.pack(pady=5)


# Opprett og stil knappen for å bla gjennom mapper
browse_button = tk.Button(
    window,
    text="Browse Folder",
    command=browse_folder,
    font=("Arial", 12),
    fg="black",
    relief="solid",
    bd=1,
    padx=10,
    pady=5,
)
browse_button.pack(pady=15)

# Opprett en ramme for å vise mappeikon og navn
folder_frame = tk.Frame(window, bg="#ffffff", width=400, height=300)
folder_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

# Start hovedløkken (event loop)
window.mainloop()