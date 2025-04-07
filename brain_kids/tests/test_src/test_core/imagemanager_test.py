from pathlib import Path
from PIL import Image
from core.datamanager import DataManager
from core.imagemanager import ImageManager
import unittest

ABSOLUTE_PATH = Path(__file__).parent.parent.parent / "test_data" / "test"
TEST_IMAGE_PATH = ABSOLUTE_PATH / "files" / "images.json"
IMAGE_DIRECTORY = ABSOLUTE_PATH / "images"


class TestImage(unittest.TestCase):

    def test_load_selected_images(self):
        image_dictionary = DataManager()
        image_dictionary.load(TEST_IMAGE_PATH)

        images = ImageManager(IMAGE_DIRECTORY, image_dictionary)

        selected_images = images.select_images(1)
        selected_images_list = selected_images.get("Viventi", "Non Viventi")
        self.assertTrue(
            any(
                image in ["pappagallo.jpg", "bandiera.jpg"]
                for image in selected_images_list
            )
        )

        preloaded_images = images.preload_images(selected_images)
        self.assertEqual(len(preloaded_images), 2)
        for img in preloaded_images.get("Viventi", "Non Viventi"):
            self.assertIsInstance(img, Image.Image)


if __name__ == "__main__":
    unittest.main()
