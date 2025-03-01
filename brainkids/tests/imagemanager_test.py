from pathlib import Path
from PIL import Image
from src.core.datamanager import DataManager
from src.core.imagemanager import ImageManager
import unittest

ABSOLUTE_PATH = Path(__file__).parent
TEST_IMAGE_PATH = ABSOLUTE_PATH / "test_data/images.json"
IMAGE_DIRECTORY = ABSOLUTE_PATH / "test_data/images"


class TestImage(unittest.TestCase):

    def test_load_selected_images(self):
        image_dictionary = DataManager()
        image_dictionary.load(TEST_IMAGE_PATH)

        images = ImageManager(IMAGE_DIRECTORY, image_dictionary)

        selected_images = images.select_images(1)
        selected_images_list = selected_images.get("Viventi", [])
        self.assertTrue(
            any(
                image in ["pappagallo.jpg", "pesce.jpg", "quercia.jpg"]
                for image in selected_images_list
            )
        )

        preloaded_images = images.preload_images(selected_images)
        self.assertEqual(len(preloaded_images), 1)
        for img in preloaded_images.get("Viventi", []):
            self.assertIsInstance(img, Image.Image)


if __name__ == "__main__":
    unittest.main()
