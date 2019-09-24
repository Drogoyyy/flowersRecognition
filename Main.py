import sys
from PyQt5.QtWidgets import QApplication, QListWidgetItem
from PyQt5 import QtWidgets
from view.MainWindow import MainWindow
from EvalManager import EvalManager


class Main(object):

    def __init__(self):
        self.mainWindow = MainWindow()
        self.evalManager = EvalManager()
        self.mainWindow.batchDetectButton.clicked.connect(
            lambda: self.detect(0))
        self.mainWindow.detectButton.clicked.connect(lambda: self.detect(1))

    def show(self):
        # Window running
        self.mainWindow.show()

    def detect(self, type):
        self.evalManager.init()
        if type == 0:
            result = self.evalManager.predict_batch()
        else:
            result = self.evalManager.predict_single(self.mainWindow.image_path)
        for i in result:
            self.mainWindow.show_message(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
