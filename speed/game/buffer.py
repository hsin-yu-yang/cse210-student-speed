import random
from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """Displaying user input. The responsibility of Buffer is to keep track of the player's typed letters.
    
    Stereotype:
        Information Holder
        
    Attributes: 
        _baseline (str): label to define where the user is typing
        _contents (str): what the user has typed thus far
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        Args:
            self (Buffer): an instance of Buffer.
        """
        super().__init__()
        self._text = ' '
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self._baseline = "Buffer: "
        self._contents = ""
        self._update_text()
    
    def add_letter(self, letter):
        """Adds the given inputs to the running buffer and updates the text.
        Args:
            self (Buffer): An instance of Buffer.
            letter (str): The letter from input that the user has typed
        """
        self._contents += letter
        self._update_text()

    def _update_text(self):
        self.set_text(self._baseline + " " + self._contents)

    def get_contents(self):
        """ Returns the current contents of the buffer
        Args:
            self (Buffer): An instance of Buffer.
        """
        return self._contents

    def clear(self):
        """ Clears the current contents of the buffer
        Args:
            self (Buffer): An instance of Buffer.
        """
        self._contents = ""
        self._update_text()