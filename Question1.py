import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import*
from PySide6.QtGui import*

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing Github")

    def paintEvent(self, e):
        pass

class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Jeen")


    def paintEvent(self, e):
        p = QPainter(self)
        p.setBrush(QColor(0, 255, 0))
        p.drawEllipse(50, 50, 150, 150)
        p.end()


class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Kenji")


    def paintEvent(self, e):
        p = QPainter(self)
        p.setBrush(QColor(0, 255, 0))
        p.drawLine(50, 50, 150, 150)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window3()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()