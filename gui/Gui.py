import os

import copy
from datetime import datetime
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel, QSpacerItem, QPushButton, QTextEdit, QProgressBar, QSpinBox, QCheckBox
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.QtCore import Qt, QObject
# TODO: Controller needs to be merged
from ..util.util import ConfigData
from ..controller.controller import Controller

class Gui(QObject):	

    def __init__(self):
        super(Gui, self).__init__()
        self.app = None
        self.main_window = None

        self.config_data = ConfigData(10, True, 1000)

    """
    Creates a new main window and opens it
    """
    def create_window(self):
        self.app = QApplication([])
        self.main_window = QMainWindow()
        self.main_window.resize(800, 600)
        self.main_window.setWindowTitle("Turo")

        # Creating the main windget
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        """
            Splitting creating different bits of the gui into separate
            functions for the sake of keeping the create_window method
            at least somewhat manageable in size.
        """
        self.create_input_widget()
        self.create_status_widget()

        # Main widget spacer
        self.main_spacer = QSpacerItem(0, 0)

        # Set widgets into main widget
        self.main_layout.addWidget(self.input_widget)
        self.main_layout.addSpacerItem(self.main_spacer)
        self.main_layout.addWidget(self.status_widget)

        self.main_window.setCentralWidget(self.main_widget)

        # Connect all the buttons to their functions
        self.pr_browse_button.clicked.connect(self.browse_for_program)
        self.ti_browse_button.clicked.connect(self.browse_for_input_file)
        self.status_run.clicked.connect(self.run)
        self.status_stop.clicked.connect(self.stop)
        self.status_config.clicked.connect(self.config)
        self.status_exit.clicked.connect(self.exit)

        self.main_window.show()
        self.app.exec_()

    """
    Creates the input widget for the main window
    """
    def create_input_widget(self):
        self.input_widget = QWidget()
        self.pr_path = QLineEdit()
        self.ti_path = QLineEdit()
        self.pr_label = QLabel("Program path")
        self.ti_label = QLabel("Input path")
        
        # browse program path button
        self.pr_browse_widget = QWidget()
        self.pr_browse_button = QPushButton("Browse")
        self.pr_browse_spacer = QSpacerItem(300, 0)
        self.pr_browse_layout = QHBoxLayout()
        self.pr_browse_layout.addWidget(self.pr_browse_button)
        self.pr_browse_layout.addSpacerItem(self.pr_browse_spacer)
        self.pr_browse_widget.setLayout(self.pr_browse_layout)

        # browse input file path button
        self.ti_browse_widget = QWidget()
        self.ti_browse_button = QPushButton("Browse")
        self.ti_browse_spacer = QSpacerItem(300, 0)
        self.ti_browse_layout = QHBoxLayout()
        self.ti_browse_layout.addWidget(self.ti_browse_button)
        self.ti_browse_layout.addSpacerItem(self.ti_browse_spacer)
        self.ti_browse_widget.setLayout(self.ti_browse_layout)

        self.input_layout = QGridLayout()
        self.input_layout.addWidget(self.pr_label, 0, 0)
        self.input_layout.addWidget(self.pr_path, 1, 0)
        self.input_layout.addWidget(self.pr_browse_widget, 2, 0)
        self.input_layout.addWidget(self.ti_label, 0, 1)
        self.input_layout.addWidget(self.ti_path, 1, 1)
        self.input_layout.addWidget(self.ti_browse_widget, 2, 1)
        self.input_widget.setLayout(self.input_layout)

    # Creates the bottom part of the GUI
    def create_status_widget(self):
        self.status_widget = QWidget()
        self.status_buttons = QWidget()
        self.status_log_widget = QWidget()
        self.status_log = QTextEdit()
        self.status_progress = QProgressBar()
        self.status_run = QPushButton("Run")
        self.status_stop = QPushButton("Stop")
        self.status_config = QPushButton("Config")
        self.status_exit = QPushButton("Exit")

        self.status_log.setReadOnly(True)
        self.status_progress.setMinimum(0)
        self.status_progress.setMaximum(10)

        self.status_layout = QHBoxLayout()
        self.status_button_layout = QVBoxLayout()
        self.status_log_layout = QVBoxLayout()

        self.status_button_layout.addWidget(self.status_run)
        self.status_button_layout.addWidget(self.status_stop)
        self.status_button_layout.addWidget(self.status_config)
        self.status_button_layout.addSpacerItem(QSpacerItem(0,300))
        self.status_button_layout.addWidget(self.status_exit)
        self.status_buttons.setLayout(self.status_button_layout)

        self.status_log_layout.addWidget(self.status_log)
        self.status_log_layout.addWidget(self.status_progress)
        self.status_log_widget.setLayout(self.status_log_layout)

        self.status_layout.addWidget(self.status_buttons)
        self.status_layout.addWidget(self.status_log_widget)
        self.status_widget.setLayout(self.status_layout)


    """
    Creates a file dialog at the current working directory and 
    returns the path to the file that was selected by the user. Returns an 
    empty string if no file chosen.
    """
    def create_file_browser(self):
        cwd = os.getcwd()
        file_dialog = QFileDialog()
        file_dialog.setFileMode(0) # set to AnyFile
        options = QFileDialog.Options()
        result = QFileDialog.getOpenFileName(self.main_window, "QFileDialog.getOpenFileName()", cwd, "", options=options)
        return result[0]

    def create_config_dialog(self):
        conf_dialog = QDialog()
        conf_dialog.setWindowTitle("Configuration")
        conf_dialog.setWindowModality(Qt.ApplicationModal)
        config_data_tmp = copy.deepcopy(self.config_data)

        it_widget = QWidget()
        it_label = QLabel("Iterations")
        it_spinbox = QSpinBox()
        it_spinbox.setMinimum(0)
        it_spinbox.setMaximum(1000000)
        it_spinbox.setValue(config_data_tmp.iterations)

        verb_widget = QWidget()
        #verb_label = QLabel("Verbose")
        verb_checkbox = QCheckBox("Verbose")
        verb_checkbox.setTristate(False)
        verb_checkbox.setChecked(config_data_tmp.verbose)

        tim_widget = QWidget()
        tim_label = QLabel("Timeout (ms)")
        tim_spinbox = QSpinBox()
        tim_spinbox.setMinimum(0)
        tim_spinbox.setMaximum(36000000)
        tim_spinbox.setValue(1000)

        config_button_widget = QWidget()
        config_button_accept = QPushButton("Accept")
        config_button_decline = QPushButton("Decline")

        config_layout = QVBoxLayout()
        config_it_layout = QHBoxLayout()
        config_verb_layout = QHBoxLayout()
        config_tim_layout = QHBoxLayout()

        config_button_layout = QHBoxLayout()

        config_it_layout.addWidget(it_spinbox)
        config_it_layout.addWidget(it_label)
        it_widget.setLayout(config_it_layout)

        config_verb_layout.addWidget(verb_checkbox)
        verb_widget.setLayout(config_verb_layout)

        config_tim_layout.addWidget(tim_spinbox)
        config_tim_layout.addWidget(tim_label)
        tim_widget.setLayout(config_tim_layout)

        config_button_layout.addWidget(config_button_accept)
        config_button_layout.addWidget(config_button_decline)
        config_button_widget.setLayout(config_button_layout)

        config_layout.addWidget(it_widget)
        config_layout.addWidget(verb_widget)
        config_layout.addWidget(tim_widget)

        config_layout.addWidget(config_button_widget)

        conf_dialog.setLayout(config_layout)

        config_button_accept.clicked.connect(conf_dialog.accept)
        config_button_decline.clicked.connect(conf_dialog.reject)

        it_spinbox.valueChanged.connect(self.config_iterations_value_change)
        verb_checkbox.stateChanged.connect(self.config_verbose_value_change)

        conf_dialog.exec()

        if conf_dialog.result() != QDialog.Accepted:
            self.config_data = copy.deepcopy(config_data_tmp)
        else:
            self.status_progress.setMaximum = self.config_data.iterations

    def config_iterations_value_change(self, value):
        self.config_data.iterations = value

    def config_verbose_value_change(self, value):
        if value == Qt.Checked:
            self.config_data.verbose = True
        else:
            self.config_data.verbose = False

    # Slot for program browse button
    def browse_for_program(self):
        chosen_file = self.create_file_browser()
        if len(chosen_file) != 0:
            self.pr_path.setText(chosen_file)

    # Slot for input browse button
    def browse_for_input_file(self):
        chosen_file = self.create_file_browser()
        if len(chosen_file) != 0:
            self.ti_path.setText(chosen_file)

    # Starts the fuzzer with the current config settings
    def run(self):
        self.log_event(self.current_timestamp(), "Run is not implemented yet")
        
        input_file = self.ti_path.text()
        program_file = self.pr_path.text()
        config = self.config_data

        if len(input_file) > 0 or len(program_file > 0):
            self.log_event(self.current_timestamp(), "Starting fuzzer...")
            self.controller = Controller(input_file, program_file, config)
            self.controller.log_event.connect(self.log_event)
        else:
            self.log_event(self.current_timestamp(), "Failed to start fuzzer: input or program file paths not set.")

    # Stops the fuzzer
    def stop(self):
        self.log_event(self.current_timestamp(), "Stop is not implemented yet")
        # TODO: all of it

    # Opens the config dialog
    def config(self):
        self.create_config_dialog()

    # Quits the program
    def exit(self):
        exit_dialog = QDialog()
        exit_dialog.setWindowTitle("Confirm exit")

        exit_label = QLabel("Confirm exit")
        exit_label.setAlignment(Qt.AlignHCenter)
        exit_button_ok = QPushButton("Yes")
        exit_button_no = QPushButton("No")
        exit_button_widget = QWidget()

        exit_layout = QVBoxLayout()
        exit_button_layout = QHBoxLayout()
        exit_layout.addWidget(exit_label)

        exit_button_layout.addWidget(exit_button_ok)
        exit_button_layout.addWidget(exit_button_no)
        exit_button_widget.setLayout(exit_button_layout)
        exit_layout.addWidget(exit_button_widget)

        exit_button_ok.clicked.connect(exit_dialog.accept)
        exit_button_no.clicked.connect(exit_dialog.reject)

        exit_dialog.setLayout(exit_layout)

        exit_dialog.exec()

        if exit_dialog.result() == QDialog.Accepted:
            exit()
        # TODO: Go a graceful exit where the fuzzer doesn't just immediately
        #       explode. Preferably with no core dumps or anything.

    """
        Logs an event into the gui log. Timestamp taken in as unix timestamp
        as an integer, event as a string.
    """
    def log_event(self, timestamp, event):
        try:
            ts = int(timestamp)
        except:
            ts = 0

        eventstring = "[" + datetime.fromtimestamp(ts).strftime('%H:%M:%S') + "]: "
        eventstring += str(event)

        self.status_log.append(eventstring)

    """
        Sets current progress bar value to the given value.
        Maximum is determined by the iterations set at the start of the run.
    """
    def set_progress(self, value):
        try:
            v = int(value)
        except:
            v = self.status_progress.value()
            
        self.status_progress.setValue(v)

    """
        Gets current unix timestamp
    """
    def current_timestamp(self):
        dt = datetime.now()
        return int(time.mktime(dt.timetuple()))

if __name__ == "__main__":
    a = Gui()
    a.create_window()
