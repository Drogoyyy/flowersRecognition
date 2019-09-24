import sys
import os
import cv2
import shutil
from PyQt5.QtGui import QImage, QPixmap
from threading import Thread, Semaphore
from ui.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QGraphicsPixmapItem, QGraphicsScene
from PyQt5 import QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):

    PREDICT_PATH = "predict_images/"
    # 设置计数器的值为 10
    sem = Semaphore(10)
    cwd = None
    image_list = []
    image_path = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 图像显示区相关初始化
        self._scene = QGraphicsScene()  # 创建场景,用于显示图片
        self.graphicsView.setScene(self._scene)  # 将场景添加至视图
        self.currentImage = None
        self.zoom_scale = 1  # 图像的缩放比例
        self.imageGraphicItem = QGraphicsPixmapItem()  # 用于在scene中显示Image
        self.imageGraphicItem.setZValue(0)  # 设置显示在0层
        self._scene.addItem(self.imageGraphicItem)
        # 图片列表相关操作
        self.importButton.clicked.connect(self._import_image)
        self._init_image_list()
        self.imageList.itemDoubleClicked.connect(self._image_select)
        # 关闭按钮位置设置
        self.closeButton.move(self.graphicsView.width() / 2, 10)
        self.closeButton.setVisible(False)
        self.closeButton.clicked.connect(self._close_image)
        self.removeImageButton.clicked.connect(self._delete_image)
        self.cleanListButton.clicked.connect(self._clear_image_list)

    def _init_image_list(self):
        for file_name in os.listdir(self.PREDICT_PATH):
            if file_name.endswith('.jpg'):
                image = cv2.imread(self.PREDICT_PATH + file_name)
                self.image_list.append([file_name, image])
                self.add_image_item(file_name, image)

    def add_image_item(self, file_name, image):
        item = QListWidgetItem()
        item.setText(file_name)
        item.image = image
        self.imageList.addItem(item)

    def show_message(self, msg):
        QApplication.processEvents()
        self.resultView.append(msg)
        self.resultView.moveCursor(
            self.resultView.textCursor().End)

    def _image_select(self, selected_item):
        self.selectedImageItem = selected_item
        self.image_path = self.PREDICT_PATH + selected_item.text()
        self.closeButton.setVisible(True)
        self.closeButton.setEnabled(True)
        self.removeImageButton.setEnabled(True)
        self.show_image(selected_item.image)

    def show_image(self, image):
        self.imageGraphicItem.setVisible(True)
        # 关闭键按钮在视图界面居中,注：46是button长度的一半
        self.closeButton.move((self.graphicsView.width() / 2) - 46, 10)
        self.currentImage = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换图像通道
        image_width = image.shape[1]  # 获取图像大小
        image_height = image.shape[0]
        frame = QImage(image, image_width, image_height, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.imageGraphicItem.setPixmap(pix)
        # 根据graphicsView的大小，调整图片的比例
        scale_x = self.graphicsView.width() / image_width
        scale_y = self.graphicsView.height() / image_height
        if scale_x < scale_y:
            self.zoom_scale = scale_x
        else:
            self.zoom_scale = scale_y
        self.imageGraphicItem.setScale(self.zoom_scale)

    def _import_image(self):
        files, file_type = QtWidgets.QFileDialog.getOpenFileNames(self,
                                                                  '图片选择',
                                                                  self.cwd,  # 起始路径
                                                                  'All Files (*);;Image Files (*.jpg)')
        for file in files:
            # 获取一个 semaphore
            self.sem.acquire()
            import_thread = Thread(
                target=self._copy_image, args=(file, self.PREDICT_PATH))
            import_thread.start()

        QApplication.processEvents()

    def _copy_image(self, source_file, target_folder):
        shutil.copy(source_file, target_folder)
        file_name = os.path.basename(source_file)
        if file_name not in self.image_list:
            self.image_list.append(file_name)
            image = cv2.imread(self.PREDICT_PATH + file_name)
            self.add_image_item(file_name, image)

    # 关闭标准图片，并完成相应的UI界面变化
    def _close_image(self):
        self.imageGraphicItem.setVisible(False)
        self.selectedImageItem = None
        self.removeImageButton.setEnabled(False)
        self.closeButton.setEnabled(False)
        self.closeButton.setVisible(False)

    def _delete_image(self):
        self.remove(self.selectedImageItem.text())
        self._remove_image_item()
    
    def _clear_image_list(self):
        shutil.rmtree(self.PREDICT_PATH)
        os.mkdir(self.PREDICT_PATH)
        self.image_list.clear()
        self.imageList.clear()

    def _remove_image_item(self):
        row = self.imageList.row(self.selectedImageItem.image)
        self.imageList.takeItem(row)
        self._close_image()

    def remove(self, file_name):
        for image in self.image_list:
            if image[0] == file_name:
                self.image_list.remove(image)
                break
        os.remove(self.PREDICT_PATH + file_name)
