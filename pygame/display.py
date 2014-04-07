from sdl2 import SDL_WasInit
from sdl2 import ext

class Window(object):
    def __init__(self, surface):
        surface.show()
        self.surface = surface
        
    def update(self, rectangle=None):
        self.surface.refresh()
        
    def flip(self):
        self.surface.refresh()
        
    def fill(self, color, rect=None, special_flags=0):
        try:
            color = ext.string_to_color(color)
        except:
            color = ext.convert_to_color(color)
        ext.fill(self.surface.get_surface(), color)
        
def init():
    ext.init()

def quit():
    ext.quit()

def get_init():
    return SDL_WasInit()

def get_surface(surface=False):
    if surface:
        return ext.Window.get_surface(surface)
    else:
        return None
