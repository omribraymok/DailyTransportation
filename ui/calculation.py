from collections import namedtuple

from PyQt5.QtCore import pyqtSignal, QObject

from algorithm import load_data, calculate


Params = namedtuple('Params', 'data_file k_count')


class CalcTracker(QObject):
    finished = pyqtSignal(object)
    error = pyqtSignal(object)


def start_calculation(params: Params, tracker: CalcTracker):
    try:
        data = load_data(str(params.data_file))
        result = calculate(*data, params.k_count)
        tracker.finished.emit(result)
    except Exception as e:
        tracker.error.emit(e)
