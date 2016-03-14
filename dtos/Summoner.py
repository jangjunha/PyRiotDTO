class Summoner(object):
    """ Summoner DTO object

    Attributes:
        profileIconId (int): ID of the summoner icon associated with the summoner.
        revisionDate (long): Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
        id (long): Summoner ID.
        name (string): Summoner name.
        summonerLevel (long): Summoner level associated with the summoner.
    """

    def __init__(self, profileIconId, revisionDate, id, name, summonerLevel):
        self.profileIconId = profileIconId
        self.revisionDate = revisionDate
        self.id = id
        self.name = name
        self.summonerLevel = summonerLevel
