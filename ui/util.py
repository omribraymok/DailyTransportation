from PyQt5.QtCore import QObjectCleanupHandler


def switch_layout(target_frame, new_layout):
    current_layout = target_frame.layout()
    if current_layout is not None:
        for i in reversed(range(current_layout.count())):
            current_layout.itemAt(i).widget().setParent(None)

    QObjectCleanupHandler().add(target_frame.layout())
    target_frame.setLayout(new_layout)
