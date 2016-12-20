from PyQt5.QtWidgets import QApplication

from .ui import MainWindow


class Application(QApplication):

    def __init__(self, args):
        super().__init__(args)

        self.mw = MainWindow()
