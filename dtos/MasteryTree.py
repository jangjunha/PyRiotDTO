class MasteryTree(object):
    """ MasteryTree DTO object

    Attributes:
        Resolve (List[MasteryTreeList]): 
        Ferocity (List[MasteryTreeList]): 
        Cunning (List[MasteryTreeList]): 
    """

    def __init__(self, Resolve, Ferocity, Cunning):
        self.Resolve = Resolve
        self.Ferocity = Ferocity
        self.Cunning = Cunning
