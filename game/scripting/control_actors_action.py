import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.handle_collisions_action import HandleCollisionsAction

#Class for controlling the cycles
class ControlActorsAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._status_check = HandleCollisionsAction()
        self._direction = Point(0, constants.CELL_SIZE)
        self._game_begin = 0
        self._key_switch = 0

    #Controls the cycles based on input
    def execute(self, cast, script, tick):
        if self._key_switch == 0:
            if self._game_begin == 0:
                if self._keyboard_service.is_key_down('s'):
                    self._direction = Point(constants.CELL_SIZE, 0)
                    self._game_begin = 1
                    self._key_switch = 1
                cycle = cast.get_first_actor("cycles")
                cycle.turn_head(self._direction)
        
        if self._key_switch == 0:    
            if self._game_begin == 1:
                if self._keyboard_service.is_key_down('s'):
                    self.result = self._status_check._handle_segment_collision(cast)
                    self._key_switch = 1

                    if self.result == 1:
                        self._status_check._handle_cycle_growth(cast)
                cycle = cast.get_first_actor("cycles")
                cycle.turn_head(self._direction)

        if tick == 10:
            if self._keyboard_service.is_key_up('s'):
                self._key_switch = 0