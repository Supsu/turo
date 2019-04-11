import shlex
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from ..fuzzer.operationhandler import OperationHandler
from ..gui.Gui import ConfigData

"""
Controller for the program. Creates OperationHandler and receives the config from GUI.

run() starts the program. 
Emits a log_Event signal when it wants to send a signal to the GUI to add a log event
to it's log window.
"""
class Controller(QObject):
	log_event = pyqtSignal(int, str)

	def __init__(self, args):
		super(Controller, self).__init__()
		self.operationhandler = None
		self.args = args
		self.sendLogMessage = pyqtSignal(str)

	# TODO: Sanitation needed for filepaths?
	#       It comes from Qt's widget so one would think that that sanitizes it...
	def run(self, input_path, program_path, config_data):	

		# Run shlex for args
		# TODO: Check this later
		self.passed_args = shlex.split(self.args)
		
		self.operationhandler = OperationHandler(input_path, program_path, verbose=config_data.verbose, timeout=config_data.timeout, iterations=config_data.iterations)

		self.operationhandler.run()

	"""
	Slot for receiving a log signal from OperationHandler
	"""
	def log_received(self, ts, event):
		self.log_event.emit(ts, event)

if __name__ == "__main__":
	a = Controller("123")
	a.run("", "", None)