#import asyncio TODO: event loop in here or operation handler?
import shlex
from ..fuzzer.operationhandler import OperationHandler

class Controller:

	def __init__(self, args):
		self.operationhandler = None
		self.args = args

	# TODO: Sanitation needed for filepaths?
	#       It comes from Qt's widget so one would think that that sanitizes it...
	def run(self, input_path, program_path, config_data):
		self.config = config_data

		# Run shlex for args
		# TODO: Check this later
		self.passed_args = shlex.split(self.args)
		self.operationhandler = OperationHandler(self.input_path, program_path, self.passed_args

		self.operationhandler.run()





if __name__ == "__main__":
	a = Controller()