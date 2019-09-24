# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(400, 10, 211, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.controlTab = QtWidgets.QWidget()
        self.controlTab.setObjectName("controlTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.controlTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.detectButton = QtWidgets.QPushButton(self.controlTab)
        self.detectButton.setObjectName("detectButton")
        self.verticalLayout_3.addWidget(self.detectButton)
        self.resultView = QtWidgets.QTextBrowser(self.controlTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultView.sizePolicy().hasHeightForWidth())
        self.resultView.setSizePolicy(sizePolicy)
        self.resultView.setObjectName("resultView")
        self.verticalLayout_3.addWidget(self.resultView)
        self.resultView.raise_()
        self.detectButton.raise_()
        self.tabWidget.addTab(self.controlTab, "")
        self.ImageTab = QtWidgets.QWidget()
        self.ImageTab.setObjectName("ImageTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ImageTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.imageList = QtWidgets.QListWidget(self.ImageTab)
        self.imageList.setObjectName("imageList")
        self.verticalLayout_6.addWidget(self.imageList)
        self.correctImageButtonLayout = QtWidgets.QHBoxLayout()
        self.correctImageButtonLayout.setObjectName("correctImageButtonLayout")
        self.importButton = QtWidgets.QPushButton(self.ImageTab)
        self.importButton.setEnabled(True)
        self.importButton.setObjectName("importButton")
        self.correctImageButtonLayout.addWidget(self.importButton)
        self.cleanListButton = QtWidgets.QPushButton(self.ImageTab)
        self.cleanListButton.setEnabled(True)
        self.cleanListButton.setObjectName("cleanListButton")
        self.correctImageButtonLayout.addWidget(self.cleanListButton)
        self.verticalLayout_6.addLayout(self.correctImageButtonLayout)
        self.batchDetectButton = QtWidgets.QPushButton(self.ImageTab)
        self.batchDetectButton.setObjectName("batchDetectButton")
        self.verticalLayout_6.addWidget(self.batchDetectButton)
        self.removeImageButton = QtWidgets.QPushButton(self.ImageTab)
        self.removeImageButton.setEnabled(False)
        self.removeImageButton.setObjectName("removeImageButton")
        self.verticalLayout_6.addWidget(self.removeImageButton)
        self.tabWidget.addTab(self.ImageTab, "")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 381, 371))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName("graphicsView")
        self.closeButton = QtWidgets.QPushButton(self.graphicsView)
        self.closeButton.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.closeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"黑体\";\n"
"background-color: red;\n"
"")
        self.closeButton.setObjectName("closeButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.detectButton.setText(_translate("MainWindow", "开始检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.controlTab), _translate("MainWindow", "控制"))
        self.importButton.setText(_translate("MainWindow", "导入"))
        self.cleanListButton.setText(_translate("MainWindow", "清空"))
        self.batchDetectButton.setText(_translate("MainWindow", "批量检测"))
        self.removeImageButton.setText(_translate("MainWindow", "删除图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImageTab), _translate("MainWindow", "图片"))
        self.closeButton.setText(_translate("MainWindow", "关闭"))

