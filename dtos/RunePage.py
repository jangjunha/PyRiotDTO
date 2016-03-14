class RunePage(object):
    """ RunePage DTO object

    Attributes:
        current (boolean): Indicates if the page is the current page.
        slots (Set[RuneSlot]): Collection of rune slots associated with the rune page.
        id (long): Rune page ID.
        name (string): Rune page name.
    """

    def __init__(self, current, slots, id, name):
        self.current = current
        self.slots = slots
        self.id = id
        self.name = name
