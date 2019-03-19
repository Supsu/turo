####################################
# Runner module for turo
#
# This module is used for single iteration of the software.
# It keeps track of state of the run and in the end of iteration
# passes loggable information to logger module.
####################################

import subprocess

#TODO: state
#TODO: init
#TODO: subprocess
#TODO: run
#TODO: log

STATES = ["waiting", "running", "finished"]

"""
kommentoi tähä homo
"""
class Runner:
    def __init__(self):
        # puske ohjelman exec arg0
        # argumentit arg1-n
        # timeout?
        pass

    def logger(self):
        # työnnä sata loggerille
        pass

    def subproc(self):
        # suorita aliprosessi
        try:
            completed = subprocess.run( self.args, #pass arguments
                                        capture_output=True, #get output
                                        check=True, #exception if non-0 exit
                                        timeout=self.time
                                        )
        except subprocess.CalledProcessError:
            #ohjelma poistuu ei-0
            pass

        except subprocess.TimeoutExpire:
            #timeout
            pass

        except subprocess.SubprocessError:
            #fallback muille subprocessin omille exceptioneille
            pass

        except:
            #muut virheet

        finally:
            #mitässit

    self._state = STATES[0]
    self.args = []
    self.time = 0
