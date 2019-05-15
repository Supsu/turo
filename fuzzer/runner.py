"""
Runner module to define Runner class for subprocess handling.
"""

import subprocess
from PyQt5.QtCore import QObject, pyqtSignal

DEBUG = False

class Runner(QObject):
    log_event = pyqtSignal(str) # Can be used to send log events with log_event.emit("event here")
    """Runner class to handle subprocesses

    Runner objects are designed to run the tested program one time,
    capture the possible error and log it. To use the class,
    create a Runner object with init parameters that contain
    at least args[]. The first arg is supposed to be the path
    to testable program.

    Args:
        args (list): A list containing the program to run and it's arguments.
        time (int): Time in ms that is used for timeouts. Default 1000.

    Attributes:
        args (list): A list containing the program to run and it's arguments.
        time (int): Time in ms that is used for timeouts. Default 1000.
        log (list of str): List of (one) str to be added to global log.

    """
    def __init__(self, args, time=1000):
        super(Runner, self).__init__()
        self.args = args
        self.time = time
        self.log = []
        self.completed = "No program was run or exception was raised!\n"

    def logger(self):
        """Log method to handle sending logs upwards

        Log method is used to send the Runner objects internal
        log list to the logger in case there are things to report.

        Note:
            [NYI] Sending to logger module

        Returns:
            int: If the log was empty, return 0. Otherwise, return 1

        """
        if len(self.log)==0:
            return 0
        else:
            #TODO: send log to logger (qt signal?)
            return 1

    def run(self):
        """Run method to handle starting subprocess

        This method starts the subprocess and handles exceptions
        related to it. If exceptions are raised, it adds a string to
        log list, which is tagged either [NON-0] if the program
        exited with return value other than 0, [TO] if it encountered timeout,
        [SUB] if it was some other exception raised by subprocess class,
        or [OTHER] if it was some exception not related to subprocess. Every
        error log append should include exception message string.

        Note:
            It should be checked if there are any more exceptions that should be
            handled here.

        Returns:
            int: Returns either 1 or 0, defined by log(), depending on whether
            there was a exception or not.

        """
        try:
            self.completed = subprocess.run( self.args, #pass arguments
                                        capture_output=True, #get output
                                        check=True, #exception if non-0 exit
                                        timeout=self.time
                                        )

        except subprocess.CalledProcessError as e:
            print("Child output:" + str(e.output))
            self.log.append("[NON-0]: " + str(e))

        except subprocess.TimeoutExpired as e:
            self.log.append("[TO]: " + str(e))

        except subprocess.SubprocessError as e:
            self.log.append("[SUB]: " + str(e))

        except Exception as e:
            self.log.append("[OTHER]: " + str(e))

        finally:
            if DEBUG:
                print("log:")
                print(self.log)
                if (isinstance(self.completed, str)):
                    print(self.completed)
                else:
                    print("returncode:" + str(self.completed.returncode))
                    print("args: " + str(self.completed.args))
                    print("stdout: " + str(self.completed.stdout))
                    print("stderr: " + str(self.completed.stderr))
            return self.logger()

#If runned as main for testing purposes
if __name__ == "__main__":
    print("Running runner module testing..")
    DEBUG = True
    #TODO: insert dummy testing software when available
    TESTARGS = ["python3.7", "../tests/dummyrun.py", "1"]
    TESTTIME = 1000
    TESTRUNNER = Runner(TESTARGS, TESTTIME)
    TESTRUNNER.run()
