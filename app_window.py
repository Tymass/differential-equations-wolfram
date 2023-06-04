from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from web_backend import Calculator
import matplotlib.image as mpimg
from loading_window import LoadingScreen
import sys


class Application(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        self.input_field = QLineEdit(self)
        self.button = QPushButton('Calculate', self)
        self.label = QLabel(self)
        self.textedit = QTextEdit(self)
        self.loading_screen = LoadingScreen()
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)

        self.plot1_label = QLabel(self)
        self.plot1_label.setText('Slope field')
        self.plot2_label = QLabel(self)
        self.plot2_label.setText('Plots of sample individual solution')
        self.plot3_label = QLabel(self)
        self.plot3_label.setText('Sample solution family')

        # Connect button to calculate method
        # self.button.clicked.connect(self.loading_screen.startAnimation)
        self.button.clicked.connect(self.calculate)

        # Create layout and add UI elements
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.textedit)

        labels_layout = QHBoxLayout()
        labels_layout.addWidget(self.plot1_label)
        labels_layout.addWidget(self.plot2_label)
        labels_layout.addWidget(self.plot3_label)
        layout.addLayout(labels_layout)

        plots_layout = QHBoxLayout()
        plots_layout.addWidget(self.canvas1)
        plots_layout.addWidget(self.canvas2)
        plots_layout.addWidget(self.canvas3)
        layout.addLayout(plots_layout)

        self.setLayout(layout)

    def calculate(self):

        input_text = self.input_field.text()
        input_text = 'diff equation ' + input_text
        self.calculator = Calculator(input_text)
        self.output_text, self.plot_error = self.calculator.calculate()
        self.textedit.setText(
            f"Solution: {self.output_text}")

        try:
            if self.plot_error == 1:
                img1 = mpimg.imread('blank')
                ax1 = self.figure1.add_subplot(111)
                ax1.set_axis_off()
                ax1.imshow(img1)
                self.canvas1.draw()
            else:
                img1 = mpimg.imread('plot1')
                ax1 = self.figure1.add_subplot(111)
                ax1.set_axis_off()
                ax1.imshow(img1)
                self.canvas1.draw()
        except:
            print('There is no plot 1')

        try:
            if self.plot_error == 2:
                img2 = mpimg.imread('blank')
                ax2 = self.figure2.add_subplot(111)
                ax2.set_axis_off()
                ax2.imshow(img2)
                self.canvas2.draw()
            else:
                img2 = mpimg.imread('plot2')
                ax2 = self.figure2.add_subplot(111)
                ax2.set_axis_off()
                ax2.imshow(img2)
                self.canvas2.draw()
        except:
            print("There is no plot 2")

        try:
            if self.plot_error == 3:
                img3 = mpimg.imread('blank')
                ax3 = self.figure3.add_subplot(111)
                ax3.set_axis_off()
                ax3.imshow(img3)
                self.canvas3.draw()
            else:
                img3 = mpimg.imread('plot3')
                ax3 = self.figure3.add_subplot(111)
                ax3.set_axis_off()
                ax3.imshow(img3)
                self.canvas3.draw()
        except:
            print("There is no plot 3")

        pixmap = QPixmap('solution_img.png')
        self.label.setPixmap(pixmap)


app = QApplication(sys.argv)

window = Application()
window.show()

sys.exit(app.exec_())
