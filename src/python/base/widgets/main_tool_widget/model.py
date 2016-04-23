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
from Bio.SubsMat import MatrixInfo


# Tool Imports

# =============================================================================
# CLASSES
# =============================================================================

class DisplayMutations(QtGui.QStandardItemModel):
    headers = ['Position', 'Residue', 'No. of Mutations', 'Score']

    blosum = MatrixInfo.blosum62


    ITEM_ROLE = QtCore.Qt.UserRole + 1

    def __init__(self, parent=None):
        super(DisplayMutations, self).__init__()
        # self._mega_file = file

        self.item = QtGui.QStandardItem
        self.setHorizontalHeaderLabels(self.headers)
        self.root_item = self.invisibleRootItem()

    def fill_rows_mutations(self, no_mutation_dict, mutations_dict, blosum_dict):
        """
        This function fills the rows with the appropriate columns
        :return:
        """
        for (k1,v1) , (k2, v2) , (k3,v3) in zip(no_mutation_dict.items(), mutations_dict.items(), blosum_dict.items()):
            if v3 < -1:
                row = [self.item(str(k1)), self.item(v2[0]),
                       self.item(str(v1)), self.item(str(v3))]
                # for item in row:
                #     item.setSelectable(False)
                self.root_item.appendRow(row)

