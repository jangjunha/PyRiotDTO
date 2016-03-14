class Block(object):
    """ Block DTO object

    Attributes:
        items (List[BlockItem]): 
        recMath (boolean): 
        type (string): 
    """

    def __init__(self, items, recMath, type):
        self.items = items
        self.recMath = recMath
        self.type = type
