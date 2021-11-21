from os import remove
from time import sleep
from game import constants
from game.word import Word
from game.buffer import Buffer
from game.score import Score
from game.word_count import WordCount
from game.explosion import Explosion

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        _words (list)                   : a list of Word(Actor) objects
        _explosions (list)              : a list of Explosion(Actor) objects
        _input_service (InputService)   : The input mechanism
        output_service (OutputService)  : the output mechanism
        _keep_playing (boolean)         : continue playing while True
        _score (Score)                  : an instance of Score(Actor)
        _buffer (Buffer)                : an instance of Buffer(Actor)
        _letter (STR)                   : a letter
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

        self._words = []
        for i in range(0, constants.STARTING_WORDS):
            word = Word()
            word.get_points
            self._words.append(word)
            word.randomize_x()

        self._explosions = []

        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        self._word_count = WordCount()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.
            > gets the letter from input service
            > updates the buffer
            > processes the buffer contents if user presses Enter
        Args:
            self (Director): An instance of Director.
        """
        self._letter = self._input_service.get_letter()

        #  if player presses Enter
        if self._letter == "*":
            buffer_contents = self._buffer.get_contents()
            self._letter = ''
            self._buffer.clear()
            self._process_buffer(buffer_contents)


    def _process_buffer(self, buffer_contents):
        """ Check the buffer contents against the text of the words,
        
        Args:
            self (Director):        An instance of Director.
            buffer_contents (STR):  the text in the buffer
        """
        for word in self._words:
            word_contents = word.get_text()

            if buffer_contents.lower() == word_contents.lower():                
                # add points
                score = word.get_points()
                self._score.add_points(score)
                self._word_count.add_points(1)

                # create explosion here
                explosion = Explosion(word)
                self._explosions.append(explosion)

                # reset
                word.reset()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.
        Args:
            self (Director): An instance of Director.
        """
        self._buffer.add_letter(self._letter)

        # move words to the right
        for word in self._words:
            word.move_word()
        
        # reset words that leave the edge of the screen
        for word in self._words:
            position = word.get_position()
            x = position.get_x()
            if x >= constants.MAX_X:
                word.reset()

        # updates for explosions
        for explosion in self._explosions:
            explosion.flicker()
            # remove explosions that are out of frames
            if explosion.frames_left == 0:
                self._explosions.remove(explosion)
        
    def _do_outputs(self):
        """ Clears the screen, draws the actors, and flushes the buffer
        Args:
            self (Director): An instance of Director.
        """

        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words)
        self._output_service.draw_actors(self._explosions)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._word_count)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()