# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titooVisu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hideCloudButton = QtWidgets.QToolButton(self.centralwidget)
        self.hideCloudButton.setObjectName("hideCloudButton")
        self.horizontalLayout_2.addWidget(self.hideCloudButton)
        self.openCloudButton = QtWidgets.QToolButton(self.centralwidget)
        self.openCloudButton.setObjectName("openCloudButton")
        self.horizontalLayout_2.addWidget(self.openCloudButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.posLabel = QtWidgets.QLabel(self.centralwidget)
        self.posLabel.setObjectName("posLabel")
        self.verticalLayout_2.addWidget(self.posLabel)
        self.lwcLabel = QtWidgets.QLabel(self.centralwidget)
        self.lwcLabel.setObjectName("lwcLabel")
        self.verticalLayout_2.addWidget(self.lwcLabel)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.zAutoCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.zAutoCheckbox.setObjectName("zAutoCheckbox")
        self.verticalLayout.addWidget(self.zAutoCheckbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.zSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.zSpinbox.setObjectName("zSpinbox")
        self.horizontalLayout.addWidget(self.zSpinbox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.zSlider = QtWidgets.QSlider(self.centralwidget)
        self.zSlider.setOrientation(QtCore.Qt.Vertical)
        self.zSlider.setObjectName("zSlider")
        self.verticalLayout.addWidget(self.zSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.zSlider.valueChanged['int'].connect(self.zSpinbox.setValue)
        self.zSpinbox.valueChanged['int'].connect(self.zSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Titoo Visu"))
        self.hideCloudButton.setText(_translate("MainWindow", "HIDE cloud"))
        self.openCloudButton.setText(_translate("MainWindow", "Open cloud"))
        self.posLabel.setText(_translate("MainWindow", "POS : X...."))
        self.lwcLabel.setText(_translate("MainWindow", "LWC: 00"))
        self.zAutoCheckbox.setText(_translate("MainWindow", "Z AUTO"))
        self.label.setText(_translate("MainWindow", "Z = "))

