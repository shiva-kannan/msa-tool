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
from Bio.SubsMat import MatrixInfo

# Tool imports
from base.widgets.main_tool_widget.ui.msa_tool import Ui_msa_tool
from base.widgets.main_tool_widget.ui.model import DisplayMutations

# =============================================================================
# CLASSES
# =============================================================================

# Global Dictionary for Substition Matrices:

MATRICES = {'BLOSUM 62' : MatrixInfo.blosum62 , 'PAM 30' : MatrixInfo.pam30 , 'PAM 250' : MatrixInfo.pam250}


class MsaToolWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MsaToolWidget, self).__init__(parent)

        self.ui = Ui_msa_tool()
        self.ui.setupUi(self)

        self.fill_matrices_combobox()
        self.connect_widgets()

        self.display_minimum_model = DisplayMutations(parent=self)
        self.ui.treeView_mutations.setModel(self.display_minimum_model)


    def connect_widgets(self):

        self.ui.select_file.released.connect(self.select_msa_file)



    def fill_matrices_combobox(self):
        """
        Fills the Matrices comboBox with the Matrices avaliable from the Global MATRICES dictionary.
        :return:
        """

        for matrix in MATRICES:
            self.ui.comboBox_matrices.addItem(matrix)

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

        self.process_mega_file(file=file)


    def process_mega_file(self, file):
        """
        This function processes the MEGA file that is selected by the user
        :return:
        """

        infile2 = open(file)
        seq_dict = {}
        seq_list = []
        actual_seq = []
        j = 0
        for line in infile2:
            if '#' in line and '#MEGA' not in line:
                seq_list.append(line.split(' ')[0])
                if j == 0:
                    seq_dict[0] = seq_list[0]
                    seq_dict[seq_list[0]] = 0
                    j += 1

        seq_list = list(set(seq_list))
        i = 1
        for item in seq_list:
            if item != seq_dict[0]:
                seq_dict[i] = item
                seq_dict[item] = i
                i += 1

        actual_seq_dict = {}
        infile1 = open(file)
        list_temp = ['' for i in range(len(seq_list))]
        k = 0
        for line in infile1:
            if '#' in line and '#MEGA' not in line:
                s = line.split(line.split(' ')[0])
                sequence = s[1].replace(' ', '')
                sequence = sequence.replace('\n', '')
                sequence = sequence.replace('\r', '')
                list_temp[seq_dict[line.split(' ')[0]]] = list_temp[seq_dict[line.split(' ')[0]]] + sequence

        # for item in list_temp:
        #     print item
        #print len(list_temp)
        no_mutation_dict = {}
        mutations_dict = {}

        for i in range(len(list_temp[0])):
            count = 0
            temp = []
            temp.append(list_temp[0][i])
            for item in list_temp[1:]:
                if not (item[i] == '.' or item[i] == '-'):
                    #print i , item[i]
                    temp.append(item[i])
                    count += 1
            mutations_dict[i] = temp
            no_mutation_dict[i] = count

        blosum_dict = {}

        for item in mutations_dict:
            score = 0
            if len(mutations_dict[item][1:]) !=0 :
                for i in mutations_dict[item][1:]:
                        if mutations_dict[item][0] == '-':
                            score = len(mutations_dict[item][1:])*-5
                        elif i == '?':
                            continue
                        else:
                            try :
                                score += MATRICES['BLOSUM 62'][(mutations_dict[item][0],i)]
                            except KeyError:
                                score += MATRICES['BLOSUM 62'][(i,mutations_dict[item][0])]
            blosum_dict[item] = score

        # for m in mutations_dict:
        #     print mutations_dict[m]

        # for item in blosum_dict:
        #     print item , blosum_dict[item]
        #
        # print 'Position   | No.  '
        # print '--------'
        # for item in no_mutation_dict:
        #     print '%s       | %s '%(item, no_mutation_dict[item])
        # print '--------'
        # print 'Residue   | All mutations'
        # for item in mutations_dict:
        #     print '%s   | %s'%(item , mutations_dict[item])


        # for (k1,v1) , (k2, v2) , (k3,v3) in zip(no_mutation_dict.items(), mutations_dict.items(), blosum_dict.items()):
        #     if v3 < -1:
        #         print '%s->%s\t| %s\t| %s\t| %s'%(k1, v2[0], v1, v3, v2[1:])

        infile1.close()
        infile2.close()

        self.display_minimum_model.fill_rows_mutations(no_mutation_dict, mutations_dict, blosum_dict)
        self.fill_positions_dropdown(no_mutation_dict, blosum_dict)

    def fill_positions_dropdown(self, no_mutations, blosum_dict):

        for (k1, v1) , (k2, v2) in zip(no_mutations.items(), blosum_dict.items()):
            if v2 < -1:
                self.ui.comboBox_positions.addItem(str(k1))



# =============================================================================
# EXCEPTIONS
# =============================================================================


# =============================================================================
# FUNCTIONS
# =============================================================================
