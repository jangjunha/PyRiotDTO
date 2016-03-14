class MasteryTreeItem(object):
    """ MasteryTreeItem DTO object

    Attributes:
        masteryId (int): 
        prereq (string): 
    """

    def __init__(self, masteryId, prereq):
        self.masteryId = masteryId
        self.prereq = prereq
