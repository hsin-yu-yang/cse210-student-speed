from game.actor import Actor
from game.point import Point

class WordCount(Actor):
    """ Display how many words the player has typed correctly
    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (WordCount): an instance of WordCount.
        """
        super().__init__()
        self._word_count = 0
        position = Point(42, 0)
        self.set_position(position)
        self.set_text(f"Word Count: {self._word_count}")
    
    def add_points(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (WordCount): An instance of WordCount.
            points (integer): The points to add.
        """
        self._word_count += points
        self.set_text(f"Word Count: {self._word_count}")