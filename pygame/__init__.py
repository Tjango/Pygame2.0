import pygame.display as _display_
from sdl2 import ext

class Display(object):
    def __init__(self):
        self.window = None

    def set_mode(self, resolution=(0,0), flags=None, depth=None):
        if not flags: flags = None
        self.window = _display_.Window(ext.Window(title='Pygame 2.0',
                                                  size=resolution,
                                                  flags=flags))
        return self.window

    def update(self, rectangle=None):
        if rectangle == None:
            self.window.surface.refresh()
        else:
            rectangle.refresh()
        
    def flip(self):
        ext.Window.refresh(self.window.surface)
        
    def set_caption(self, title='Pygame 2.0'):
        self.window.surface.title = title

def init():
    """Initialize all inits"""
    _display_.init()
    
def quit():
    """Quits all instances"""
    _display_.quit()


display = Display()
