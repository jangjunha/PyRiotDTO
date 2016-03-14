class MetaData(object):
    """ MetaData DTO object

    Attributes:
        tier (string): 
        type (string): 
        isRune (boolean): 
    """

    def __init__(self, tier, type, isRune):
        self.tier = tier
        self.type = type
        self.isRune = isRune
