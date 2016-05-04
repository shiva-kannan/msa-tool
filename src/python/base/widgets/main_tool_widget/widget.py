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
from base.widgets.main_tool_widget.ui.msa_tool import Ui_msa_tool
from base.widgets.main_tool_widget.model import DisplayMutations
from base.widgets.detail_widget.widget import MsaDetailedToolWidget

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
        # self.proxy_model = QtGui.QSortFilterProxyModel(self)
        # self.proxy_model.setSourceModel(self.display_minimum_model)
        self.ui.treeView_mutations.setModel(self.display_minimum_model)

        self.mutations_new_dict = {}
        self.no_mutation_dict = {}
        self.mutations_dict = {}
        self.blosum_dict = {}
        self.disable_ui_elements = []

        # Initially disable UI elements that have no significance before file is selected.
        self.ui.lineEdit_max_range.setDisabled(True)
        self.disable_ui_elements.append(self.ui.lineEdit_max_range)
        self.ui.lineEdit_min_range.setDisabled(True)
        self.disable_ui_elements.append(self.ui.lineEdit_min_range)
        self.ui.pushButton_apply_range.setDisabled(True)
        self.disable_ui_elements.append(self.ui.pushButton_apply_range)
        self.ui.comboBox_matrices.setDisabled(True)
        self.disable_ui_elements.append(self.ui.comboBox_matrices)
        self.ui.comboBox_threshold.setDisabled(True)
        self.disable_ui_elements.append(self.ui.comboBox_threshold)

        self.threshold = ['All', 'Negative ( < 0)', 'Negative ( < -1)']


    def connect_widgets(self):

        self.ui.pushButton_apply_range.released.connect(self.apply_residue_range)

        self.ui.select_file.released.connect(self.select_msa_file)

        self.ui.treeView_mutations.doubleClicked.connect(self.show_detailed_mutations)

        self.ui.comboBox_threshold.currentIndexChanged.connect(self.apply_residue_range)



    def fill_matrices_combobox(self):
        """
        Fills the Matrices comboBox with the Matrices avaliable from the Global MATRICES dictionary.
        :return:
        """

        # TODO : For now have included only the BLOSUM 62 Matrix
        for matrix in MATRICES:
            if matrix == "BLOSUM 62":
                self.ui.comboBox_matrices.addItem(matrix)
        self.ui.comboBox_matrices.setCurrentIndex(0)
        self.ui.comboBox_matrices.setEditable(False)

    def show_detailed_mutations(self):
        selections = self.ui.treeView_mutations.selectedIndexes()
        selected =  selections[0].model().data(selections[0], QtCore.Qt.UserRole)
        mutations_detailed = self.mutations_new_dict[selected]
        # for item in mutations_detailed:
        #     print item
        self.detailed_mutations = MsaDetailedToolWidget(mutations_strains=mutations_detailed, position=selected)
        self.detailed_mutations.show()

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

        # print seq_dict
        actual_seq_dict = {}
        infile1 = open(file)

        ####### New Code ###############
        main_strains_dict = {}
        infile3 = open(file)
        index = 0
        for line  in infile3:
            if '#' in line and '#MEGA' not in line:
                if line.split(' ')[0] not in main_strains_dict.values():
                    main_strains_dict[index] = line.split(' ')[0]
                    main_strains_dict[line.split(' ')[0]] = index
                index += 1

        # print main_strains_dict
        infile3.close()

        list_temp = ['' for i in range(len(seq_list))]
        k = 0
        for line in infile1:
            if '#' in line and '#MEGA' not in line:
                s = line.split(line.split(' ')[0])
                sequence = s[1].replace(' ', '')
                sequence = sequence.replace('\n', '')
                sequence = sequence.replace('\r', '')
                list_temp[main_strains_dict[line.split(' ')[0]]] = list_temp[main_strains_dict[line.split(' ')[0]]] + sequence


        # no_mutation_dict = {}
        # mutations_dict = {}
        # mutations_new_dict = {}

        self.number_of_elements = len(list_temp[0])

        for i in range(len(list_temp[0])):
            count = 0
            temp = []
            index = 1
            temp.append(list_temp[0][i])
            ## NC ##
            temp_new = []
            t = {}
            t[list_temp[0][i]] = main_strains_dict[0]
            temp_new.append(t)
            for item in list_temp[1:]:
                if not (item[i] == '.' or item[i] == '-'):
                    #print i , item[i]
                    tn = {}
                    tn[item[i]] = main_strains_dict[index]
                    temp_new.append(tn)
                    temp.append(item[i])
                    count += 1
                index += 1
            self.mutations_new_dict[i] = temp_new
            self.mutations_dict[i] = temp
            self.no_mutation_dict[i] = count

        # for item in mutations_new_dict:
        #     print item , mutations_new_dict[item]

        ########## New Code ############

        # list_temp = ['' for i in range(len(seq_list))]
        # k = 0
        # for line in infile1:
        #     if '#' in line and '#MEGA' not in line:
        #         s = line.split(line.split(' ')[0])
        #         sequence = s[1].replace(' ', '')
        #         sequence = sequence.replace('\n', '')
        #         sequence = sequence.replace('\r', '')
        #         list_temp[seq_dict[line.split(' ')[0]]] = list_temp[seq_dict[line.split(' ')[0]]] + sequence





        # for item in list_temp:
        #     print item
        # print len(list_temp)
        # no_mutation_dict = {}
        # mutations_dict = {}
        #
        # for i in range(len(list_temp[0])):
        #     count = 0
        #     temp = []
        #     temp.append(list_temp[0][i])
        #     for item in list_temp[1:]:
        #         if not (item[i] == '.' or item[i] == '-'):
        #             #print i , item[i]
        #             temp.append(item[i])
        #             count += 1
        #     mutations_dict[i] = temp
        #     no_mutation_dict[i] = count

        # blosum_dict = {}

        for item in self.mutations_dict:
            score = 0
            if len(self.mutations_dict[item][1:]) !=0 :
                for i in self.mutations_dict[item][1:]:
                        if self.mutations_dict[item][0] == '-':
                            score = len(self.mutations_dict[item][1:])*-5
                        elif i == '?':
                            continue
                        else:
                            try :
                                score += MATRICES['BLOSUM 62'][(self.mutations_dict[item][0],i)]
                            except KeyError:
                                score += MATRICES['BLOSUM 62'][(i,self.mutations_dict[item][0])]
            self.blosum_dict[item] = score

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

        # Consequent display of UI elements that needed file to be selected.
        self.fill_initial_range()
        self.fill_threshold_dropdown()

        for element in self.disable_ui_elements:
            element.setDisabled(False)

        self.display_minimum_model.fill_rows_mutations(self.no_mutation_dict,
                                                       self.mutations_dict,
                                                       self.blosum_dict,
                                                       threshold=-1)

    def fill_threshold_dropdown(self):

        for threshold in self.threshold:
            self.ui.comboBox_threshold.addItem(threshold)
        self.ui.comboBox_threshold.setCurrentIndex(2)

    def fill_initial_range(self):


        self.ui.lineEdit_min_range.setText('0')
        self.ui.lineEdit_max_range.setText(str(self.number_of_elements))


    def apply_residue_range(self):

        min_range = int(self.ui.lineEdit_min_range.text())
        max_range = int(self.ui.lineEdit_max_range.text())
        message = QtGui.QMessageBox()


        if (max_range - min_range <= 0) or min_range < 0 or max_range < 0 :

            message.setText("Input Range is invalid!")
            message.setInformativeText("Please enter a valid subset of the Range 0 - %s"
                                       %(str(self.number_of_elements)))
            message.setStandardButtons(QtGui.QMessageBox.Ok)
            ret = message.exec_()
        else:
            index = self.ui.comboBox_threshold.currentIndex()
            if index == 0:
                threshold = None
            elif index == 1:
                threshold = 0
            else:
                threshold = -1
            residue_range = min_range , max_range
            self.display_minimum_model.fill_rows_mutations(self.no_mutation_dict,
                                                           self.mutations_dict,
                                                           self.blosum_dict,
                                                           threshold=threshold,
                                                           residue_range=residue_range)





# =============================================================================
# EXCEPTIONS
# =============================================================================


# =============================================================================
# FUNCTIONS
# =============================================================================
