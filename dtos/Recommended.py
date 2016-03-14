class Recommended(object):
    """ Recommended DTO object

    Attributes:
        map (string): 
        blocks (List[Block]): 
        champion (string): 
        title (string): 
        priority (boolean): 
        mode (string): 
        type (string): 
    """

    def __init__(self, map, blocks, champion, title, priority, mode, type):
        self.map = map
        self.blocks = blocks
        self.champion = champion
        self.title = title
        self.priority = priority
        self.mode = mode
        self.type = type
