import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel, QSpacerItem, QPushButton
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

		# Creating the input widget ########################
		# variables related to program input gui features start with "pr"
		# and variables related to test input begin with "ti"
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

		# Main widget spacer
		self.main_spacer = QSpacerItem(800, 600)

		# Set widgets into main widget
		self.main_layout.addWidget(self.input_widget)
		self.main_layout.addSpacerItem(self.main_spacer)

		self.main_window.setCentralWidget(self.main_widget)

		self.main_window.show()
		self.app.exec_()

	"""
	Creates a file dialog at the current working directory and 
	returns the path to the file that was selected by the user. Returns an 
	empty string if no file chosen.
	"""
	def create_file_browser(self):
		self.cwd = os.getcwd()
		self.file_dialog = QFileDialog()
		self.file_dialog.setFileMode(0) # set to AnyFile


	def browse_for_program(self):
		chosen_file = create_file_browser()
		if len(chosen_file) != 0:
			self.program_path_edit.setText(chosen_file)

	def browse_for_input_file(self):
		chosen_file = create_file_browser()
		if len(chosen_file) != 0:
			self.test_input_path_edit.setText(chosen_file)


if __name__ == "__main__":
	a = Gui()
	a.create_window()
