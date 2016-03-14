class MatchHistorySummary(object):
    """ MatchHistorySummary DTO object

    Attributes:
        opposingTeamName (string): 
        opposingTeamKills (int): 
        gameId (long): 
        kills (int): 
        deaths (int): 
        win (boolean): 
        gameMode (string): 
        mapId (int): 
        invalid (boolean): 
        assists (int): 
        date (long): Date that match was completed specified as epoch milliseconds.
    """

    def __init__(self, opposingTeamName, opposingTeamKills, gameId, kills, deaths, win, gameMode, mapId, invalid, assists, date):
        self.opposingTeamName = opposingTeamName
        self.opposingTeamKills = opposingTeamKills
        self.gameId = gameId
        self.kills = kills
        self.deaths = deaths
        self.win = win
        self.gameMode = gameMode
        self.mapId = mapId
        self.invalid = invalid
        self.assists = assists
        self.date = date
