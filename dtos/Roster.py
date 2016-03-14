class Roster(object):
    """ Roster DTO object

    Attributes:
        memberList (List[TeamMemberInfo]): 
        ownerId (long): 
    """

    def __init__(self, memberList, ownerId):
        self.memberList = memberList
        self.ownerId = ownerId
