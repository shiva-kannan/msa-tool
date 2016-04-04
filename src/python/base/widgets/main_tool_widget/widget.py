"""
.. module:: tau.widgets.review_widget.widget
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


# =============================================================================
# EXCEPTIONS
# =============================================================================


# =============================================================================
# FUNCTIONS
# =============================================================================
