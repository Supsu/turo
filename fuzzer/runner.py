"""
Runner module to define Runner class for subprocess handling.
"""

import subprocess

debug = False

class Runner:
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
        self.args = args
        self.time = time
        self.log = []

    def log(self):
        """Log method to handle sending logs upwards

        Log method is used to send the Runner objects internal
        log list to the logger in case there are things to report.

        Note:
            [NYI] Sending to logger module

        Returns:
            int: If the log was empty, return 0. Otherwise, return 1

        """
        if size(self.log)==0:
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
            completed = subprocess.run( self.args, #pass arguments
                                        capture_output=True, #get output
                                        check=True, #exception if non-0 exit
                                        timeout=self.time
                                        )

        except subprocess.CalledProcessError as e:
            self.log.append("[NON-0]: " + str(e))

        except subprocess.TimeoutExpire as e:
            self.log.append("[TO]: " + str(e))

        except subprocess.SubprocessError as e:
            self.log.append("[SUB]: " + str(e))

        except Exception as e:
            self.log.append("[OTHER]: " + str(e))

        finally:
            if debug == True:
                print(self.log)
            self.logstate = self.log()
            return self.logstate

#If runned as main for testing purposes
if __name__ == "__main__":
    debug = True
    testargs = ["./test", "arg1", "arg2"]
    testrunner = Runner(testargs)
