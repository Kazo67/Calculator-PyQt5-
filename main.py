from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from helper import Helper
import sys
import os


# Main class application which inherits QMainWindow class
class ApplicationWindow(QMainWindow):
    # Initializing constructor
    def __init__(self):
        # Initializing constructor of inherited class
        # which is passed in the argument of the class
        super(ApplicationWindow, self).__init__()
        # super().__init__() is the same

        # object name, size of the window, background and window title
        self.setObjectName("Kalkulator")
        self.resize(318, 400)
        self.setStyleSheet("background-color: grey;")
        self.setWindowTitle("Kalkulator")
        self.setWindowIcon(QtGui.QIcon(os.path.join("Assets", "icon.png")))

        # Method show_ui
        self.show_ui()

    # Method which is showing UI and
    # at the end has mechanism method
    def show_ui(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 331, 98))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: black; color: white;")
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setMargin(15)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.to_the_power_of = QtWidgets.QPushButton(self.centralwidget)
        self.to_the_power_of.setGeometry(QtCore.QRect(0, 340, 78, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.to_the_power_of.setFont(font)
        self.to_the_power_of.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.to_the_power_of.setMouseTracking(False)
        self.to_the_power_of.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""\n""")
        self.to_the_power_of.setObjectName("to_the_power_of")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(80, 340, 78, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.zero.setFont(font)
        self.zero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero.setMouseTracking(False)
        self.zero.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.zero.setObjectName("zero")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(160, 340, 78, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divide.setFont(font)
        self.divide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.divide.setMouseTracking(False)
        self.divide.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.divide.setObjectName("divide")
        self.sum = QtWidgets.QPushButton(self.centralwidget)
        self.sum.setGeometry(QtCore.QRect(240, 340, 78, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sum.setFont(font)
        self.sum.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sum.setMouseTracking(False)
        self.sum.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.sum.setObjectName("sum")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 280, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.one.setFont(font)
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(80, 280, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.two.setFont(font)
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(160, 280, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.three.setFont(font)
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.three.setObjectName("three")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(240, 280, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus.setFont(font)
        self.plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.plus.setObjectName("plus")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 220, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.four.setFont(font)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(80, 220, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.five.setFont(font)
        self.five.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(160, 220, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.six.setFont(font)
        self.six.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.six.setObjectName("six")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(240, 220, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus.setFont(font)
        self.minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minus.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.minus.setObjectName("minus")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 160, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.seven.setFont(font)
        self.seven.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(80, 160, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eight.setFont(font)
        self.eight.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(160, 160, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nine.setFont(font)
        self.nine.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.nine.setObjectName("nine")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(240, 160, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.multiply.setFont(font)
        self.multiply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiply.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.multiply.setObjectName("multiply")
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(0, 100, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.point.setFont(font)
        self.point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.point.setMouseTracking(False)
        self.point.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.point.setObjectName("point")
        self.root = QtWidgets.QPushButton(self.centralwidget)
        self.root.setGeometry(QtCore.QRect(80, 100, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.root.setFont(font)
        self.root.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.root.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.root.setObjectName("root")
        self.deleteAll = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAll.setGeometry(QtCore.QRect(160, 100, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.deleteAll.setFont(font)
        self.deleteAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteAll.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.deleteAll.setObjectName("deleteAll")
        self.deleteOne = QtWidgets.QPushButton(self.centralwidget)
        self.deleteOne.setGeometry(QtCore.QRect(240, 100, 78, 58))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.deleteOne.setFont(font)
        self.deleteOne.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteOne.setStyleSheet("QPushButton{background-color: black;color: white;}\n""QPushButton:hover{background-color: #484544;}\n""")
        self.deleteOne.setObjectName("deleteOne")
        self.setCentralWidget(self.centralwidget)

        # method retranslate_ui
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)


        # Mechanism of the program
        self.mechanism()

    # Method which is changing names of buttons
    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Kalkulator", "Kalkulator"))
        self.label.setText(_translate("Kalkulator", ""))
        self.to_the_power_of.setText(_translate("Kalkulator", "x²"))
        self.zero.setText(_translate("Kalkulator", "0"))
        self.divide.setText(_translate("Kalkulator", "÷"))
        self.sum.setText(_translate("Kalkulator", "="))
        self.one.setText(_translate("Kalkulator", "1"))
        self.two.setText(_translate("Kalkulator", "2"))
        self.three.setText(_translate("Kalkulator", "3"))
        self.plus.setText(_translate("Kalkulator", "+"))
        self.four.setText(_translate("Kalkulator", "4"))
        self.five.setText(_translate("Kalkulator", "5"))
        self.six.setText(_translate("Kalkulator", "6"))
        self.minus.setText(_translate("Kalkulator", "-"))
        self.seven.setText(_translate("Kalkulator", "7"))
        self.eight.setText(_translate("Kalkulator", "8"))
        self.nine.setText(_translate("Kalkulator", "9"))
        self.multiply.setText(_translate("Kalkulator", "×"))
        self.point.setText(_translate("Kalkulator", "."))
        self.root.setText(_translate("Kalkulator", "√"))
        self.deleteAll.setText(_translate("Kalkulator", "C"))
        self.deleteOne.setText(_translate("Kalkulator", "⌫"))

    # Mechanism of the application used at the end of show_ui method
    def mechanism(self):
        # Helpful variables
        _translate = QtCore.QCoreApplication.translate
        _setLabelText = self.label.setText

        # region Clicking mechanism
        self.deleteAll.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(""))))
        self.deleteOne.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.delete_last_character_of_string(self.label.text()))))

        self.point.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "."))))

        self.zero.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "0"))))
        self.one.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "1"))))
        self.two.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "2"))))
        self.three.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "3"))))
        self.four.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "4"))))
        self.five.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "5"))))
        self.six.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "6"))))
        self.seven.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "7"))))
        self.eight.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "8"))))
        self.nine.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "9"))))

        self.plus.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "+"))))
        self.minus.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "-"))))
        self.multiply.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "*"))))
        self.divide.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "/"))))
        self.to_the_power_of.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "**2"))))
        self.root.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.return_result_of_extraction_of_the_root(self.label.text()))))

        self.sum.clicked.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.sum_the_value(self.label.text()))))
        # endregion Clicking mechanism

        # region Shortcuts
        self.shortcut0 = QShortcut(QKeySequence('0'), self)
        self.shortcut1 = QShortcut(QKeySequence('1'), self)
        self.shortcut2 = QShortcut(QKeySequence('2'), self)
        self.shortcut3 = QShortcut(QKeySequence('3'), self)
        self.shortcut4 = QShortcut(QKeySequence('4'), self)
        self.shortcut5 = QShortcut(QKeySequence('5'), self)
        self.shortcut6 = QShortcut(QKeySequence('6'), self)
        self.shortcut7 = QShortcut(QKeySequence('7'), self)
        self.shortcut8 = QShortcut(QKeySequence('8'), self)
        self.shortcut9 = QShortcut(QKeySequence('9'), self)

        self.shortcut0.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "0"))))
        self.shortcut1.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "1"))))
        self.shortcut2.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "2"))))
        self.shortcut3.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "3"))))
        self.shortcut4.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "4"))))
        self.shortcut5.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "5"))))
        self.shortcut6.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "6"))))
        self.shortcut7.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "7"))))
        self.shortcut8.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "8"))))
        self.shortcut9.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(self.label.text() + "9"))))


        self.shortcutDivide = QShortcut(QKeySequence('/'), self)
        self.shortcutPlus = QShortcut(QKeySequence('+'), self)
        self.shortcutSum = QShortcut(QKeySequence('='), self)
        self.shortcutEnter = QShortcut(QKeySequence('Return'), self)
        self.shortcutMinus = QShortcut(QKeySequence('-'), self)
        self.shortcutMultiply = QShortcut(QKeySequence('*'), self)
        self.shortcutPoint = QShortcut(QKeySequence('.'), self)
        self.shortcutBackspace = QShortcut(QKeySequence('Backspace'), self)
        self.shortcutDelete = QShortcut(QKeySequence('Del'), self)

        self.shortcutDivide.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "/"))))
        self.shortcutPlus.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "+"))))
        self.shortcutSum.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.sum_the_value(self.label.text()))))
        self.shortcutEnter.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.sum_the_value(self.label.text()))))
        self.shortcutMinus.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "-"))))
        self.shortcutMultiply.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "*"))))
        self.shortcutPoint.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.add_symbol_at_the_end_of_label(self.label.text(), "."))))
        self.shortcutBackspace.activated.connect(lambda: _setLabelText(_translate("Kalkulator", Helper.delete_last_character_of_string(self.label.text()))))
        self.shortcutDelete.activated.connect(lambda: _setLabelText(_translate("Kalkulator", str(""))))
        # endregion Shortcuts

        # Not necessary
        self.label.update()


# Main function
def application():
    # Creating instance of QApplication class
    # QApplication takes a list of string as input
    # So QApplication is also able to work with [] argument
    # app = QApplication([])
    app = QApplication(sys.argv)

    # Creating object of the main application class
    window = ApplicationWindow()

    # Shows the application window
    window.show()

    # exec_() call starts the event-loop
    # and will block until the application quits
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
