import subprocess

"""
Runner class to handle subprocesses

Runner objects are designed to run the tested program one time,
capture the possible error and log it. To use the class,
create a Runner object with init parameters that contain
at least args[]. The first arg is supposed to be the path
to testable program.
"""
class Runner:
    def __init__(self, args, time=1000):
        self.args = args
        self.time = time
        self.log = []

    def log(self):
        if size(self.log)==0:
            return 0
        else:
            #TODO: send log to logger (qt signal?)
            return 1

    def run(self):
        # suorita aliprosessi
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
            self.logstate = self.log()
            return self.logstate
