import random
from pathlib import Path
from PIL import Image


class ImageManager:
    def __init__(self, base_directory, data_manager):
        # Initialize the ImageManager with a base directory and a DataManager instance
        self.base_directory = Path(base_directory)
        self.data_manager = data_manager
        self.preloaded_images = {}

    def select_images(self, max_images_per_category):
        # Randomly select a limited number of images per category
        selected_images = {}
        for category, image_list in self.data_manager.data.items():
            selected_images[category] = random.sample(
                image_list, max_images_per_category
            )
        return selected_images

    def preload_images(self, selected_images):
        # Preload selected images into memory for faster access
        for category, image_filenames in selected_images.items():
            self.preloaded_images[category] = []
            for image_filename in image_filenames:
                image_path = self.base_directory / category / image_filename
                img = Image.open(image_path)
                self.preloaded_images[category].append(img)
        return self.preloaded_images
