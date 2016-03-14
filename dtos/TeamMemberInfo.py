class TeamMemberInfo(object):
    """ TeamMemberInfo DTO object

    Attributes:
        playerId (long): 
        status (string): 
        joinDate (long): Date that team member joined team specified as epoch milliseconds.
        inviteDate (long): Date that team member was invited to team specified as epoch milliseconds.
    """

    def __init__(self, playerId, status, joinDate, inviteDate):
        self.playerId = playerId
        self.status = status
        self.joinDate = joinDate
        self.inviteDate = inviteDate
