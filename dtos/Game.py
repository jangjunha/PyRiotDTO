class Game(object):
    """ Game DTO object

    Attributes:
        gameId (long): Game ID.
        fellowPlayers (List[Player]): Other players associated with the game.
        level (int): Level.
        createDate (long): Date that end game data was recorded, specified as epoch milliseconds.
        gameMode (string): Game mode. (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
        mapId (int): Map ID.
        invalid (boolean): Invalid flag.
        subType (string): Game sub-type. (Legal values: NONE, NORMAL, BOT, RANKED_SOLO_5x5, RANKED_PREMADE_3x3, RANKED_PREMADE_5x5, ODIN_UNRANKED, RANKED_TEAM_3x3, RANKED_TEAM_5x5, NORMAL_3x3, BOT_3x3, CAP_5x5, ARAM_UNRANKED_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF, URF_BOT, NIGHTMARE_BOT, ASCENSION, HEXAKILL, KING_PORO, COUNTER_PICK, BILGEWATER)
        teamId (int): Team ID associated with game. Team ID 100 is blue team. Team ID 200 is purple team.
        gameType (string): Game type. (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
        ipEarned (int): IP Earned.
        championId (int): Champion ID associated with game.
        spell1 (int): ID of first summoner spell.
        spell2 (int): ID of second summoner spell.
        stats (RawStats): Statistics associated with the game for this summoner.
    """

    def __init__(self, gameId, fellowPlayers, level, createDate, gameMode, mapId, invalid, subType, teamId, gameType, ipEarned, championId, spell1, spell2, stats):
        self.gameId = gameId
        self.fellowPlayers = fellowPlayers
        self.level = level
        self.createDate = createDate
        self.gameMode = gameMode
        self.mapId = mapId
        self.invalid = invalid
        self.subType = subType
        self.teamId = teamId
        self.gameType = gameType
        self.ipEarned = ipEarned
        self.championId = championId
        self.spell1 = spell1
        self.spell2 = spell2
        self.stats = stats
