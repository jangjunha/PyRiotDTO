class MasteryPage(object):
    """ MasteryPage DTO object

    Attributes:
        current (boolean): Indicates if the mastery page is the current mastery page.
        masteries (List[Mastery]): Collection of masteries associated with the mastery page.
        id (long): Mastery page ID.
        name (string): Mastery page name.
    """

    def __init__(self, current, masteries, id, name):
        self.current = current
        self.masteries = masteries
        self.id = id
        self.name = name
