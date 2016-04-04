"""
.. module:: model
   :platform: Unix (CentOS)
   :synopsis: ___DESC___

.. moduleauthor:: Shiva Kannan <sssk2006@gmail.com>, Tau Films
"""

# =============================================================================
# IMPORTS
# =============================================================================

# General Imports
from PySide import QtCore, QtGui

# Tool Imports

# =============================================================================
# CLASSES
# =============================================================================

class DisplayMutations(QtGui.QStandardItemModel):
    headers = []

    ITEM_ROLE = QtCore.Qt.UserRole + 1

    def __init__(self, file, parent=None):
        super(DisplayMutations, self).__init__()
        self._mega_file = file

