from PyQt5.QtWidgets import QMainWindow

from main_gui import Ui_MainWindow

class Window(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__(None)

        self.setupUi(self)