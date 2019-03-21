import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel, QSpacerItem, QPushButton, QTextEdit, QProgressBar
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt

"""

"""
class Gui:	

	def __init__(self):
		self.app = None
		self.main_window = None
		

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
		self.cwd = os.getcwd()
		self.file_dialog = QFileDialog()
		self.file_dialog.setFileMode(0) # set to AnyFile
		options = QFileDialog.Options()
		result = QFileDialog.getOpenFileName(self.main_window, "QFileDialog.getOpenFileName()", self.cwd, "", options=options)
		return result[0]

	def browse_for_program(self):
		self.chosen_file = self.create_file_browser()
		if len(self.chosen_file) != 0:
			self.pr_path.setText(self.chosen_file)

	def browse_for_input_file(self):
		self.chosen_file = self.create_file_browser()
		if len(self.chosen_file) != 0:
			self.ti_path.setText(self.chosen_file)

	def run(self):
		print("Run")

	def stop(self):
		print("Stop")

	def config(self):
		print("Config")

	def exit(self):
		exit()

if __name__ == "__main__":
	a = Gui()
	a.create_window()
