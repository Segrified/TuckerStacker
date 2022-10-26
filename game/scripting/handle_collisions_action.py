import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.tower import Tower
from game.shared.color import Color

#Determines what happens on collision
class HandleCollisionsAction(Action):

    def __init__(self):
        self._is_game_over = False

    #Runs the parts of cycle control
    def execute(self, cast, script, tick):
        self._handle_cycle_growth(cast)
        self._handle_segment_collision(cast)
        self._handle_game_over(cast)

    #Grows the cycles
    def _handle_cycle_growth(self, cast):
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_segments()[0]

        cast.add_actor("tower", Tower(Color(0, 255, 0), head._position.get_x(), head._position.get_y()))
        head.set_position(Point(8, head._position.get_y() - 40))
    
    #Determines when a collision takes place
    def _handle_segment_collision(self, cast):
        cycle = cast.get_first_actor("cycles")
        stack = cast.get_first_actor("tower")
        head = cycle.get_segments()[0]
        #segments = stack.get_segments()[1:]

        #cycle2 = cast.get_second_actor("cycles")
        #head2 = cycle2.get_segments()[0]
        #segments2 = cycle2.get_segments()[1:]

        if head._position.get_x() == stack._position.get_x() or head._position.get_y() == 762:
            return 1
        else:
            return 0
        
        """for segment in segments:
            if head.get_x().equals(stack.get_x()):
                x = 0"""
                
            #if head2.get_position().equals(segment.get_position()):
                #self._is_game_over = True
        
        #for segment in segments2:
            #if head.get_position().equals(segment.get_position()):
                #self._is_game_over = True

            #if head2.get_position().equals(segment.get_position()):
                #self._is_game_over = True
        
    #Changes the cycles when the game ends and displays the game over message
    def _handle_game_over(self, cast):
        if self._is_game_over:
            cycle= cast.get_first_actor("cycles")
            #cycle2 = cast.get_second_actor("cycles")
            
            segments = cycle.get_segments()
            #segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)

            #for segment in segments2:
                #segment.set_color(constants.WHITE)