"""
.. module:: panel
   :platform: Unix (CentOS)
   :synopsis: ${DESCRIPTION}

.. moduleauthor:: shiva (sssk2006@gmail.com)
"""

# =============================================================================
# IMPORTS
# =============================================================================

#Tool imports
from base.widgets.main_tool_widget.widget import MsaToolWidget
from base.ui.tool_panel import Ui_msa_tool_panel
#Standard import
from PySide import QtGui, QtCore
import sys


# =============================================================================
# CLASSES
# =============================================================================



class Msa_tool(QtGui.QMainWindow):
    def __init__(self):
        super(Msa_tool, self).__init__()

        self.ui = Ui_msa_tool_panel()
        self.ui.setupUi(self)

        self.msa_tool_widget = MsaToolWidget()
        self.ui.layout_actions.addWidget(self.msa_tool_widget)


# =============================================================================
# EXCEPTIONS
# =============================================================================


# =============================================================================
# FUNCTIONS
# =============================================================================