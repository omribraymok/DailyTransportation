from pathlib import Path
from typing import Callable

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel, QFileDialog, QHBoxLayout, QPushButton, QVBoxLayout

from consts import DEFAULT_K_COUNT
from ui import dialogs
from ui.calculation import Params


class StartWindow(QFrame):

    def __init__(self, next_window: Callable[[Params], None]):
        super().__init__()

        self._next_window = next_window

        browse_bar = self._create_file_select()
        transports_bar = self._create_count_select()

        self._calculate_button = QPushButton('Calculate')
        self._calculate_button.setFixedSize(QSize(200, 50))
        self._calculate_button.setDisabled(True)
        self._calculate_button.clicked.connect(self._start_calculate)

        layout = QVBoxLayout()
        layout.addWidget(browse_bar)
        layout.addWidget(transports_bar)

        form_frame = QFrame()
        form_frame.setLayout(layout)

        root_layout = QVBoxLayout()
        root_layout.addWidget(form_frame, alignment=Qt.AlignCenter)
        root_layout.addWidget(self._calculate_button, alignment=Qt.AlignCenter)
        self.setLayout(root_layout)

    def _create_file_select(self):
        layout = QHBoxLayout()
        layout.setSpacing(0)
        self._file_field = QLineEdit()
        self._file_field.setFixedSize(QSize(300, 30))
        self._file_field.setDisabled(True)
        layout.addWidget(self._file_field)
        button = QPushButton('Browse')
        button.setFixedSize(QSize(120, 30))
        button.clicked.connect(self._select_file)
        layout.addWidget(button)

        frame = QFrame()
        frame.setLayout(layout)
        return frame

    def _create_count_select(self):
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(QLabel('Transports Count'))
        self._k_count_field = QLineEdit()
        self._k_count_field.setFixedSize(QSize(100, 25))
        self._k_count_field.setValidator(QIntValidator(1, 200))
        self._k_count_field.setText(str(DEFAULT_K_COUNT))
        layout.addWidget(self._k_count_field)

        frame = QFrame()
        frame.setLayout(layout)
        return frame

    def _select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Data File", "",
                                                  "Excel Files (*.xlsx)", options=options)
        if not filename:
            return

        self._file_field.setText(filename)
        self._calculate_button.setDisabled(False)

    def _start_calculate(self):
        file = Path(self._file_field.text())

        count_text = self._k_count_field.text()
        if count_text == '':
            dialogs.show_error_dialog(self, ValueError("Missing Transportation count"))
            return

        count = int(count_text)

        if count < 0 or count > 20:
            dialogs.show_error_dialog(self, ValueError(f"Invalid Transportation count {count}"))
            return

        self._next_window(Params(file, count))

