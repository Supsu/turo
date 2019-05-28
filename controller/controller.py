import shlex
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from ..fuzzer.operationhandler import OperationHandler
from ..util.util import ConfigData
from datetime import datetime
import time

"""
Controller for the program. Creates OperationHandler and receives the config from GUI.

run() starts the program. 
Emits a log_Event signal when it wants to send a signal to the GUI to add a log event
to it's log window.
"""
class Controller(QObject):
	log_event = pyqtSignal(int, str)  # tells the Gui to add a log event to the Gui log
	progress_update = pyqtSignal(int) # updates progress in Gui for how many iterations have been completed

	def __init__(self, args):
		super(Controller, self).__init__()
		self.operationhandler = None
		self.args = args

	"""
	Starts up the entire sequence by creating the event handler
	"""
	def run(self, program_path, program_args, input_path, mutator_args, config_data):	

		# Run shlex for args
		# TODO: Check this later
		self.passed_args = shlex.split(self.args)
		
		epoch = current_timestamp()
		event = "Starting up handler..."
		self.log_event.emit(epoch, event)
		self.operationhandler = OperationHandler(input_path, program_path, verbose=config_data.verbose, timeout=config_data.timeout, iterations=config_data.iterations)
		# TODO: Remove comments when operation handler actually has these 
		self.operationhandler.event_logged.connect(self.log_received)
		self.operationhandler.progress_update.connect(self.progress_update_slot)

		self.operationhandler.run()

	"""
	For the stop button, whatever it will actually do
	"""
	def stop(self):
		pass

	"""
	Slot for receiving a log signal from OperationHandler
	"""
	def log_received(self, ts, event):
		self.log_event.emit(ts, event)

	"""
	Slot to capture iteration updates from operationhandler
	"""
	def progress_update_slot(self, progress):
		self.progress_update.emit(progress)

def current_timestamp():
	dt = datetime.now()
	return int(time.mktime(dt.timetuple()))

if __name__ == "__main__":
	a = Controller("123")
	c = ConfigData(10, True, 1000)
	a.run("", "", c)