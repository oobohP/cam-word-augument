# article of what this does in general here
# https://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/
from random import shuffle
import re
import argparse
from Tkinter import Tk


RE_GARBLE = re.compile(r"\b(\w)(\w+)(\w)\b")


def garble_word(match):
    # shuffles everything in the middle except the first and last letters

    first, middle, last = match.groups()

    middle = list(middle)
    shuffle(middle)

    return first + ''.join(middle) + last


def garble(sentence):
    # takes in a string sentence and randomizes characters in between

    return RE_GARBLE.sub(garble_word, sentence)


if __name__ == "__main__":
    """ when run the program will randomize the string from the command line.
    Then will copy to the system clipboard automatically"""

    parser = argparse.ArgumentParser(description='aggregating a string')
    parser.add_argument('string', nargs='+', help='enter a string')
    args = parser.parse_args()
    arg_str = ' '.join(args.string)
    print garble(arg_str)

    board = Tk()
    board.withdraw()
    board.clipboard_clear
    board.clipboard_append(garble(arg_str))
    board.update()
    board.destroy()
