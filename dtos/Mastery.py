class Mastery(object):
    """ Mastery DTO object

    Attributes:
        prereq (string): 
        masteryTree (string): Legal values: Cunning, Ferocity, Resolve
        description (List[string]): 
        ranks (int): 
        image (Image): 
        sanitizedDescription (List[string]): 
        id (int): 
        name (string): 
    """

    def __init__(self, prereq, masteryTree, description, ranks, image, sanitizedDescription, id, name):
        self.prereq = prereq
        self.masteryTree = masteryTree
        self.description = description
        self.ranks = ranks
        self.image = image
        self.sanitizedDescription = sanitizedDescription
        self.id = id
        self.name = name
