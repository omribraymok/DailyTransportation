from concurrent.futures.thread import ThreadPoolExecutor

from PyQt5.QtWidgets import QMainWindow

from ui.calculation import Params, start_calculation, CalcTracker
from ui.calcwindow import CalculationWindow
from ui.startwindow import StartWindow


class MainWindow(QMainWindow):

    def __init__(self, executor: ThreadPoolExecutor):
        super().__init__()
        self._executor = executor

    def start(self):
        self._on_start_window()
        self.show()

    def _on_start_window(self):
        self.setCentralWidget(StartWindow(self._on_results_window))

    def _on_results_window(self, params: Params):
        calc_window = CalculationWindow(self._start_calculation, self._on_start_window)
        self.setCentralWidget(calc_window)

        calc_window.start(params)

    def _start_calculation(self, params: Params, tracker: CalcTracker):
        self._executor.submit(lambda p=params, t=tracker: start_calculation(p, t))
