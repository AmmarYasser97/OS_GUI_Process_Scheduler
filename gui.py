from PyQt5 import QtCore, QtGui, QtWidgets
from priority import priority_scheduling
from sjf import sjf
from roundRobin import round_robin
from Processes_Class import FCFS

task_list = []


class Ui_MainWindow(object):
    scheduling_algorithm = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 509)
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.schedule_btn = QtWidgets.QPushButton(self.centralwidget)
        self.schedule_btn.setGeometry(QtCore.QRect(580, 10, 171, 91))
        self.schedule_btn.setObjectName("schedule_btn")
        self.schedule_btn.clicked.connect(self.schedule)
        self.Algorithm_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Algorithm_Box.setGeometry(QtCore.QRect(10, 10, 251, 80))
        self.Algorithm_Box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Algorithm_Box.setFlat(False)
        self.Algorithm_Box.setCheckable(False)
        self.Algorithm_Box.setObjectName("Algorithm_Box")
        self.algorithm = QtWidgets.QComboBox(self.Algorithm_Box)
        self.algorithm.setGeometry(QtCore.QRect(10, 30, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(14)
        self.algorithm.setFont(font)
        self.algorithm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.algorithm.setEditable(False)
        self.algorithm.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.algorithm.setObjectName("algorithm")
        self.algorithm.currentTextChanged.connect(self.select_algorithm)
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.Quantum_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Quantum_Box.setGeometry(QtCore.QRect(280, 10, 111, 61))
        self.Quantum_Box.setObjectName("Quantum_Box")
        self.quantum = QtWidgets.QSpinBox(self.Quantum_Box)
        self.quantum.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.quantum.setObjectName("quantum")
        self.preemptive = QtWidgets.QCheckBox(self.centralwidget)
        self.preemptive.setGeometry(QtCore.QRect(280, 70, 121, 31))
        self.preemptive.setObjectName("preemptive")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 741, 111))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 40, 251, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.task_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.task_name.setGeometry(QtCore.QRect(10, 30, 231, 20))
        self.task_name.setObjectName("task_name")
        self.Quantum_Box_2 = QtWidgets.QGroupBox(self.groupBox)
        self.Quantum_Box_2.setGeometry(QtCore.QRect(280, 40, 111, 61))
        self.Quantum_Box_2.setObjectName("Quantum_Box_2")
        self.arrive_time = QtWidgets.QSpinBox(self.Quantum_Box_2)
        self.arrive_time.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.arrive_time.setObjectName("arrive_time")
        self.Quantum_Box_3 = QtWidgets.QGroupBox(self.groupBox)
        self.Quantum_Box_3.setGeometry(QtCore.QRect(400, 40, 141, 61))
        self.Quantum_Box_3.setObjectName("Quantum_Box_3")
        self.burst = QtWidgets.QSpinBox(self.Quantum_Box_3)
        self.burst.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.burst.setObjectName("burst")
        self.Priority_Box = QtWidgets.QGroupBox(self.groupBox)
        self.Priority_Box.setGeometry(QtCore.QRect(550, 40, 111, 61))
        self.Priority_Box.setObjectName("Priority_Box")
        self.priority = QtWidgets.QSpinBox(self.Priority_Box)
        self.priority.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.priority.setObjectName("priority")
        self.add_task_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_task_btn.setGeometry(QtCore.QRect(670, 60, 61, 31))
        self.add_task_btn.setObjectName("add_task_btn")
        self.add_task_btn.clicked.connect(self.addTask)
        self.tasks = QtWidgets.QTableWidget(self.centralwidget)
        self.tasks.setGeometry(QtCore.QRect(10, 220, 741, 281))
        self.tasks.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tasks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tasks.setTabKeyNavigation(False)
        self.tasks.setProperty("showDropIndicator", False)
        self.tasks.setDragDropOverwriteMode(False)
        self.tasks.setWordWrap(False)
        self.tasks.setCornerButtonEnabled(False)
        self.tasks.setObjectName("tasks")
        self.tasks.setColumnCount(4)
        self.tasks.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tasks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasks.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tasks.setHorizontalHeaderItem(3, item)
        self.tasks.horizontalHeader().setDefaultSectionSize(175)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.schedule_btn.setText(_translate("MainWindow", "Schedule"))
        self.Algorithm_Box.setTitle(_translate(
            "MainWindow", "Select Scheduling Algorithm"))
        self.algorithm.setCurrentText(_translate("MainWindow", "FCFS"))
        self.algorithm.setItemText(0, _translate("MainWindow", "FCFS"))
        self.algorithm.setItemText(1, _translate("MainWindow", "SJF"))
        self.algorithm.setItemText(2, _translate("MainWindow", "Priority"))
        self.algorithm.setItemText(3, _translate("MainWindow", "Round Robin"))
        self.Quantum_Box.setTitle(_translate("MainWindow", "Quantum"))
        self.preemptive.setText(_translate("MainWindow", "Preemptive"))
        self.groupBox.setTitle(_translate("MainWindow", "Enter Tasks"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Name"))
        self.Quantum_Box_2.setTitle(_translate("MainWindow", "Arrive Time"))
        self.Quantum_Box_3.setTitle(_translate("MainWindow", "Burst Duration"))
        self.Priority_Box.setTitle(_translate("MainWindow", "Priority"))
        self.add_task_btn.setText(_translate("MainWindow", "Add"))
        self.tasks.setSortingEnabled(True)
        item = self.tasks.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tasks.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrive Time"))
        item = self.tasks.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst Time"))
        item = self.tasks.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Priority"))

    #
    #

    def select_algorithm(self, text):
        self.scheduling_algorithm = str(text)
        if self.scheduling_algorithm == "Round Robin":
            self.Quantum_Box.show()
            self.preemptive.hide()
            self.Priority_Box.hide()
            self.tasks.setColumnHidden(3, True)

        elif self.scheduling_algorithm == "FCFS":
            self.Quantum_Box.hide()
            self.preemptive.hide()
            self.Priority_Box.hide()
            self.tasks.setColumnHidden(3, True)

        elif self.scheduling_algorithm == "SJF":
            self.Quantum_Box.hide()
            self.preemptive.show()
            self.Priority_Box.hide()
            self.tasks.setColumnHidden(3, True)

        elif self.scheduling_algorithm == "Priority":
            self.Quantum_Box.hide()
            self.preemptive.show()
            self.Priority_Box.show()
            self.tasks.setColumnHidden(3, False)

    def addTask(self):
        name = str(self.task_name.text())
        arrive_time = str(self.arrive_time.text())
        burst = str(self.burst.text())
        priority = str(self.priority.text())

        task = dict(task=name, arrival_time=int(arrive_time), burst_time=int(burst), priority=priority)
        task_list.append(task)

        rowPosition = self.tasks.rowCount()
        self.tasks.insertRow(rowPosition)
        self.tasks.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(name))
        self.tasks.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(arrive_time))
        self.tasks.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(burst))
        self.tasks.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(priority))

    def schedule(self):
        if self.scheduling_algorithm == "Round Robin":
            output_list = round_robin(task_list, int(self.quantum.text()))
        elif self.scheduling_algorithm == "Priority":
            output_list = priority_scheduling(task_list, self.preemptive.isChecked())
        elif self.scheduling_algorithm == "FCFS":
            output_list = FCFS(task_list)
        elif self.scheduling_algorithm == "SJF":
            output_list = sjf(task_list, self.preemptive.isChecked())
        else:
            output_list = []

        print(output_list)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
