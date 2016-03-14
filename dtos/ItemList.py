class ItemList(object):
    """ ItemList DTO object

    Attributes:
        data (Map[string, Item]): 
        tree (List[ItemTree]): 
        version (string): 
        groups (List[Group]): 
        basic (BasicData): 
        type (string): 
    """

    def __init__(self, data, tree, version, groups, basic, type):
        self.data = data
        self.tree = tree
        self.version = version
        self.groups = groups
        self.basic = basic
        self.type = type
