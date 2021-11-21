from game.actor import Actor

class Explosion(Actor):
    """
    """
    def __init__(self, word):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        Args:
            _length (INT): the length of the string to be displayed
            self (Actor): an instance of Actor.
            word (Word): an instance of Word
        """
        super().__init__()

        position = word.get_position()
        self._length = len(word.get_text())

        self.set_position(position)
        self.set_text("@" * self._length)

        self.frames_left = 6

    def flicker(self):
        """ Creates a flickering explosion text, and counts down the frames to the Explosion's destruction
        """
        self.frames_left = self.frames_left - 1

        if self.frames_left in [1,3,5]:
            self.set_text("#" * self._length)
        elif self.frames_left in [0,2,4]:
            self.set_text("@" * self._length)