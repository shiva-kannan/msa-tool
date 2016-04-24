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
from Bio.SubsMat import MatrixInfo
from PySide import QtGui, QtCore

# Tool imports
from base.widgets.detail_widget.ui.detailed_widget import Ui_Detailed_mutations
from base.widgets.detail_widget.model import DisplayDetailedMutations

# =============================================================================
# CLASSES
# =============================================================================

# Global Dictionary for Substition Matrices:

MATRICES = {'BLOSUM 62' : MatrixInfo.blosum62 , 'PAM 30' : MatrixInfo.pam30 , 'PAM 250' : MatrixInfo.pam250}


class MsaDetailedToolWidget(QtGui.QWidget):
    def __init__(self, mutations_strains, position, parent=None):
        super(MsaDetailedToolWidget, self).__init__(parent)

        self.ui = Ui_Detailed_mutations()
        self.ui.setupUi(self)

        # self.fill_matrices_combobox()
        # self.connect_widgets()

        self.mutations_strains = mutations_strains
        self.position = position

        self.display_detailed_model = DisplayDetailedMutations(parent=self)
        self.ui.treeView_detailed_mutations.setModel(self.display_detailed_model)
        self.display_mutation_types_model = DisplayDetailedMutations(parent=self)
        self.ui.treeView_mutation_types.setModel(self.display_mutation_types_model)

        # for item in self.mutations_strains:
        #     print item
        self.ui.label_consensus_residue.setText(self.mutations_strains[0].keys()[0])
        self.ui.label_position.setText(str(self.position))

        self.display_detailed_mutations()

        self.connect_widgets()


    def display_detailed_mutations(self):

        self.display_detailed_model.fill_detailed_mutations_rows(mutations_strains=self.mutations_strains)
        self.display_mutation_types_model.fill_mutation_types(mutation_strains=self.mutations_strains)


    def connect_widgets(self):

        self.ui.treeView_detailed_mutations.doubleClicked.connect(self.open_url)

    def open_url(self):

        selections = self.ui.treeView_detailed_mutations.selectedIndexes()
        selected =  selections[0].model().data(selections[0], QtCore.Qt.UserRole)
        selected = selected.replace('#','')
        selected = "http://www.uniprot.org/uniprot/?query=%s"%(selected)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(selected))
