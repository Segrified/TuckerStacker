from game.scripting.action import Action
class MoveActorsAction(Action):

     #Handles cycle movement
     def execute(self, cast, script, tick):
        self.tick = tick

        if self.tick == 2 or self.tick == 4 or self.tick == 6 or self.tick == 8 or self.tick == 10:
            actors = cast.get_all_actors()
            for actor in actors:
                actor.move_next()
        else:
            block = cast.get_first_actor("cycles")
            current = block.get_segments()[0]
            if current._position.get_y() < 362:
                actors = cast.get_all_actors()
                for actor in actors:
                    actor.move_next()



