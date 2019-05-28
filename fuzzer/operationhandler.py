"""
This module handles running the fuzzing.
"""
import threading
import time
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from ..fuzzer.logger import Logger
from ..fuzzer.runner import Runner

class OperationHandler(threading.Thread, QObject):
    """
        OperationHandler takes care of handling the communication between running the process,
        mutating data and logging the output.

        Thread is started with the start() method.
    """

    # Signal for sending event logs upwards
    event_logged = pyqtSignal(int, str)
    progress_update = pyqtSignal(int)

    def __init__(self, program_path, input_file, mutator_args, **kwargs):
        #print("Ophandler starting up...")
        threading.Thread.__init__(self)
        QObject.__init__(self)
        self._input_file = input_file
        self._program_path = program_path
        self._mutator_args = mutator_args

        # Get program name
        index_s = self._program_path.rfind('/')
        index_p = self._program_path.rfind('.')
        if index_s != -1 and index_p != -1:
            program_name = self._program_path[index_s+1:index_p]
        else:
            program_name = "FilenameError"

        # look for config values in kwargs
        self.verbose = False
        self.timeout = 1000
        self.iterations = 10
        for key, value in kwargs.items():
            if key == "verbose":
                self.verbose = value
            elif key == "timeout":
                self.timeout = value
            elif key == "iterations":
                self.iterations = value
            
        self.logger = Logger(program_name, self.verbose)
        self.logger.event_logged.connect(self.event_slot)

    def run(self):
        """This function is the main function in the thread"""
        self.logger.log_event("Starting run sequence...", True)

        # Parse the input file
        try:
            f = open(self._input_file, 'r')
        except OSError as error:
            self.logger.log_event("Failed to open input file", True)
            self.logger.log_event(error, True)
        
        inputs = []
        for line in f:
            inputs.append(line)

        f.close()

        for i in range(0, self.iterations):
            # select input args
            # mutating goes here
            prog_args = inputs[i%len(inputs)]
            args = [self._program_path, prog_args]

            # create runner
            runner = Runner(args, self.timeout)
            # connect it
            runner.log_event.connect(self.logger.log_event)
            # run it
            runner.run()
            # kill it
            del runner
            # update progress
            self.progress_update.emit(i)
        self.progress_update.emit(self.iterations)
        self.logger.log_event("Fuzzer complete.", True)

    def event_slot(self, ts, event):
        """Captures an event signal and handles it by passing it upwards"""
        #print("Caught event")
        self.event_logged.emit(ts, event)

if __name__ == "__main__":
    a = OperationHandler("test/inputfile.py", "test/program.py")
