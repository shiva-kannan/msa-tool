# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../python/base/widgets/main_tool_widget/resources/msa_tool.ui'
#
# Created: Mon Apr  4 12:55:09 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_msa_tool(object):
    def setupUi(self, msa_tool):
        msa_tool.setObjectName("msa_tool")
        msa_tool.resize(678, 291)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(msa_tool)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_file = QtGui.QCommandLinkButton(msa_tool)
        self.select_file.setObjectName("select_file")
        self.horizontalLayout_2.addWidget(self.select_file)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(msa_tool)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_positions = QtGui.QComboBox(msa_tool)
        self.comboBox_positions.setObjectName("comboBox_positions")
        self.horizontalLayout.addWidget(self.comboBox_positions)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(msa_tool)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_mutations = QtGui.QComboBox(msa_tool)
        self.comboBox_mutations.setObjectName("comboBox_mutations")
        self.horizontalLayout.addWidget(self.comboBox_mutations)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.view_mutations = QtGui.QTreeView(msa_tool)
        self.view_mutations.setObjectName("view_mutations")
        self.verticalLayout.addWidget(self.view_mutations)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(msa_tool)
        QtCore.QMetaObject.connectSlotsByName(msa_tool)

    def retranslateUi(self, msa_tool):
        msa_tool.setWindowTitle(QtGui.QApplication.translate("msa_tool", "MSA Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file.setText(QtGui.QApplication.translate("msa_tool", "Select MEGA File", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file.setDescription(QtGui.QApplication.translate("msa_tool", "Select MEGA file from your system to parse through", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("msa_tool", "Positions", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("msa_tool", "Mutations", None, QtGui.QApplication.UnicodeUTF8))

