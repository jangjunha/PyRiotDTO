class RunePages(object):
    """ RunePages DTO object

    Attributes:
        pages (Set[RunePage]): Collection of rune pages associated with the summoner.
        summonerId (long): Summoner ID.
    """

    def __init__(self, pages, summonerId):
        self.pages = pages
        self.summonerId = summonerId
