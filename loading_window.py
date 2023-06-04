from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QMovie

# TODO


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie = QMovie('Loading_2.gif')
        self.label_animation.setMovie(self.movie)

    def startAnimation(self):
        self.movie.start()
        self.show()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


'''
from PyQt5.QtWidgets import QApplication
import sys
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.ls = LoadingScreen()
        self.ls.startAnimation()
        import time
        # time.sleep(3)
        # self.ls.stopAnimation()
        # self.show()


app = QApplication(sys.argv)
demo = AppDemo()
app.exit(app.exec())
'''
