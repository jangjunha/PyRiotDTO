class RuneList(object):
    """ RuneList DTO object

    Attributes:
        data (Map[string, Rune]): 
        version (string): 
        type (string): 
        basic (BasicData): 
    """

    def __init__(self, data, version, type, basic):
        self.data = data
        self.version = version
        self.type = type
        self.basic = basic
