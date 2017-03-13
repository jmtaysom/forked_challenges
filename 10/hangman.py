from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.word = word
        self.graphics_gen = hang_graphics()
        self.graphics = next(self.graphics_gen)
        self.show = ''.join('_' if letter in ASCII else ' ' for letter in self.word )
        print(self.graphics, '\n')
        print(self.show)


# or use functions ...


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print(word)
    Hangman(word)
    # init / call program
