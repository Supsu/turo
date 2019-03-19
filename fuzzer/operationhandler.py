"""
This module handles running the fuzzing.
"""
import threading
import time

class OperationHandler(threading.Thread):
    """
        OperationHandler takes care of handling the communication between running the process,
        mutating data and logging the output.

        Thread is started with the start() method.
    """
    def __init__(self, input_file, program_path, **kwargs):
        super().__init__()
        self._input_file = input_file
        self._program_path = program_path

    def run(self):
        """This function is the main function in the thread"""

        # For testing, just wait 5 seconds.
        time.sleep(5)
