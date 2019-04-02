from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from datetime import datetime
import time

class Logger(QObject):

    event_logged = pyqtSignal(int, str)
    """
    program_name is the name of the program being run. The logger bases the log file name on that.
    verbose is a Bool value that controls the flood of log info into the GUI. Everything is logged 
    the file regardless though. For the time being the file is simply program_name.log in parent directory.

    event_logged is the signal that is emitted and it sends the timestamp as int and event as str
    """
    def __init__(self, program_name, verbose):
        super(Logger, self).__init__()
        self.verbose = verbose
        self.filename = str(program_name) + ".log"

    """
    Takes the log event in as event and pushes it into the log file. If priority is True then it'll also emit a signal of the 
    log event regardless of whether verbose is True or False.
    """
    def log_event(self, event, priority):
        # Input checks
        if not isinstance(event, str):
            event = "Invalid event string"
        if not isinstance(priority, bool):
            priority = False

        # Get current timestamp
        dt = datetime.now()
        epoch = int(time.mktime(dt.timetuple()))

        eventstring = "[" + datetime.fromtimestamp(epoch).strftime('%H:%M:%S') + "]: " + event

        # Write into the file
        f = open(self.filename, "a")
        f.write(eventstring)
        f.close()

        # send signal of the message being logged
        if priority or self.verbose:
            self.event_logged.emit(epoch, event)

    def test_slot(self, ts, event):
        print("[" + datetime.fromtimestamp(ts).strftime('%H:%M:%S') + "]: " + event)

if __name__ == "__main__":
    a = Logger("test", True)
    a.event_logged.connect(a.test_slot)
    a.log_event("Stuff happened\n", True)