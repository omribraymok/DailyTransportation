from typing import Callable

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTabWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from algorithm import Result
from consts import LOADING_SPINNER
from graphs import plot_group_scatter, plot_combined_route, plot_group_route
from ui import dialogs
from ui.calculation import Params, CalcTracker
from ui.util import switch_layout


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class CalculationWindow(QFrame):

    def __init__(self, calc_func: Callable[[Params, CalcTracker], None],
                 back_window: Callable):
        super().__init__()

        self._calc_func = calc_func
        self._back_window = back_window

        self._calc_tracker = CalcTracker()
        self._calc_tracker.finished.connect(self._done_calculation)
        self._calc_tracker.error.connect(self._error_calculation)

        button_bar = QFrame()
        button_layout = QHBoxLayout()
        self._back_button = QPushButton('Back')
        self._back_button.setFixedSize(QSize(100, 30))
        self._back_button.setDisabled(True)
        self._back_button.clicked.connect(self._on_back)
        button_layout.addWidget(self._back_button, alignment=Qt.AlignRight)
        button_bar.setLayout(button_layout)

        self._center_bar = QFrame()

        loading_layout = QVBoxLayout()
        self._loading_label = QLabel()
        self._loading_movie = QMovie(str(LOADING_SPINNER))
        self._loading_label.setMovie(self._loading_movie)
        loading_layout.addWidget(self._loading_label)
        self._center_bar.setLayout(loading_layout)

        layout = QVBoxLayout()
        layout.addWidget(self._center_bar, alignment=Qt.AlignCenter)
        layout.addWidget(button_bar, alignment=Qt.AlignBottom)
        self.setLayout(layout)

    def start(self, params: Params):
        self._loading_label.show()
        self._loading_movie.start()

        self._calc_func(params, self._calc_tracker)

    def _on_back(self):
        self._back_window()

    def _done_calculation(self, result: Result):
        self._loading_movie.stop()
        self._loading_label.hide()
        self._back_button.setDisabled(False)

        group_canvas = self._plot_group_scatter(result)
        graphs_list, canvases = self._plot_group_routes(result)
        all_canvas = self._plot_combined_route(result, graphs_list)

        tabs = [('Groups', group_canvas), ('Routes', all_canvas)]
        for i, c in enumerate(canvases):
            tabs.append((f"Route {i}", c))
        self._show_graph_tabs(tabs)

    def _error_calculation(self, exception: Exception):
        self._loading_movie.stop()
        self._loading_label.hide()

        dialogs.show_error_dialog(self, exception)
        self._on_back()

    def _plot_group_routes(self, result: Result):
        canvases = []
        graphs_list = []
        for group_num, list_of_address_in_short_path in enumerate(result.list_of_address_in_short_path):
            sc = MplCanvas(self, width=5, height=4, dpi=100)
            G = plot_group_route(group_num, list_of_address_in_short_path, sc.axes)
            canvases.append(sc)
            graphs_list.append(G)

        return graphs_list, canvases

    def _plot_combined_route(self, result: Result, graphs_list):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        plot_combined_route(result, graphs_list, sc.axes)
        return sc

    def _plot_group_scatter(self, result: Result):
        # https://www.learnpyqt.com/tutorials/plotting-matplotlib/
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        plot_group_scatter(result, sc.axes)
        return sc

    def _show_graph_tabs(self, graphs):
        tab_root = QTabWidget()

        # https://pythonspot.com/pyqt5-tabs/
        for name, graph in graphs:
            tab_root.addTab(graph, name)

        layout = QHBoxLayout()
        layout.addWidget(tab_root)
        switch_layout(self._center_bar, layout)
