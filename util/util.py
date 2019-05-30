from dataclasses import dataclass
"""
    Config dataclass
    Contains all the config data sent from the GUI to the actual
    functional parts of the program
"""
@dataclass
class ConfigData:
    iterations: int
    verbose: bool
    timeout: int