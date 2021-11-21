
   
from game.actor import Actor
from game.point import Point


class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self.set_position(Point(1, 20))
    
    def add_letter(self, new_letter):
        new_text = self.get_text() + new_letter
        self.set_text(new_text)

    def display_text(self):
        return "Buffer: " + self.get_text()

    def clear_letters(self):
        self.set_text("")