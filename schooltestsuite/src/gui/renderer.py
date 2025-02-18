import platform
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk
from PIL import Image, ImageTk


def get_resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    else:
        return Path(__file__).parent.parent.parent / relative_path


class Renderer:
    def __init__(self, ui_callback, title):
        self.ui_callback = ui_callback

        self.root = tk.Tk()
        self.root.title(title)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # App icon
        self.set_icon()

        # UI parameters

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TButton", font=("Arial", 16), background="#b0c4d3", foreground="black"
        )
        style.configure("TEntry", font=("TkDefaultFont", 16))
        style.configure("TLabel", font=("TkDefaultFont", 20))

        # Frame construction
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.configure_frame(self.main_frame)

        self.frame1 = ttk.Frame(self.main_frame)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.configure_frame(self.frame1)

        self.frame2 = ttk.Frame(self.main_frame)
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.configure_frame(self.frame2)

    def set_icon(self):
        system_os = platform.system()
        if system_os == "Windows":
            icon_path = "src/gui/images/icon.ico"
        else:
            icon_path = "src/gui/images/icon.icns"
            icon = Image.open(get_resource_path(icon_path))
            icon_photo = ImageTk.PhotoImage(icon)
            self.root.iconphoto(True, icon_photo)

    def configure_frame(self, frame):
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def clean_screen(self):
        for frame in (self.frame1, self.frame2):
            for widget in frame.winfo_children():
                widget.destroy()

    def load_images(self, image_path):
        # Show the generating images screen
        self.label_image = ttk.Label(self.frame1)
        self.label_image.grid(row=0, column=0, padx=5, pady=5)
        image_chosen = get_resource_path(image_path)
        image = Image.open(image_chosen)
        self.tk_image = ImageTk.PhotoImage(image)
        self.label_image.config(image=self.tk_image)
        self.label_image.image = self.tk_image

    def load_label(self, text):
        # Show the generating label screen
        self.label_generating = ttk.Label(self.frame1, text=text)
        self.label_generating.grid(row=1, column=0, padx=5, pady=5)

    def create_button(self, text, command, row):
        button = ttk.Button(self.frame2, text=text, command=command)
        button.grid(row=row, column=0, padx=5, pady=5)

    def selection_screen(self, games):
        # Show the selection screen
        self.load_images("src/gui/images/intro.png")
        self.load_label("Scegli un gioco:")
        for idx, category in enumerate(games):
            self.create_button(
                category, lambda c=category: self.start_game(games[c]), idx
            )

    def start_game(self, game_function):
        # Destroy the selection screen and start the chosen game
        self.root.destroy()
        game_function()

    def get_name(self):
        # Show the username selection screen
        self.load_images("src/gui/images/name.png")
        self.load_label("Benvenuto! Inserisci il tuo nome:")
        name_entry = ttk.Entry(self.frame2, width=30)
        name_entry.grid(row=0, column=0, padx=5, pady=5)
        self.create_button(
            "Invia", lambda: self.ui_callback("assign_username", name_entry.get()), 1
        )

    def get_difficulty(self, difficulties):
        # Show the difficulty selection screen
        self.clean_screen()
        self.load_images("src/gui/images/difficulty.png")
        self.load_label("Scegli la difficoltà:")
        for idx, difficulty in enumerate(difficulties):
            self.create_button(
                difficulty,
                lambda d=difficulty: self.ui_callback("assign_difficulty", d),
                idx,
            )

    def setup_gui_images(self):
        # Image Label
        self.clean_screen()
        self.label_image = ttk.Label(self.frame1)
        self.label_image.grid(row=0, column=0, padx=5, pady=5)

    def answers_button(self, categories):
        # Dynamic buttons creation
        for idx, category in enumerate(categories):
            self.create_button(
                category, lambda c=category: self.ui_callback("check_answer", c), idx
            )

    def next_image(self, image):
        # Show the next image
        self.tk_image = ImageTk.PhotoImage(image)
        self.label_image.config(image=self.tk_image)
        self.label_image.image = self.tk_image

    def correct_answer(self):
        # Show a message for a correct answer
        messagebox.showinfo("Corretto", "Bravo, risposta esatta!")

    def wrong_answer(self):
        # Show a message for a wrong answer
        messagebox.showerror("Non corretto", "Mi dispiace, riprova!")

    def end_game(self, data):
        # Show the chart and end the game
        self.clean_screen()

        for idx, (left_value, right_value) in enumerate(data):
            self.frame1.rowconfigure(idx, weight=1)
            for col, text, anchor in [
                (0, left_value, "w"),
                (1, "." * 20, "center"),
                (2, right_value, "e"),
            ]:
                label = ttk.Label(self.frame1, text=text, anchor=anchor)
                label.grid(row=idx, column=col, padx=5, pady=5, sticky="ew")

        exit_button = ttk.Button(self.frame2, text="Esci", command=self.root.destroy)
        exit_button.grid(row=0, column=0, pady=5)

    def run(self):
        # Start the main loop
        self.root.mainloop()
