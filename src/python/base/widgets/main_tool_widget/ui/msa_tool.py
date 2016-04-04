# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../python/base/widgets/main_tool_widget/resources/msa_tool.ui'
#
# Created: Mon Apr  4 02:43:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_msa_tool(object):
    def setupUi(self, msa_tool):
        msa_tool.setObjectName("msa_tool")
        msa_tool.resize(746, 301)
        self.widget = QtGui.QWidget(msa_tool)
        self.widget.setGeometry(QtCore.QRect(12, 12, 565, 242))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_file = QtGui.QCommandLinkButton(self.widget)
        self.select_file.setObjectName("select_file")
        self.horizontalLayout_2.addWidget(self.select_file)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_shot = QtGui.QComboBox(self.widget)
        self.comboBox_shot.setObjectName("comboBox_shot")
        self.horizontalLayout.addWidget(self.comboBox_shot)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_tasks = QtGui.QComboBox(self.widget)
        self.comboBox_tasks.setObjectName("comboBox_tasks")
        self.horizontalLayout.addWidget(self.comboBox_tasks)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeView = QtGui.QTreeView(self.widget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(msa_tool)
        QtCore.QMetaObject.connectSlotsByName(msa_tool)

    def retranslateUi(self, msa_tool):
        msa_tool.setWindowTitle(QtGui.QApplication.translate("msa_tool", "MSA Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file.setText(QtGui.QApplication.translate("msa_tool", "Select MEGA File", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file.setDescription(QtGui.QApplication.translate("msa_tool", "Select MEGA file from your system to parse through", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("msa_tool", "Positions", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("msa_tool", "Mutations", None, QtGui.QApplication.UnicodeUTF8))

