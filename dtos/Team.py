class Team(object):
    """ Team DTO object

    Attributes:
        status (string): 
        modifyDate (long): Date that team was last modified specified as epoch milliseconds.
        name (string): 
        roster (Roster): 
        createDate (long): Date that team was created specified as epoch milliseconds.
        fullId (string): 
        lastGameDate (long): Date that last game played by team ended specified as epoch milliseconds.
        lastJoinDate (long): Date that last member joined specified as epoch milliseconds.
        tag (string): 
        thirdLastJoinDate (long): Date that third to last member joined specified as epoch milliseconds.
        teamStatDetails (List[TeamStatDetail]): 
        lastJoinedRankedTeamQueueDate (long): Date that team last joined the ranked team queue specified as epoch milliseconds.
        matchHistory (List[MatchHistorySummary]): 
        secondLastJoinDate (long): Date that second to last member joined specified as epoch milliseconds.
    """

    def __init__(self, status, modifyDate, name, roster, createDate, fullId, lastGameDate, lastJoinDate, tag, thirdLastJoinDate, teamStatDetails, lastJoinedRankedTeamQueueDate, matchHistory, secondLastJoinDate):
        self.status = status
        self.modifyDate = modifyDate
        self.name = name
        self.roster = roster
        self.createDate = createDate
        self.fullId = fullId
        self.lastGameDate = lastGameDate
        self.lastJoinDate = lastJoinDate
        self.tag = tag
        self.thirdLastJoinDate = thirdLastJoinDate
        self.teamStatDetails = teamStatDetails
        self.lastJoinedRankedTeamQueueDate = lastJoinedRankedTeamQueueDate
        self.matchHistory = matchHistory
        self.secondLastJoinDate = secondLastJoinDate
