class PlayerStatsSummaryList(object):
    """ PlayerStatsSummaryList DTO object

    Attributes:
        playerStatSummaries (List[PlayerStatsSummary]): Collection of player stats summaries associated with the summoner.
        summonerId (long): Summoner ID.
    """

    def __init__(self, playerStatSummaries, summonerId):
        self.playerStatSummaries = playerStatSummaries
        self.summonerId = summonerId
