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
import collections

# Tool Imports

# =============================================================================
# CLASSES
# =============================================================================

class DisplayDetailedMutations(QtGui.QStandardItemModel):
    headers1 = ['Mutation', 'Strain ID', 'Score']
    headers2 = ['Type of Mutations', 'Count']

    blosum = MatrixInfo.blosum62

    MATRICES = {'BLOSUM 62' : MatrixInfo.blosum62 , 'PAM 30' : MatrixInfo.pam30 , 'PAM 250' : MatrixInfo.pam250}

    ITEM_ROLE = QtCore.Qt.UserRole + 1

    def __init__(self, parent=None):
        super(DisplayDetailedMutations, self).__init__()

        self.item = QtGui.QStandardItem


    def fill_detailed_mutations_rows(self, mutations_strains):
        """
        Fills the Tree View rows with all the mutations for the particular position
        :param mutations_strains:
        :return:
        """

        self.setHorizontalHeaderLabels(self.headers1)
        self.root_item = self.invisibleRootItem()
        consensus_residue = mutations_strains[0].keys()[0]
        index = 0
        for mutation in mutations_strains:
            if index != 0:
                if consensus_residue == '-':
                    score = -5
                elif consensus_residue == '?':
                    score = 'NA'
                else:
                    try :
                        score = self.MATRICES['BLOSUM 62'][(consensus_residue,mutation.keys()[0])]
                    except KeyError:
                        score = self.MATRICES['BLOSUM 62'][(mutation.keys()[0], consensus_residue)]
                row = [self.item(mutation.keys()[0]),
                       self.item(mutation.values()[0]),
                       self.item(str(score))]
                row[0].setData(mutation.values()[0], QtCore.Qt.UserRole)
                self.root_item.appendRow(row)
            index += 1

    def fill_mutation_types(self, mutation_strains):
        """
        Fills the Tree View with the types of mutations and the number of types.
        :param mutation_strains:
        :return:
        """
        self.setHorizontalHeaderLabels(self.headers2)
        self.root_item = self.invisibleRootItem()

        consensus_residue = mutation_strains[0].keys()[0]
        type_list = []

        for mutation in mutation_strains[1:]:
            type = '%s -> %s'%(consensus_residue, mutation.keys()[0])
            type_list.append(type)

        type_counter = collections.Counter(type_list)

        for type in type_counter:
            row = [self.item(type), self.item(str(type_counter[type]))]
            self.root_item.appendRow(row)