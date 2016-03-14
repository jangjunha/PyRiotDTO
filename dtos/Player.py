class Player(object):
    """ Player DTO object

    Attributes:
        teamId (int): Team id associated with player.
        championId (int): Champion id associated with player.
        summonerId (long): Summoner id associated with player.
    """

    def __init__(self, teamId, championId, summonerId):
        self.teamId = teamId
        self.championId = championId
        self.summonerId = summonerId
