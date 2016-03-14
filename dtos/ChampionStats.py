class ChampionStats(object):
    """ ChampionStats DTO object

    Attributes:
        stats (AggregatedStats): Aggregated stats associated with the champion.
        id (int): Champion ID. Note that champion ID 0 represents the combined stats for all champions. For static information correlating to champion IDs, please refer to the LoL Static Data API.
    """

    def __init__(self, stats, id):
        self.stats = stats
        self.id = id
