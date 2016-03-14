class Champion(object):
    """ Champion DTO object

    Attributes:
        rankedPlayEnabled (boolean): Ranked play enabled flag.
        botEnabled (boolean): Bot enabled flag (for custom games).
        botMmEnabled (boolean): Bot Match Made enabled flag (for Co-op vs. AI games).
        active (boolean): Indicates if the champion is active.
        freeToPlay (boolean): Indicates if the champion is free to play. Free to play champions are rotated periodically.
        id (long): Champion ID. For static information correlating to champion IDs, please refer to the LoL Static Data API.
    """

    def __init__(self, rankedPlayEnabled, botEnabled, botMmEnabled, active, freeToPlay, id):
        self.rankedPlayEnabled = rankedPlayEnabled
        self.botEnabled = botEnabled
        self.botMmEnabled = botMmEnabled
        self.active = active
        self.freeToPlay = freeToPlay
        self.id = id
