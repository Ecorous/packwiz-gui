from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSize

import sys
import logger

source = "packwiz-gui.main"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PackwizGUI | Made by Ecorous, powered by Pyckwiz")
        self.resize(QSize(800,600))

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)
    
    #def contextMenuEvent(self, e):
    #    context = QMenu(self)
    #    context.addAction(QAction("test 1", self))
    #    context.addAction(QAction("test 2", self))
    #    context.addAction(QAction("test 3", self))
    #    context.exec(e.globalPos())




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



logger.info("Exiting Packwiz-GUI", source)
logger.exit()
# Return the final return code which is then handled by the bottom of the file
