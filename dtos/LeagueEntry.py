class LeagueEntry(object):
    """ LeagueEntry DTO object

    Attributes:
        isFreshBlood (boolean): Specifies if the participant is fresh blood.
        division (string): The league division of the participant.
        isVeteran (boolean): Specifies if the participant is a veteran.
        miniSeries (MiniSeries): Mini series data for the participant. Only present if the participant is currently in a mini series.
        wins (int): The number of wins for the participant.
        losses (int): The number of losses for the participant.
        playerOrTeamId (string): The ID of the participant (i.e., summoner or team) represented by this entry.
        playerOrTeamName (string): The name of the the participant (i.e., summoner or team) represented by this entry.
        isInactive (boolean): Specifies if the participant is inactive.
        isHotStreak (boolean): Specifies if the participant is on a hot streak.
        leaguePoints (int): The league points of the participant.
    """

    def __init__(self, isFreshBlood, division, isVeteran, miniSeries, wins, losses, playerOrTeamId, playerOrTeamName, isInactive, isHotStreak, leaguePoints):
        self.isFreshBlood = isFreshBlood
        self.division = division
        self.isVeteran = isVeteran
        self.miniSeries = miniSeries
        self.wins = wins
        self.losses = losses
        self.playerOrTeamId = playerOrTeamId
        self.playerOrTeamName = playerOrTeamName
        self.isInactive = isInactive
        self.isHotStreak = isHotStreak
        self.leaguePoints = leaguePoints
