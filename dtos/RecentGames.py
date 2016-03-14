class RecentGames(object):
    """ RecentGames DTO object

    Attributes:
        games (Set[Game]): Collection of recent games played (max 10).
        summonerId (long): Summoner ID.
    """

    def __init__(self, games, summonerId):
        self.games = games
        self.summonerId = summonerId
