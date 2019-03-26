import asyncio
from ..fuzzer.operationhandler import OperationHandler

class Controller:

	def __init__(self):
		self.operationhandler = None

	# TODO: Sanitation needed for filepaths?
	#       It comes from Qt's widget so one would think that that sanitizes it...
	def run(self, input_path, program_path, config_data):
		self.config = config_data

		self.operationhandler = OperationHandler(self.input_path, program_path)






if __name__ == "__main__":
	a = Controller()