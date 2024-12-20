from PySide2.QtWidgets import QApplication

from gui.main_window import MainWindow


def run_app():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    run_app()
