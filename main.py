# Form implementation generated from reading ui file 'pycalc.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PyCalc(object):
    def setupUi(self, PyCalc):
        PyCalc.setObjectName("PyCalc")
        PyCalc.resize(338, 520)
        self.StyleSheet = QtWidgets.QWidget(PyCalc)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.StyleSheet.setFont(font)
        self.StyleSheet.setStyleSheet("QWidget{\n"
"    color: rgb(221, 221, 221);\n"
"    font: 36pt Courier;\n"
"}\n"
"#bgFrame {    \n"
"    \n"
"    background-color: rgb(51, 57, 68);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-radius: 10px;\n"
"}\n"
"#buttonsFrame {\n"
"    border-top-left-radius: 25px;\n"
"    border-top-right-radius: 25px;\n"
"    background-color: rgb(40, 44, 52);\n"
"    border: 1px solid black;\n"
"}\n"
"#buttonsFrame .QPushButton {\n"
"    background-color: rgb(40, 44, 52);\n"
"}")
        self.StyleSheet.setObjectName("StyleSheet")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.StyleSheet)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bgFrame = QtWidgets.QFrame(self.StyleSheet)
        self.bgFrame.setStyleSheet("")
        self.bgFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bgFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bgFrame.setObjectName("bgFrame")
        self.outputLabel = QtWidgets.QLabel(self.bgFrame)
        self.outputLabel.setGeometry(QtCore.QRect(0, 0, 320, 110))
        self.outputLabel.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.outputLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.outputLabel.setMargin(10)
        self.outputLabel.setObjectName("outputLabel")
        self.buttonsFrame = QtWidgets.QFrame(self.bgFrame)
        self.buttonsFrame.setGeometry(QtCore.QRect(0, 100, 320, 400))
        self.buttonsFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buttonsFrame.setObjectName("buttonsFrame")
        self.actionC = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionC.setGeometry(QtCore.QRect(36, 42, 45, 45))
        self.actionC.setStyleSheet("\n"
"background-color: #FF605C")
        self.actionC.setObjectName("actionC")
        self.actionSlash = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionSlash.setGeometry(QtCore.QRect(106, 42, 45, 45))
        self.actionSlash.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionSlash.setObjectName("actionSlash")
        self.actionMult = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionMult.setGeometry(QtCore.QRect(173, 42, 45, 45))
        self.actionMult.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionMult.setObjectName("actionMult")
        self.actionBackslash = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionBackslash.setGeometry(QtCore.QRect(242, 42, 45, 45))
        self.actionBackslash.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionBackslash.setObjectName("actionBackslash")
        self.actionMinus = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionMinus.setGeometry(QtCore.QRect(242, 112, 45, 45))
        self.actionMinus.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionMinus.setObjectName("actionMinus")
        self.num7 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num7.setGeometry(QtCore.QRect(36, 112, 45, 45))
        self.num7.setObjectName("num7")
        self.num8 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num8.setGeometry(QtCore.QRect(106, 112, 45, 45))
        self.num8.setObjectName("num8")
        self.num9 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num9.setGeometry(QtCore.QRect(173, 112, 45, 45))
        self.num9.setObjectName("num9")
        self.num5 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num5.setGeometry(QtCore.QRect(106, 180, 45, 45))
        self.num5.setObjectName("num5")
        self.actionSum = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionSum.setGeometry(QtCore.QRect(242, 180, 45, 45))
        self.actionSum.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionSum.setObjectName("actionSum")
        self.num6 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num6.setGeometry(QtCore.QRect(173, 180, 45, 45))
        self.num6.setObjectName("num6")
        self.num4 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num4.setGeometry(QtCore.QRect(36, 180, 45, 45))
        self.num4.setObjectName("num4")
        self.num1 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num1.setGeometry(QtCore.QRect(36, 248, 45, 45))
        self.num1.setObjectName("num1")
        self.num3 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num3.setGeometry(QtCore.QRect(173, 248, 45, 45))
        self.num3.setObjectName("num3")
        self.num2 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num2.setGeometry(QtCore.QRect(106, 248, 45, 45))
        self.num2.setObjectName("num2")
        self.actionEqual = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionEqual.setGeometry(QtCore.QRect(242, 248, 45, 114))
        self.actionEqual.setStyleSheet("background-color: rgb(21, 168, 133);")
        self.actionEqual.setObjectName("actionEqual")
        self.actionPercent = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionPercent.setGeometry(QtCore.QRect(36, 317, 45, 45))
        self.actionPercent.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionPercent.setObjectName("actionPercent")
        self.actionDot = QtWidgets.QPushButton(self.buttonsFrame)
        self.actionDot.setGeometry(QtCore.QRect(173, 317, 45, 45))
        self.actionDot.setStyleSheet("background-color: rgb(51, 57, 68);")
        self.actionDot.setObjectName("actionDot")
        self.num0 = QtWidgets.QPushButton(self.buttonsFrame)
        self.num0.setGeometry(QtCore.QRect(106, 317, 45, 45))
        self.num0.setObjectName("num0")
        self.closeButton = QtWidgets.QPushButton(self.bgFrame)
        self.closeButton.setGeometry(QtCore.QRect(10, 10, 21, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 96, 92))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.closeButton.setPalette(palette)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: rgb(255, 96, 92);\n"
"border: 1px solid transparent;\n"
"border-radius: 10px;\n"
"font:10px bold aria;")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.bgFrame)
        PyCalc.setCentralWidget(self.StyleSheet)

        self.retranslateUi(PyCalc)
        QtCore.QMetaObject.connectSlotsByName(PyCalc)

    def retranslateUi(self, PyCalc):
        _translate = QtCore.QCoreApplication.translate
        PyCalc.setWindowTitle(_translate("PyCalc", "MainWindow"))
        self.outputLabel.setText(_translate("PyCalc", "0"))
        self.actionC.setText(_translate("PyCalc", "C"))
        self.actionSlash.setText(_translate("PyCalc", "/"))
        self.actionMult.setText(_translate("PyCalc", "*"))
        self.actionBackslash.setText(_translate("PyCalc", "←"))
        self.actionMinus.setText(_translate("PyCalc", "-"))
        self.num7.setText(_translate("PyCalc", "7"))
        self.num8.setText(_translate("PyCalc", "8"))
        self.num9.setText(_translate("PyCalc", "9"))
        self.num5.setText(_translate("PyCalc", "5"))
        self.actionSum.setText(_translate("PyCalc", "+"))
        self.num6.setText(_translate("PyCalc", "6"))
        self.num4.setText(_translate("PyCalc", "4"))
        self.num1.setText(_translate("PyCalc", "1"))
        self.num3.setText(_translate("PyCalc", "3"))
        self.num2.setText(_translate("PyCalc", "2"))
        self.actionEqual.setText(_translate("PyCalc", "="))
        self.actionPercent.setText(_translate("PyCalc", "%"))
        self.actionDot.setText(_translate("PyCalc", "."))
        self.num0.setText(_translate("PyCalc", "0"))
        self.closeButton.setText(_translate("PyCalc", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyCalc = QtWidgets.QMainWindow()
    ui = Ui_PyCalc()
    ui.setupUi(PyCalc)
    PyCalc.show()
    sys.exit(app.exec())
