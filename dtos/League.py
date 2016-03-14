class League(object):
    """ League DTO object

    Attributes:
        queue (string): The league's queue type. (Legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)
        tier (string): The league's tier. (Legal values: CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)
        entries (List[LeagueEntry]): The requested league entries.
        participantId (string): Specifies the relevant participant that is a member of this league (i.e., a requested summoner ID, a requested team ID, or the ID of a team to which one of the requested summoners belongs). Only present when full league is requested so that participant's entry can be identified. Not present when individual entry is requested.
        name (string): This name is an internal place-holder name only. Display and localization of names in the game client are handled client-side.
    """

    def __init__(self, queue, tier, entries, participantId, name):
        self.queue = queue
        self.tier = tier
        self.entries = entries
        self.participantId = participantId
        self.name = name
