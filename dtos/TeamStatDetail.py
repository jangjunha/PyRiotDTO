class TeamStatDetail(object):
    """ TeamStatDetail DTO object

    Attributes:
        wins (int): 
        losses (int): 
        averageGamesPlayed (int): 
        teamStatType (string): 
    """

    def __init__(self, wins, losses, averageGamesPlayed, teamStatType):
        self.wins = wins
        self.losses = losses
        self.averageGamesPlayed = averageGamesPlayed
        self.teamStatType = teamStatType
