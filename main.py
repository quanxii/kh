from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QLineEdit, QInputDialog, QFileDialog
import os
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap

class ImageEditor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filemane = None
        self.save_dir = 'Modified/'

    def loadimage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showimage(self, path):
        picture.hide()
        pixmapimage = QPixmap(path)
        w, h = picture.width(), picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmapimage)
        picture.show()
    
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def mirrorr(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage(image_path)

    def left_90(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage(image_path)

    def right_90(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showimage(image_path)
    
#    def sharpness_(self):
#        contrast = self.image.ImageEnhance.Contrast(self.image)
#        contrast = self.image.enhance(1.5)
#        self.saveImage()
#        image_path = os.path.join(self.dir, self.save_dir, self.filename)
#        self.showimage(image_path)

app = QApplication([])
window = QWidget()
window.resize(700, 500)
window.setWindowTitle('Easy Editor')

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()

folder = QPushButton('Папка')
left = QPushButton('Лево')
right = QPushButton('Право')
mirror = QPushButton('Отзеркалить')
sharpness = QPushButton('Резкость')
bw = QPushButton('Ч/Б')

lists = QListWidget()

picture = QLabel('Картинка')

v1.addWidget(folder)
v1.addWidget(lists)
v2.addWidget(picture)
h2.addWidget(left)
h2.addWidget(right)
h2.addWidget(mirror)
h2.addWidget(sharpness)
h2.addWidget(bw)
v2.addLayout(h1)
v2.addLayout(h2)
h3.addLayout(v1)
h3.addLayout(v2)
window.setLayout(h3)

workdir = ''

def filter(files, extensoins):
    result = []
    for filename in files:
        for ext in extensoins:
            if filename.endswith(ext):
                result.append(filename)
    return result


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensoins = ['.png', '.jpg', '.jpeg', '.gif']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensoins)
    lists.clear()
    for filename in filenames:
        lists.addItem(filename)

def showChosenImage():
    filename = lists.currentItem().text()
    workimage.loadimage(workdir, filename)
    image_path = os.path.join(workimage.dir, workimage.filename)
    workimage.showimage(image_path)

workimage = ImageEditor()

folder.clicked.connect(showFilenamesList)
lists.currentRowChanged.connect(showChosenImage)
bw.clicked.connect(workimage.do_bw)
mirror.clicked.connect(workimage.mirrorr)
left.clicked.connect(workimage.left_90)
right.clicked.connect(workimage.right_90)
#sharpness.clicked.connect(workimage.sharpness_)

window.show()
app.exec_()