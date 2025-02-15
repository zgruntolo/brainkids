import random
from pathlib import Path
from PIL import Image


class ImageManager:
    def __init__(self, absolute_path, data):
        self.absolute_path = absolute_path
        self.data = data
        self.preloaded_images = {}

    def select_images(self, max_images_per_category):
        # Select a limited number of images per category
        selected_images = {}
        for category, images in self.data.data.items():
            selected_images[category] = random.sample(images, max_images_per_category)
        return selected_images

    def preload_images(self, selected_images):
        # Preload the selected images
        for category, images in selected_images.items():
            self.preloaded_images[category] = []
            for image_name in images:
                full_path = Path(self.absolute_path) / category / image_name
                img = Image.open(full_path)
                self.preloaded_images[category].append(img)
        return self.preloaded_images
