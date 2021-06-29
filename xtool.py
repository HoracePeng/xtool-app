# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/xtool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 322)
        MainWindow.setMinimumSize(QtCore.QSize(326, 322))
        MainWindow.setMaximumSize(QtCore.QSize(326, 322))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.phoneTable = QtWidgets.QTableWidget(self.centralwidget)
        self.phoneTable.setObjectName("phoneTable")
        self.phoneTable.setColumnCount(3)
        self.phoneTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.phoneTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.phoneTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.phoneTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.phoneTable)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importBtn = QtWidgets.QPushButton(self.widget)
        self.importBtn.setObjectName("importBtn")
        self.horizontalLayout.addWidget(self.importBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.delayTimeBox = QtWidgets.QSpinBox(self.widget)
        self.delayTimeBox.setProperty("value", 0)
        self.delayTimeBox.setObjectName("delayTimeBox")
        self.horizontalLayout.addWidget(self.delayTimeBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.playBtn = QtWidgets.QPushButton(self.widget)
        self.playBtn.setObjectName("playBtn")
        self.horizontalLayout.addWidget(self.playBtn)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.phoneTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.phoneTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "手机号"))
        item = self.phoneTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "状态"))
        self.importBtn.setText(_translate("MainWindow", "导入"))
        self.label.setText(_translate("MainWindow", "间隔:"))
        self.playBtn.setText(_translate("MainWindow", "执行"))
