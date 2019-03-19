"""Mutator takes care of mutating the program inputs. """
import random


class Mutator:
    def __init__(self, initial_input, number_of_mutations=10):
        self._initial_input = initial_input
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
    mutator = Mutator("abcdefg")

    for i in range(10):
        print(mutator.mutate())
