from pathlib import Path

from PyQt5.QtCore import QSize

import matplotlib.colors as mcolors


RESOURCES_PATH = Path('resources')
LOADING_SPINNER = RESOURCES_PATH / 'ajax-loader.gif'

OUTPUT_PATH = Path('output')
GROUP_CANVAS_PATH = OUTPUT_PATH / 'clustering.png'
ALL_ROUTES_CANVAS_PATH = OUTPUT_PATH / 'GT.png'
SINGLE_ROUTE_CANVAS_NAME = 'G{group_num}.png'

RESOLUTION = QSize(600, 400)

DEFAULT_K_COUNT = 3

NODE_COLORS = list(mcolors.BASE_COLORS.keys())
# ["r", "b", "g", "r"]
