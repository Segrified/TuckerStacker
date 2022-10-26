import pyray

#Checks for input
class KeyboardService:

    def __init__(self):
        self._keys = {}
        
        self._keys['s'] = pyray.KEY_S

    #Checks for key release
    def is_key_up(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    #Checks for key press
    def is_key_down(self, key):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)