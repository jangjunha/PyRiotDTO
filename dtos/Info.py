class Info(object):
    """ Info DTO object

    Attributes:
        difficulty (int): 
        attack (int): 
        defense (int): 
        magic (int): 
    """

    def __init__(self, difficulty, attack, defense, magic):
        self.difficulty = difficulty
        self.attack = attack
        self.defense = defense
        self.magic = magic
