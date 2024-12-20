import os

from PySide2 import QtWidgets, QtCore, QtGui

from api.fetch_data import fetch_data
from src.configuration import load_env_vars, update_env_vars
from src.messenger import Messenger


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        load_env_vars()

        # Window title and geometry
        self.setWindowTitle("Astro Alert Service")
        self.setFixedSize(600, 400)

        # Create a QThreadPool for threading operations
        self.threadpool = QtCore.QThreadPool()

        # Create a messenger to handle alerts
        self.messenger = Messenger()

        # Define basic layout
        self.root_window = QtWidgets.QWidget()
        self.base_layout = QtWidgets.QVBoxLayout()
        self.inputs_layout = QtWidgets.QVBoxLayout()
        self.inputs_layout.setSpacing(10)
        self.inputs_layout.setContentsMargins(5, 5, 5, 5)
        self.outputs_layout = QtWidgets.QVBoxLayout()
        self.outputs_layout.setContentsMargins(5, 5, 5, 5)
        self.base_layout.addLayout(self.inputs_layout)
        self.base_layout.addLayout(self.outputs_layout)
        self.root_window.setLayout(self.base_layout)
        self.setCentralWidget(self.root_window)

        # Add Widgets - Inputs - Location Form
        location_form = QtWidgets.QFormLayout()
        self.ent_lat = QtWidgets.QLineEdit(os.getenv('LATITUDE'))
        self.ent_lat.setFixedWidth(200)
        self.ent_lat.setReadOnly(True)
        self.ent_long = QtWidgets.QLineEdit(os.getenv('LONGITUDE'))
        self.ent_long.setFixedWidth(200)
        self.ent_long.setReadOnly(True)
        location_form.addRow(QtWidgets.QLabel("Latitude:"), self.ent_lat)
        location_form.addRow(QtWidgets.QLabel("Longitude:"), self.ent_long)
        location_form.setContentsMargins(0, 10, 0, 0)
        self.inputs_layout.addLayout(location_form)

        # Add Widgets - Inputs - Button Layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(0)
        self.inputs_layout.addLayout(button_layout)

        # Add Widgets - Inputs - Lock Button
        svg_size = 60
        self.icon_lock = QtGui.QIcon('./img/locked.svg')
        self.icon_unlock = QtGui.QIcon('./img/unlocked.svg')
        self.btn_lock = QtWidgets.QPushButton(icon=self.icon_lock)
        self.btn_lock.setIconSize(QtCore.QSize(svg_size, svg_size))
        self.btn_lock.setFixedSize(svg_size, svg_size)
        self.btn_lock.setFlat(True)
        button_layout.addWidget(self.btn_lock)

        # Add Widgets - Inputs - Apply Button
        self.btn_apply = QtWidgets.QPushButton(text='APPLY')
        self.btn_apply.setFixedSize(QtCore.QSize(200, 50))
        button_layout.addWidget(self.btn_apply)

        # Add Widgets - Outputs - Output Console
        self.output_console = QtWidgets.QTextEdit()
        self.output_console.setTextColor(QtGui.QColor('#68ff68'))
        self.output_console.setReadOnly(True)
        self.outputs_layout.setAlignment(QtCore.Qt.AlignCenter)
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedWidth(570)
        scroll_area.setFixedHeight(200)
        scroll_area.setWidget(self.output_console)
        self.outputs_layout.addWidget(scroll_area)

