# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../python/base/resources/tool_panel.ui'
#
# Created: Mon Apr  4 02:43:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_msa_tool_panel(object):
    def setupUi(self, msa_tool_panel):
        msa_tool_panel.setObjectName("msa_tool_panel")
        msa_tool_panel.resize(700, 516)
        self.verticalLayout = QtGui.QVBoxLayout(msa_tool_panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(msa_tool_panel)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget_main = QtGui.QWidget(self.splitter)
        self.widget_main.setObjectName("widget_main")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_tools = QtGui.QWidget(self.widget_main)
        self.widget_tools.setEnabled(True)
        self.widget_tools.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_tools.setObjectName("widget_tools")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_tools)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_actions = QtGui.QFrame(self.widget_tools)
        self.frame_actions.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_actions.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_actions.setObjectName("frame_actions")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_actions)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_actions = QtGui.QGridLayout()
        self.layout_actions.setObjectName("layout_actions")
        self.horizontalLayout.addLayout(self.layout_actions)
        self.horizontalLayout_2.addWidget(self.frame_actions)
        self.verticalLayout_2.addWidget(self.widget_tools)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(msa_tool_panel)
        QtCore.QMetaObject.connectSlotsByName(msa_tool_panel)

    def retranslateUi(self, msa_tool_panel):
        msa_tool_panel.setWindowTitle(QtGui.QApplication.translate("msa_tool_panel", "MSA TOOL", None, QtGui.QApplication.UnicodeUTF8))

