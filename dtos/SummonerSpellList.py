class SummonerSpellList(object):
    """ SummonerSpellList DTO object

    Attributes:
        data (Map[string, SummonerSpell]): 
        version (string): 
        type (string): 
    """

    def __init__(self, data, version, type):
        self.data = data
        self.version = version
        self.type = type
