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
    def __init__(self, game_callback, window_title):
        self.game_callback = game_callback

        self.root = tk.Tk()
        self.root.title(window_title)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # App icon
        self.set_application_icon()

        # UI parameters
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background="#778899")

        style.configure("TButton", font=("Arial", 16), borderwidth=2)
        style.map(
            "TButton",
            background=[
                ("pressed", "#5f9ea0"),
                ("active", "#add8e6"),
                ("!disabled", "#E6E6FA"),
            ],
            foreground=[("active", "black"), ("!disabled", "black")],
            bordercolor=[("focus", "#2f4f4f"), ("!focus", "#2f4f4f")],
            relief=[("pressed", "sunken"), ("!pressed", "raised")],
        )

        style.configure("TEntry", font=("TkDefaultFont", 16), fieldbackground="#f0ffff")
        style.configure("TEntryFocus", fieldbackground="#b0e0e6")
        style.configure("TLabel", font=("TkDefaultFont", 20))

        # Frame construction
        self.main_container = ttk.Frame(self.root)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.configure_grid(self.main_container)

        self.image_frame = ttk.Frame(self.main_container)
        self.image_frame.grid(row=0, column=0, sticky="nsew")
        self.configure_grid(self.image_frame)

        self.button_frame = ttk.Frame(self.main_container)
        self.button_frame.grid(row=1, column=0, sticky="nsew")
        self.configure_grid(self.button_frame)

    def set_application_icon(self):
        system_os = platform.system()
        icon_ext = (
            "ico"
            if system_os == "Windows"
            else "icns" if system_os == "Darwin" else "png"
        )
        icon_path = get_resource_path(f"data/gui/images/icon.{icon_ext}")

        if system_os == "Windows":
            self.root.iconbitmap(icon_path)
        else:
            icon = Image.open(icon_path)
            self.root.iconphoto(True, ImageTk.PhotoImage(icon))

    def configure_grid(self, frame):
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def clean_screen(self, remove_image_label=False):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        if hasattr(self, "text_label") and self.text_label.winfo_exists():
            self.text_label.destroy()
        if (
            remove_image_label
            and hasattr(self, "image_label")
            and self.image_label.winfo_exists()
        ):
            self.image_label.destroy()

    def display_image(self, image_source):
        # Show the generating images screen
        if isinstance(image_source, str):
            image_file_path = get_resource_path(image_source)
            image = Image.open(image_file_path)
        else:
            image = image_source
        self.tk_image = ImageTk.PhotoImage(image)
        if not hasattr(self, "image_label") or not self.image_label.winfo_exists():
            self.image_label = ttk.Label(self.image_frame)
            self.image_label.grid(row=0, column=0, padx=5, pady=5)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def display_text(self, text):
        # Show the generating label screen
        if not hasattr(self, "text_label") or not self.text_label.winfo_exists():
            self.text_label = ttk.Label(
                self.image_frame, text=text, anchor="center", justify="center"
            )
            self.text_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        else:
            self.text_label.config(text=text)

    def create_action_button(self, text, command, row, column=0, columnspan=1):
        button = ttk.Button(self.button_frame, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def create_buttons(self, options, callback):
        self.clean_screen()
        for idx, option in enumerate(options):
            self.create_action_button(option, lambda opt=option: callback(opt), idx)

    def update_screen(self, image_path=None, text=None):
        if image_path:
            self.display_image(image_path)
        if text:
            self.display_text(text)

    def show_game_selection_screen(self, game_option):
        # Show the selection screen
        self.update_screen("data/gui/images/intro.png", "Scegli un gioco:")
        self.create_buttons(game_option, lambda g: self.start_game(game_option[g], g))

    def start_game(self, game_function, game_title):
        # Switch between the game selection screen and the game screen
        self.clean_screen()
        self.root.title(game_title)
        game_function(self)

    def request_player_name(self):
        # Show the username selection screen
        self.update_screen(
            "data/gui/images/name.png", "Benvenuto! Inserisci il tuo nome:"
        )
        name_entry = ttk.Entry(self.button_frame, width=30)
        name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.create_action_button(
            "Invia",
            lambda: self.game_callback("assign_player_name", name_entry.get()),
            1,
        )

    def request_game_difficulty(self, difficulty_levels):
        # Show the difficulty selection screen
        self.update_screen("data/gui/images/difficulty.png", "Scegli la difficoltà:")
        self.create_buttons(
            difficulty_levels, lambda d: self.game_callback("set_game_difficulty", d)
        )

    def display_answers_button(self, answer_options):
        # Dynamic buttons creation
        self.create_buttons(
            answer_options, lambda c: self.game_callback("verify_player_answer", c)
        )

    def show_correct_answer_message(self):
        # Show a message for a correct answer
        messagebox.showinfo("Corretto", "Bravo, risposta esatta!")

    def show_wrong_answer_message(self):
        # Show a message for a wrong answer
        messagebox.showerror("Non corretto", "Mi dispiace, riprova!")

    def display_game_results(self, results_data):
        # Show the chart and end the game
        self.clean_screen(remove_image_label=True)

        results_label = ttk.Label(self.image_frame, text="Risultati del gioco:")
        results_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        for idx, (player_name, score) in enumerate(results_data, start=1):
            for col, text, anchor in [
                (0, player_name, "w"),
                (1, "." * 20, "center"),
                (2, score, "e"),
            ]:
                self.image_frame.columnconfigure(col, weight=1)
                label = ttk.Label(self.image_frame, text=text, anchor=anchor)
                label.grid(row=idx, column=col, padx=5, pady=5, sticky="ew")

        self.create_action_button("Esci", lambda: self.root.destroy(), 1)

    def run(self):
        # Start the main loop
        self.root.mainloop()
