# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 675)
        MainWindow.setMinimumSize(QtCore.QSize(452, 675))
        MainWindow.setMaximumSize(QtCore.QSize(452, 675))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/die_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.diceCount = QtWidgets.QSpinBox(self.centralwidget)
        self.diceCount.setGeometry(QtCore.QRect(60, 430, 42, 22))
        self.diceCount.setAlignment(QtCore.Qt.AlignCenter)
        self.diceCount.setMinimum(1)
        self.diceCount.setMaximum(9)
        self.diceCount.setObjectName("diceCount")
        self.diceDM = QtWidgets.QSpinBox(self.centralwidget)
        self.diceDM.setGeometry(QtCore.QRect(240, 430, 42, 22))
        self.diceDM.setAlignment(QtCore.Qt.AlignCenter)
        self.diceDM.setMinimum(-9)
        self.diceDM.setMaximum(9)
        self.diceDM.setObjectName("diceDM")
        self.diceType = QtWidgets.QComboBox(self.centralwidget)
        self.diceType.setGeometry(QtCore.QRect(140, 430, 51, 22))
        self.diceType.setMaxVisibleItems(9)
        self.diceType.setMaxCount(9)
        self.diceType.setObjectName("diceType")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 430, 16, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 430, 16, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.diceRoll = QtWidgets.QLabel(self.centralwidget)
        self.diceRoll.setGeometry(QtCore.QRect(330, 420, 46, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.diceRoll.setFont(font)
        self.diceRoll.setFrameShape(QtWidgets.QFrame.Box)
        self.diceRoll.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.diceRoll.setText("")
        self.diceRoll.setAlignment(QtCore.Qt.AlignCenter)
        self.diceRoll.setObjectName("diceRoll")
        self.countLabel = QtWidgets.QLabel(self.centralwidget)
        self.countLabel.setGeometry(QtCore.QRect(60, 400, 46, 13))
        self.countLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countLabel.setObjectName("countLabel")
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(140, 400, 46, 13))
        self.typeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typeLabel.setObjectName("typeLabel")
        self.dmLabel = QtWidgets.QLabel(self.centralwidget)
        self.dmLabel.setGeometry(QtCore.QRect(240, 400, 46, 13))
        self.dmLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dmLabel.setObjectName("dmLabel")
        self.rollLabel = QtWidgets.QLabel(self.centralwidget)
        self.rollLabel.setGeometry(QtCore.QRect(330, 400, 46, 13))
        self.rollLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rollLabel.setObjectName("rollLabel")
        self.rollButton = QtWidgets.QPushButton(self.centralwidget)
        self.rollButton.setGeometry(QtCore.QRect(60, 490, 75, 23))
        self.rollButton.setObjectName("rollButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(220, 490, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(300, 490, 71, 23))
        self.quitButton.setObjectName("quitButton")
        self.rollBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.rollBrowser.setGeometry(QtCore.QRect(140, 540, 131, 71))
        self.rollBrowser.setObjectName("rollBrowser")
        self.rollInput = QtWidgets.QLineEdit(self.centralwidget)
        self.rollInput.setGeometry(QtCore.QRect(60, 590, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rollInput.setFont(font)
        self.rollInput.setObjectName("rollInput")
        self.diceinputLabel = QtWidgets.QLabel(self.centralwidget)
        self.diceinputLabel.setGeometry(QtCore.QRect(60, 570, 61, 20))
        self.diceinputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.diceinputLabel.setObjectName("diceinputLabel")
        self.mpl = MplWidget(self.centralwidget)
        self.mpl.setGeometry(QtCore.QRect(10, 10, 431, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Optima")
        font.setBold(True)
        font.setWeight(75)
        self.mpl.setFont(font)
        self.mpl.setObjectName("mpl")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 350, 171, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/shonner_brand.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.clear_graphButton = QtWidgets.QPushButton(self.centralwidget)
        self.clear_graphButton.setGeometry(QtCore.QRect(140, 490, 75, 23))
        self.clear_graphButton.setObjectName("clear_graphButton")
        self.voiceLabel = QtWidgets.QLabel(self.centralwidget)
        self.voiceLabel.setGeometry(QtCore.QRect(300, 540, 71, 20))
        self.voiceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.voiceLabel.setObjectName("voiceLabel")
        self.voiceBox = QtWidgets.QComboBox(self.centralwidget)
        self.voiceBox.setGeometry(QtCore.QRect(300, 560, 71, 22))
        self.voiceBox.setMaxVisibleItems(5)
        self.voiceBox.setObjectName("voiceBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRoll_Dice = QtWidgets.QAction(MainWindow)
        self.actionRoll_Dice.setIcon(icon)
        self.actionRoll_Dice.setObjectName("actionRoll_Dice")
        self.actionClear_All = QtWidgets.QAction(MainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_Graphical_Dice_Roll = QtWidgets.QAction(MainWindow)
        self.actionAbout_Graphical_Dice_Roll.setObjectName("actionAbout_Graphical_Dice_Roll")
        self.actionGraph = QtWidgets.QAction(MainWindow)
        self.actionGraph.setObjectName("actionGraph")
        self.actionClear_Graph = QtWidgets.QAction(MainWindow)
        self.actionClear_Graph.setObjectName("actionClear_Graph")
        self.menuMenu.addAction(self.actionRoll_Dice)
        self.menuMenu.addAction(self.actionClear_Graph)
        self.menuMenu.addAction(self.actionClear_All)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_Graphical_Dice_Roll)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.diceCount, self.diceType)
        MainWindow.setTabOrder(self.diceType, self.diceDM)
        MainWindow.setTabOrder(self.diceDM, self.rollButton)
        MainWindow.setTabOrder(self.rollButton, self.clear_graphButton)
        MainWindow.setTabOrder(self.clear_graphButton, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.quitButton)
        MainWindow.setTabOrder(self.quitButton, self.rollInput)
        MainWindow.setTabOrder(self.rollInput, self.rollBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graphical Dice Roll 0.2.0 (Beta)"))
        self.diceCount.setToolTip(_translate("MainWindow", "Dice count"))
        self.diceDM.setToolTip(_translate("MainWindow", "Dice modifier"))
        self.diceType.setToolTip(_translate("MainWindow", "Dice type"))
        self.label.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "="))
        self.diceRoll.setToolTip(_translate("MainWindow", "Roll result"))
        self.countLabel.setText(_translate("MainWindow", "Count"))
        self.typeLabel.setText(_translate("MainWindow", "Type"))
        self.dmLabel.setText(_translate("MainWindow", "Modifier"))
        self.rollLabel.setText(_translate("MainWindow", "Roll"))
        self.rollButton.setToolTip(_translate("MainWindow", "Roll the dice"))
        self.rollButton.setText(_translate("MainWindow", "Roll Dice"))
        self.clearButton.setToolTip(_translate("MainWindow", "Clear all fields"))
        self.clearButton.setText(_translate("MainWindow", "Clear All"))
        self.quitButton.setToolTip(_translate("MainWindow", "Quit this program"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.rollBrowser.setToolTip(_translate("MainWindow", "Roll History"))
        self.rollInput.setToolTip(_translate("MainWindow", "Enter a Roll"))
        self.diceinputLabel.setText(_translate("MainWindow", "Dice Input"))
        self.mpl.setToolTip(_translate("MainWindow", "Roll Graph"))
        self.clear_graphButton.setToolTip(_translate("MainWindow", "Clear graph"))
        self.clear_graphButton.setText(_translate("MainWindow", "Clear Graph"))
        self.voiceLabel.setText(_translate("MainWindow", "Voice Used"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionRoll_Dice.setText(_translate("MainWindow", "Roll Dice"))
        self.actionRoll_Dice.setStatusTip(_translate("MainWindow", "Roll the dice"))
        self.actionClear_All.setText(_translate("MainWindow", "Clear All"))
        self.actionClear_All.setStatusTip(_translate("MainWindow", "Clear all fields"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit this program"))
        self.actionAbout_Graphical_Dice_Roll.setText(_translate("MainWindow", "About Graphical Dice Roll"))
        self.actionAbout_Graphical_Dice_Roll.setStatusTip(_translate("MainWindow", "About Graphical Dice Roll"))
        self.actionGraph.setText(_translate("MainWindow", "Graph"))
        self.actionGraph.setStatusTip(_translate("MainWindow", "Display a graph"))
        self.actionClear_Graph.setText(_translate("MainWindow", "Clear Graph"))
        self.actionClear_Graph.setStatusTip(_translate("MainWindow", "Clear the graph"))
from mplwidget import MplWidget
import resources_rc
