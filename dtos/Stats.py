class Stats(object):
    """ Stats DTO object

    Attributes:
        armorperlevel (double): 
        hpperlevel (double): 
        attackdamage (double): 
        mpperlevel (double): 
        attackspeedoffset (double): 
        armor (double): 
        hp (double): 
        hpregenperlevel (double): 
        attackspeedperlevel (double): 
        attackrange (double): 
        movespeed (double): 
        attackdamageperlevel (double): 
        mpregenperlevel (double): 
        mp (double): 
        spellblockperlevel (double): 
        crit (double): 
        mpregen (double): 
        spellblock (double): 
        hpregen (double): 
        critperlevel (double): 
    """

    def __init__(self, armorperlevel, hpperlevel, attackdamage, mpperlevel, attackspeedoffset, armor, hp, hpregenperlevel, attackspeedperlevel, attackrange, movespeed, attackdamageperlevel, mpregenperlevel, mp, spellblockperlevel, crit, mpregen, spellblock, hpregen, critperlevel):
        self.armorperlevel = armorperlevel
        self.hpperlevel = hpperlevel
        self.attackdamage = attackdamage
        self.mpperlevel = mpperlevel
        self.attackspeedoffset = attackspeedoffset
        self.armor = armor
        self.hp = hp
        self.hpregenperlevel = hpregenperlevel
        self.attackspeedperlevel = attackspeedperlevel
        self.attackrange = attackrange
        self.movespeed = movespeed
        self.attackdamageperlevel = attackdamageperlevel
        self.mpregenperlevel = mpregenperlevel
        self.mp = mp
        self.spellblockperlevel = spellblockperlevel
        self.crit = crit
        self.mpregen = mpregen
        self.spellblock = spellblock
        self.hpregen = hpregen
        self.critperlevel = critperlevel
