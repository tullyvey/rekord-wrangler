
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout, QSplitter, QWidget, QLabel,
        QTableWidget, QTableWidgetItem,
        QTreeWidget, QTreeWidgetItem)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exit_action)
        helpMenu = menubar.addMenu('&Help')

        self.mainwidget = _MainWidget()
        self.setCentralWidget(self.mainwidget)

        self.setWindowTitle("Rekord Wrangler")

        self.statusBar().showMessage('Ready')

        self.show()


class _MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setwidget = QWidget()
        self.trackswidget = QWidget()

        vbox = QVBoxLayout()
        splitter = QSplitter(self)
        splitter.addWidget(self.setwidget)
        splitter.addWidget(self.trackswidget)
        vbox.addWidget(splitter)
        self.setLayout(vbox)
