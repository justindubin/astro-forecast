
from PySide2 import QtWidgets, QtCore, QtGui

from src.configuration import load_env_vars, update_env_vars


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        load_env_vars()

        # Window title and geometry
        self.setWindowTitle("Astro Alert Service")
        self.setFixedSize(600, 400)

        # Create a QThreadPool for threading operations
        self.threadpool = QtCore.QThreadPool()

