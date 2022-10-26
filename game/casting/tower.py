import constants
from game.casting.actor import Actor
from game.shared.point import Point

#Child of Actor Class, makes an controls a cycle object
class Tower(Actor):

    def __init__(self, color, x, y):
        super().__init__()
        self._segments = []
        self._color = color
        self._position_x = x
        self._position_y = y
        self._prepare()
    
    #Specifies how the cycle should be drawn
    def _prepare(self):
        x = self._position_x
        y = self._position_y

        position = Point(x, y)
        text = "O"
        color = self._color

        self.set_position(position)
        self.set_text(text)
        self.set_color(color)