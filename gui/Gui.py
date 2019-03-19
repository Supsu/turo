from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel, QSpacerItem
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
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

		# Creating the input widget
		self.input_widget = QWidget()
		self.program_line_edit = QLineEdit()
		self.test_input_line_edit = QLineEdit()
		self.program_label = QLabel("Program path")
		self.test_input_label = QLabel("Input path")

		self.input_layout = QGridLayout()
		self.input_layout.addWidget(self.program_label, 0, 0)
		self.input_layout.addWidget(self.program_line_edit, 1, 0)
		self.input_layout.addWidget(self.test_input_label, 0, 1)
		self.input_layout.addWidget(self.test_input_line_edit, 1, 1)
		self.input_widget.setLayout(self.input_layout)

		# Main widget spacer
		self.main_spacer = QSpacerItem(800, 600)

		# Set widgets into main widget
		self.main_layout.addWidget(self.input_widget)
		#self.main_layout.addWidget(self.main_spacer)

		self.main_window.setCentralWidget(self.main_widget)

		self.main_window.show()
		self.app.exec_()


if __name__ == "__main__":
	a = Gui()
	a.create_window()
