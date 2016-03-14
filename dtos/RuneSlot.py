class RuneSlot(object):
    """ RuneSlot DTO object

    Attributes:
        runeId (int): Rune ID associated with the rune slot. For static information correlating to rune IDs, please refer to the LoL Static Data API.
        runeSlotId (int): Rune slot ID.
    """

    def __init__(self, runeId, runeSlotId):
        self.runeId = runeId
        self.runeSlotId = runeSlotId
