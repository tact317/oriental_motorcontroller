# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 130, 30, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 91, 21))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.label_8.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 120, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 80, 30, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 60, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 30, 70, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 91, 20))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 160, 41, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 120, 15))
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.start = QtWidgets.QPushButton(self.tab)
        self.start.setGeometry(QtCore.QRect(20, 30, 70, 23))
        self.start.setObjectName("start")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 110, 40, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.WindingImg_3 = QtWidgets.QLabel(self.tab)
        self.WindingImg_3.setGeometry(QtCore.QRect(200, 10, 281, 231))
        self.WindingImg_3.setText("")
        self.WindingImg_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.WindingImg_3.setPixmap(QtGui.QPixmap("img/push.png"))
        self.WindingImg_3.setAlignment(QtCore.Qt.AlignCenter)
        self.WindingImg_3.setObjectName("WindingImg_3")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(80, 110, 40, 20))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 80, 60, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 130, 30, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 110, 120, 15))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 80, 30, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.WindingImg = QtWidgets.QLabel(self.tab_2)
        self.WindingImg.setGeometry(QtCore.QRect(200, 60, 271, 150))
        self.WindingImg.setText("")
        self.WindingImg.setTextFormat(QtCore.Qt.MarkdownText)
        self.WindingImg.setPixmap(QtGui.QPixmap("img/rotate.png"))
        self.WindingImg.setObjectName("WindingImg")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 30, 70, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 70, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 120, 15))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 80, 61, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 130, 131, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(10, 170, 71, 21))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(0, 150, 120, 21))
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 150, 41, 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "OK"))
        self.label_8.setText(_translate("MainWindow", "押し込み"))
        self.label_9.setText(_translate("MainWindow", "アラームの状態"))
        self.pushButton_7.setText(_translate("MainWindow", "OK"))
        self.pushButton_8.setText(_translate("MainWindow", "停止"))
        self.label_10.setText(_translate("MainWindow", "押し幅の入力"))
        self.pushButton_9.setText(_translate("MainWindow", "解除"))
        self.label_11.setText(_translate("MainWindow", "周期/周期数の入力"))
        self.start.setText(_translate("MainWindow", "開始"))
        self.radioButton_2.setText(_translate("MainWindow", "Dx2"))
        self.radioButton.setText(_translate("MainWindow", "Dx1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "押し込み"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "初期角度の入力"))
        self.pushButton_4.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
        self.label_4.setText(_translate("MainWindow", "巻き取り"))
        self.pushButton.setText(_translate("MainWindow", "開始"))
        self.label_5.setText(_translate("MainWindow", "パルス数/回転数の入力"))
        self.label_13.setText(_translate("MainWindow", "アラームの状態"))
        self.pushButton_10.setText(_translate("MainWindow", "解除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "巻き取り"))
        self.menu.setTitle(_translate("MainWindow", "ファイル"))
        self.menu_2.setTitle(_translate("MainWindow", "設定"))
