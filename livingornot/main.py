import os
from renderer import Renderer

if __name__ == "__main__":
    # Image folder and image list file path
    ABSOLUTE_PATH = "./livingornot/data/images"
    MAIN_DIR = os.path.join(os.path.dirname(__file__), "data/image_list/images.json")

    # GUI start
    app = Renderer(ABSOLUTE_PATH, MAIN_DIR)
    app.run()
