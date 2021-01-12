import sys
from concurrent.futures.thread import ThreadPoolExecutor

from PyQt5.QtWidgets import QApplication

from consts import RESOLUTION
from ui.window import MainWindow


def main():
    with ThreadPoolExecutor(max_workers=1) as executor:
        app = QApplication(sys.argv)

        window = MainWindow(executor)
        window.setWindowTitle('Daily Transportation')
        window.setFixedSize(RESOLUTION)
        window.start()

        app.exec_()


if __name__ == '__main__':
    main()
