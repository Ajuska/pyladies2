# MATERIALY
# https://naucse.python.cz/2018/pyknihovny-jaro/intro/pyqt/

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

button = QtWidgets.QPushButton("Click to Exit")
button.setWindowTitle("Goodye World")

def print_line():
    print("klik!")

button.clicked.connect(print_line)
button.clicked.connect(app.quit)

button.show()
app.exec()
