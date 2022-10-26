class Director:

    def __init__(self, video_service):
        self._video_service = video_service
        self.tick = 1
        
    #Starts and loops the game until the window is closed
    def start_game(self, cast, script):
        self._video_service.open_window()
        self._video_service._draw_grid()
        while self._video_service.is_window_open():
            self.tick += 1
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
            if self.tick == 10:
                self.tick = 1
        self._video_service.close_window()

    #uns through the actions it set up
    def _execute_actions(self, group, cast, script):
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script, self.tick)          