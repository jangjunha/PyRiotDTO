class Image(object):
    """ Image DTO object

    Attributes:
        full (string): 
        group (string): 
        sprite (string): 
        h (int): 
        w (int): 
        y (int): 
        x (int): 
    """

    def __init__(self, full, group, sprite, h, w, y, x):
        self.full = full
        self.group = group
        self.sprite = sprite
        self.h = h
        self.w = w
        self.y = y
        self.x = x
