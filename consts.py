from pathlib import Path

from PyQt5.QtCore import QSize


RESOURCES_PATH = Path('resources')
LOADING_SPINNER = RESOURCES_PATH / 'ajax-loader.gif'

RESOLUTION = QSize(600, 400)

DEFAULT_K_COUNT = 3

NODE_COLORS = ["r", "b", "g"]
