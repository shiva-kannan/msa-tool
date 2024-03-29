# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../python/base/widgets/main_tool_widget/resources/msa_tool.ui'
#
# Created: Wed May  4 11:23:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_msa_tool(object):
    def setupUi(self, msa_tool):
        msa_tool.setObjectName("msa_tool")
        msa_tool.resize(677, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(msa_tool.sizePolicy().hasHeightForWidth())
        msa_tool.setSizePolicy(sizePolicy)
        msa_tool.setMinimumSize(QtCore.QSize(650, 400))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(msa_tool)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(msa_tool)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.select_file = QtGui.QCommandLinkButton(self.groupBox)
        self.select_file.setObjectName("select_file")
        self.horizontalLayout_3.addWidget(self.select_file)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(msa_tool)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_3 = QtGui.QLabel(msa_tool)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_min_range = QtGui.QLineEdit(msa_tool)
        self.lineEdit_min_range.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_min_range.setFont(font)
        self.lineEdit_min_range.setText("")
        self.lineEdit_min_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_min_range.setObjectName("lineEdit_min_range")
        self.horizontalLayout.addWidget(self.lineEdit_min_range)
        self.label_4 = QtGui.QLabel(msa_tool)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtGui.QFrame.Plain)
        self.label_4.setMidLineWidth(-16)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_max_range = QtGui.QLineEdit(msa_tool)
        self.lineEdit_max_range.setMaximumSize(QtCore.QSize(40, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_max_range.setFont(font)
        self.lineEdit_max_range.setText("")
        self.lineEdit_max_range.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_max_range.setObjectName("lineEdit_max_range")
        self.horizontalLayout.addWidget(self.lineEdit_max_range)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_apply_range = QtGui.QPushButton(msa_tool)
        self.pushButton_apply_range.setObjectName("pushButton_apply_range")
        self.verticalLayout.addWidget(self.pushButton_apply_range)
        self.label_2 = QtGui.QLabel(msa_tool)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_threshold = QtGui.QComboBox(msa_tool)
        self.comboBox_threshold.setObjectName("comboBox_threshold")
        self.verticalLayout.addWidget(self.comboBox_threshold)
        self.line = QtGui.QFrame(msa_tool)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem2 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtGui.QLabel(msa_tool)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox_matrices = QtGui.QComboBox(msa_tool)
        self.comboBox_matrices.setEditable(False)
        self.comboBox_matrices.setObjectName("comboBox_matrices")
        self.verticalLayout.addWidget(self.comboBox_matrices)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.treeView_mutations = QtGui.QTreeView(msa_tool)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_mutations.sizePolicy().hasHeightForWidth())
        self.treeView_mutations.setSizePolicy(sizePolicy)
        self.treeView_mutations.setMinimumSize(QtCore.QSize(420, 375))
        self.treeView_mutations.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView_mutations.setAlternatingRowColors(True)
        self.treeView_mutations.setObjectName("treeView_mutations")
        self.horizontalLayout_2.addWidget(self.treeView_mutations)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(msa_tool)
        QtCore.QMetaObject.connectSlotsByName(msa_tool)

    def retranslateUi(self, msa_tool):
        msa_tool.setWindowTitle(QtGui.QApplication.translate("msa_tool", "MSA Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("msa_tool", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file.setText(QtGui.QApplication.translate("msa_tool", "Select MEGA File", None, QtGui.QApplication.UnicodeUTF8))
        self.select_file.setDescription(QtGui.QApplication.translate("msa_tool", "Select MEGA file from your system to parse through", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("msa_tool", "Residue Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("msa_tool", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_apply_range.setText(QtGui.QApplication.translate("msa_tool", "Apply Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("msa_tool", "Score threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("msa_tool", "Matrix Type:", None, QtGui.QApplication.UnicodeUTF8))

