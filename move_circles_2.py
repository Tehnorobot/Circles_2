import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import QtWidgets
from PyQt5 import uic

Form, Window = uic.loadUiType("Ui.ui")

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
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
    ex = Ui()
    sys.exit(app.exec_())