class MasteryPages(object):
    """ MasteryPages DTO object

    Attributes:
        pages (Set[MasteryPage]): Collection of mastery pages associated with the summoner.
        summonerId (long): Summoner ID.
    """

    def __init__(self, pages, summonerId):
        self.pages = pages
        self.summonerId = summonerId
