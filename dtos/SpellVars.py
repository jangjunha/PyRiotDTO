class SpellVars(object):
    """ SpellVars DTO object

    Attributes:
        link (string): 
        coeff (List[double]): 
        ranksWith (string): 
        dyn (string): 
        key (string): 
    """

    def __init__(self, link, coeff, ranksWith, dyn, key):
        self.link = link
        self.coeff = coeff
        self.ranksWith = ranksWith
        self.dyn = dyn
        self.key = key
