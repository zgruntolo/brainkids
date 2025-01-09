import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from src.randomimageselection import RandomImageSelector
from src.state import State


class Renderer:
    def __init__(self, absolute_path, json):
        self.absolute_path = absolute_path
        self.json = json
        self.categories = RandomImageSelector(json)
        self.root = tk.Tk()
        self.root.title("Vivente o Non Vivente")
        self.label_image = None
        self.current_image = None
        self.state = State()
        self.setup_gui()

    def setup_gui(self):
        # Image Label
        self.label_image = tk.Label(self.root, width=300, height=300)
        self.label_image.pack()

        # Dynamic button generation
        for key in self.categories.image.data.keys():
            button = tk.Button(
                self.root, text=key, command=lambda k=key: self.check_answer(k)
            )
            button.pack(side=tk.TOP, padx=20)
        self.show_image()

    # Open image and show it on the GUI
    def show_image(self):
        chosen_image = self.categories.select_image()
        current_image = os.path.join(
            self.absolute_path, self.state.category, chosen_image
        )
        img = Image.open(current_image)
        img = img.resize((300, 300))
        image_tk = ImageTk.PhotoImage(img)
        self.label_image.config(image=image_tk)
        self.label_image.image = image_tk
        if self.state.counter > 5:
            self.end()

    # Check if answer is right or wrong
    def check_answer(self, answer):
        if answer == self.state.category:
            messagebox.showinfo("Corretto", "Bravo, risposta esatta!")
        else:
            messagebox.showerror("Non corretto", "Mi dispiace, riprova!")
        self.show_image()

    def end(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        scritta = tk.Label(self.root, text="Bravo, hai terminato!", font=("Arial", 20))
        scritta.pack()

    def run(self):
        # Start the main loop
        self.root.mainloop()
