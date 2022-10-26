from game.scripting.action import Action

#Draws everything on the screen
class DrawActorsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    #Gets what it needs, then draws them
    def execute(self, cast, script, tick):
        cycle = cast.get_first_actor("cycles")
        tower = cast.get_actors("tower")
        segments = cycle.get_segments()

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(tower)
        self._video_service._draw_grid()
        self._video_service.flush_buffer()