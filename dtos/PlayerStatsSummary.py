class PlayerStatsSummary(object):
    """ PlayerStatsSummary DTO object

    Attributes:
        wins (int): Number of wins for this queue type.
        aggregatedStats (AggregatedStats): Aggregated stats.
        modifyDate (long): Date stats were last modified specified as epoch milliseconds.
        playerStatSummaryType (string): Player stats summary type. (Legal values: AramUnranked5x5, Ascension, Bilgewater, CAP5x5, CoopVsAI, CoopVsAI3x3, CounterPick, FirstBlood1x1, FirstBlood2x2, Hexakill, KingPoro, NightmareBot, OdinUnranked, OneForAll5x5, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, SummonersRift6x6, Unranked, Unranked3x3, URF, URFBots)
        losses (int): Number of losses for this queue type. Returned for ranked queue types only.
    """

    def __init__(self, wins, aggregatedStats, modifyDate, playerStatSummaryType, losses):
        self.wins = wins
        self.aggregatedStats = aggregatedStats
        self.modifyDate = modifyDate
        self.playerStatSummaryType = playerStatSummaryType
        self.losses = losses
