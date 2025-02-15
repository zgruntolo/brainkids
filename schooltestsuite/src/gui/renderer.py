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
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.frame1 = ttk.Frame(self.main_frame)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(0, weight=1)

        self.frame2 = ttk.Frame(self.main_frame)
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)

    def clean_screen(self):
        for frame in (self.frame1, self.frame2):
            for widget in frame.winfo_children():
                widget.destroy()

    def selection_screen(self, games):
        # Show the selection screen
        self.label_image = ttk.Label(self.frame1)
        self.label_image.grid(row=0, column=0, padx=5, pady=5)
        image_path = get_resource_path("src/gui/images/intro.png")
        image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(image)
        self.label_image.config(image=self.tk_image)
        self.label_image.image = self.tk_image
        self.label_selection = ttk.Label(self.frame1, text="Scegli un gioco:")
        self.label_selection.grid(row=1, column=0, padx=5, pady=5)
        for idx, category in enumerate(games):
            button = ttk.Button(
                self.frame2,
                text=category,
                command=lambda c=category: self.start_game(games[c]),
            )
            button.grid(row=idx, column=0, padx=5, pady=5)

    def start_game(self, game_function):
        # Destroy the selection screen and start the single game
        self.root.destroy()
        game_function()

    def setup_gui_images(self):
        # Image Label
        self.clean_screen()
        self.label_image = ttk.Label(self.frame1)
        self.label_image.grid(row=0, column=0, padx=5, pady=5)

    def create_buttons(self, categories):
        # Dynamic buttons creation
        for idx, category in enumerate(categories):
            button = ttk.Button(
                self.frame2,
                text=category,
                command=lambda c=category: self.ui_callback("check_answer", c),
            )
            button.grid(row=idx, column=0, padx=5, pady=5)

    def next_image(self, image):
        # Show the next image
        self.tk_image = ImageTk.PhotoImage(image)
        self.label_image.config(image=self.tk_image)
        self.label_image.image = self.tk_image

    def get_name(self):
        # Show the username selection screen
        self.label_image = ttk.Label(self.frame1)
        self.label_image.grid(row=0, column=0, padx=5, pady=5)
        image_path = get_resource_path("src/gui/images/intro.png")
        image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(image)
        self.label_image.config(image=self.tk_image)
        self.label_image.image = self.tk_image
        name_label = ttk.Label(self.frame1, text="Benvenuto! Inserisci il tuo nome:")
        name_label.grid(row=1, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(self.frame2, width=30)
        name_entry.grid(row=0, column=0, padx=5, pady=5)
        button = ttk.Button(
            self.frame2,
            text="Invia",
            command=lambda: self.ui_callback("assign_username", name_entry.get()),
        )
        button.grid(row=1, column=0, padx=5, pady=5)

    def get_difficulty(self, difficulties):
        # Show the difficulty selection screen
        self.clean_screen()
        difficulty_label = ttk.Label(self.frame1, text="Scegli la difficoltà:")
        difficulty_label.grid(row=0, column=0, padx=5, pady=5)
        for idx, difficulty in enumerate(difficulties):
            button = ttk.Button(
                self.frame2,
                text=difficulty,
                command=lambda d=difficulty: self.ui_callback("assign_difficulty", d),
            )
            button.grid(row=idx, column=0, padx=5, pady=5)

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
