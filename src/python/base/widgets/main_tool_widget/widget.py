"""
.. module:: base.widgets.main_tool_widget.widget
   :platform: Unix (CentOS)
   :synopsis: ___DESC___

.. moduleauthor:: Shiva Kannan <sssk2006@gmail.com>
"""

# =============================================================================
# IMPORTS
# =============================================================================

# General imports
from PySide import QtCore, QtGui

# Tool imports
from base.widgets.main_tool_widget.ui.msa_tool import Ui_msa_tool

# =============================================================================
# CLASSES
# =============================================================================
class MsaToolWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MsaToolWidget, self).__init__(parent)

        self.ui = Ui_msa_tool()
        self.ui.setupUi(self)

        self.connect_widgets()


    def connect_widgets(self):

        self.ui.select_file.released.connect(self.select_msa_file)


    def select_msa_file(self):
        """
        Get the file to be parsed through from file browser dialog.
        :return:
        """
        open_file = QtGui.QFileDialog.getOpenFileName(
            self,
            caption="Select MEGA file"
        )

        file = open_file[0].decode('utf-8')

        print file




# =============================================================================
# EXCEPTIONS
# =============================================================================


# =============================================================================
# FUNCTIONS
# =============================================================================
