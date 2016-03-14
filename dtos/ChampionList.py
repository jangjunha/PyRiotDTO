class ChampionList(object):
    """ ChampionList DTO object

    Attributes:
        champions (List[Champion]): The collection of champion information.
    """

    def __init__(self, champions):
        self.champions = champions
