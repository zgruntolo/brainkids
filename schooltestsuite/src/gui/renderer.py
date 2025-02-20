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
        style.configure(".", background="#f0f8ff")
        style.configure(
            "TButton", font=("Arial", 16), background="#7fffd4", foreground="black"
        )
        style.configure("TEntry", font=("TkDefaultFont", 16))
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
        icon_ext = "ico" if system_os == "Windows" else "icns" if system_os == "Darwin" else "png"
        icon_path = get_resource_path(f"src/gui/images/icon.{icon_ext}")

        if system_os == "Windows":
            self.root.iconbitmap(icon_path)
        else:
            icon = Image.open(icon_path)
            self.root.iconphoto(True, ImageTk.PhotoImage(icon))

    def configure_grid(self, frame):
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

    def clean_screen(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        self.text_label.destroy()

    def display_image(self, image_path):
        # Show the generating images screen
        image_file_path = get_resource_path(image_path)
        image = Image.open(image_file_path)
        self.tk_image = ImageTk.PhotoImage(image)
        if not hasattr(self, "image_label") or not self.image_label.winfo_exists():
            self.image_label = ttk.Label(self.image_frame)
            self.image_label.grid(row=0, column=0, padx=5, pady=5)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def display_text(self, text):
        # Show the generating label screen
        self.text_label = ttk.Label(self.image_frame, text=text)
        self.text_label.grid(row=1, column=0, padx=5, pady=5)

    def create_action_button(self, text, command, row):
        button = ttk.Button(self.button_frame, text=text, command=command)
        button.grid(row=row, column=0, padx=5, pady=5)

    def show_game_selection_screen(self, game_option):
        # Show the selection screen
        self.display_image("src/gui/images/intro.png")
        self.display_text("Scegli un gioco:")
        for idx, game_name in enumerate(game_option):
            self.create_action_button(
                game_name, lambda g=game_name: self.start_game(game_option[g], g), idx
            )

    def start_game(self, game_function, game_title):
        # Switch between the game selection screen and the game screen
        self.clean_screen()
        self.root.title(game_title)
        game_function(self)

    def request_player_name(self):
        # Show the username selection screen
        self.display_image("src/gui/images/name.png")
        self.display_text("Benvenuto! Inserisci il tuo nome:")
        
        name_entry = ttk.Entry(self.button_frame, width=30)
        name_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.create_action_button(
            "Invia", lambda: self.game_callback("assign_username", name_entry.get()), 1
        )

    def request_game_difficulty(self, difficulty_levels):
        # Show the difficulty selection screen
        self.clean_screen()
        self.display_image("src/gui/images/difficulty.png")
        self.display_text("Scegli la difficoltà:")
        for idx, difficulty in enumerate(difficulty_levels):
            self.create_action_button(
                difficulty,
                lambda d=difficulty: self.game_callback("assign_difficulty", d),
                idx,
            )

    def update_game_image(self, image):
        # Show the next image
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def show_answers_button(self, answer_options):
        # Dynamic buttons creation
        self.clean_screen()
        for idx, category in enumerate(answer_options):
            self.create_action_button(
                category, lambda c=category: self.game_callback("check_answer", c), idx
            )

    def show_correct_answer_message(self):
        # Show a message for a correct answer
        messagebox.showinfo("Corretto", "Bravo, risposta esatta!")

    def show_wrong_answer_message(self):
        # Show a message for a wrong answer
        messagebox.showerror("Non corretto", "Mi dispiace, riprova!")

    def display_game_results(self, results_data):
        # Show the chart and end the game
        for frame in (self.image_frame, self.button_frame):
            for widget in frame.winfo_children():
                widget.destroy()

        self.display_text("Risultati del gioco:")

        for idx, (player_name, score) in enumerate(results_data):
            self.image_frame.rowconfigure(idx, weight=1)
            for col, text, anchor in [
                (0, player_name, "w"),
                (1, "." * 20, "center"),
                (2, score, "e"),
            ]:
                label = ttk.Label(self.image_frame, text=text, anchor=anchor)
                label.grid(row=idx, column=col, padx=5, pady=5, sticky="ew")

        exit_button = ttk.Button(self.button_frame, text="Esci", command=self.root.destroy)
        exit_button.grid(row=0, column=0, pady=5)

    def run(self):
        # Start the main loop
        self.root.mainloop()