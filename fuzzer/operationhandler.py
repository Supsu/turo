"""
This module handles running the fuzzing.
"""
import threading
import time
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from ..fuzzer.logger import Logger

class OperationHandler(threading.Thread, QObject):
    """
        OperationHandler takes care of handling the communication between running the process,
        mutating data and logging the output.

        Thread is started with the start() method.
    """

    # Signal for sending event logs upwards
    event_logged = pyqtSignal(int, str)

    def __init__(self, input_file, program_path, **kwargs):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        self._input_file = input_file
        self._program_path = program_path

        # Get program name
        index_s = self._program_path.rfind('/')
        index_p = self._program_path.rfind('.')
        if index_s != -1 and index_p != -1:
            program_name = self._program_path[index_s+1:index_p]
        else:
            program_name = "FilenameError"

        # look for verbose in kwargs
        verbose = False
        for key, value in kwargs.items():
            if key == "verbose":
                verbose = value

        self.logger = Logger(program_name, verbose)
        self.logger.event_logged.connect(self.event_slot)
        self.logger.log_event("This is a test event...", True)

    def run(self):
        """This function is the main function in the thread"""

        # For testing, just wait 5 seconds.
        time.sleep(5)

    def event_slot(self, ts, event):
        """Captures an event signal and handles it by passing it upwards"""
        print("Caught event")
        self.event_logged.emit(ts, event)

if __name__ == "__main__":
    a = OperationHandler("test/inputfile.py", "test/program.py")
