class RankedStats(object):
    """ RankedStats DTO object

    Attributes:
        modifyDate (long): Date stats were last modified specified as epoch milliseconds.
        champions (List[ChampionStats]): Collection of aggregated stats summarized by champion.
        summonerId (long): Summoner ID.
    """

    def __init__(self, modifyDate, champions, summonerId):
        self.modifyDate = modifyDate
        self.champions = champions
        self.summonerId = summonerId
