import shlex
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from ..fuzzer.operationhandler import OperationHandler
# TODO: import ConfigData

class Controller:

	def __init__(self, args):
		self.operationhandler = None
		self.args = args
		self.sendLogMessage = pyqtSignal(str)

	# TODO: Sanitation needed for filepaths?
	#       It comes from Qt's widget so one would think that that sanitizes it...
	def run(self, input_path, program_path, config_data):

		# Run shlex for args
		# TODO: Check this later
		self.passed_args = shlex.split(self.args)
		
		self.operationhandler = OperationHandler(input_path, program_path)

		self.operationhandler.run()

if __name__ == "__main__":
	a = Controller("123")
	a.run("", "", None)