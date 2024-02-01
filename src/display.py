from pygame import *


_display = display
_display.init()
font.init()
mixer.init()


class display:
    surface: Surface

    def create():
        display.surface = _display.set_mode((0, 0), HWACCEL|HWPALETTE|HWSURFACE|DOUBLEBUF|FULLSCREEN)
    
    def get_size():
        return Vector2(_display.get_window_size())
    
    def get_surface():
        return display.surface
    
    def flip():
        _display.flip()
