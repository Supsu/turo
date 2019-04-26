"""Mutator takes care of mutating the program inputs. """
import random

class Mutator:
    def __init__(self, initial_input, number_of_mutations=10):

        try:
            self._initial_input = bytearray(initial_input, "utf-8")
        except TypeError:
            self._initial_input = initial_input

        

        if type(self._initial_input) is not bytearray:
            raise TypeError("Mutator expected a bytearray or a string")

        self._number_of_mutations = number_of_mutations
        self._mutated = 0
        self._output = self._initial_input

    def mutate(self):
        output = list(self._output)
        output[random.randint(0, len(output)-1)] = random.choice(["1", "0"])
        output = "".join(output)
        self._output = output
        return output

if __name__ == "__main__":
    mutator = Mutator(66)

    for i in range(10):
        print(mutator.mutate())
