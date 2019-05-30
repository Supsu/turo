"""Mutator takes care of mutating the program inputs. """
import random
import argparse

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
        """Changes one byte of the data and returns the result.
        Also saves the changed data for possible next iteration."""

        output = list(self._output)
        index = random.randint(0, len(output)-1)
        output[index] = random.randint(0,255)
        self._output = bytearray(output)
        return bytearray(output)

def load_file(path):
    """A helper function that loads given file as bytearray"""
    with open(path, "rb") as f:
        data = f.read()

    return bytearray(data)

if __name__ == "__main__":
    #Command line interface for mutator

    parser = argparse.ArgumentParser(description='Mutator module')
    parser.add_argument('file', type=str,
                        help='File to be mutated')
    parser.add_argument('outfile', type=str,
                        help='Where to save the output')
    parser.add_argument('-N', type=int, default=10,
                        help='Number of mutations')

    args = parser.parse_args()
    img_data = load_file(args.file)

    mutator = Mutator(img_data)
    for i in range(args.N):
        mutator.mutate()
        print(i)

    final_data = mutator.mutate()
    with open(args.outfile, "wb") as f:
        f.write(final_data)
