class MasteryList(object):
    """ MasteryList DTO object

    Attributes:
        data (Map[string, Mastery]): 
        version (string): 
        tree (MasteryTree): 
        type (string): 
    """

    def __init__(self, data, version, tree, type):
        self.data = data
        self.version = version
        self.tree = tree
        self.type = type
