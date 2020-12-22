import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import QtWidgets

class Widget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Git и желтые окружности')
        self.setGeometry(500, 500, 500, 500)
        self.pushButton = QPushButton('Нажать', self)
        self.pushButton.resize(100, 30)
        self.pushButton.move(200, 240)
        self.pushButton.clicked.connect(self.draw_circle)
        self.flag = False
        self.show()
    
    def draw_circle(self):
        self.flag = True
        if self.flag:
            self.repaint()
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()
    
    def drawFlag(self, qp):
        if self.flag:
            x, y, d = randint(0, self.width() - 10), randint(0, self.height() - 100), randint(0, self.width() // 2)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(x, y, d, d)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())