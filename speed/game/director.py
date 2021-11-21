from time import sleep
import game.constants as constants
from game.welovejosh import Welovejosh
from game.score import Score
from game.word import Word
from game.buffer import Buffer
from random import choice

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        self._welovejosh = Welovejosh()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._create_new_word()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.
        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self._buffer.add_letter(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.
        Args:
            self (Director): An instance of Director.
        """
        self._check_for_correct_word()
        self._kill_words()
        self._create_new_word()
        # Move everything
        for word in self._welovejosh.get_words():
            word.move_next()

    def example(self):
        # Create new words
        
        pass
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.
        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._welovejosh.get_words())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _check_for_correct_word(self):
        # Check for correct word
        # - A list of all the words

        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.
        Args:
            self (Director): An instance of Director.
        """
        for word in self._welovejosh.get_words():
            if word.get_word() == self._buffer.get_text():
                self._score.add_points(30)
                self._welovejosh.remove_word(word)
                self._create_new_word()
                self._buffer.clear_letters()
        

    def _kill_words(self):
        # Check for words at that never got typed
        # - A list of all the words (positions)
        # - Delete the words at the bottom
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.
        Args:
            self (Director): An instance of Director.
        """
        for word in self._welovejosh.get_words():
            word_position = word.get_position()
            y = word_position.get_y()
            if y == constants.MAX_Y - 1:
                self._welovejosh.remove_word(word)
                self._score.add_points(-5)
                self._create_new_word()

    def _create_new_word(self):
        self._welovejosh.add_word(Word("apple"))
        return
        with open("game/words.txt", "r") as f:
            word_list = f.readlines()
        self._welovejosh.add_word(Word(choice(word_list)))