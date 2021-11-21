import os

MAX_X = 60
MAX_Y = 40
FRAME_LENGTH = 0.2
MIN_WORD_SPEED = 1
MAX_WORD_SPEED = 2
FRAME_LENGTH = 0.1
STARTING_WORDS = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
