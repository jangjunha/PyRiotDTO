class MapData(object):
    """ MapData DTO object

    Attributes:
        data (Map[string, MapDetails]): 
        version (string): 
        type (string): 
    """

    def __init__(self, data, version, type):
        self.data = data
        self.version = version
        self.type = type
