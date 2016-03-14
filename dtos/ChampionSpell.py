class ChampionSpell(object):
    """ ChampionSpell DTO object

    Attributes:
        cooldownBurn (string): 
        resource (string): 
        description (string): 
        vars (List[SpellVars]): 
        costType (string): 
        altimages (List[Image]): 
        sanitizedDescription (string): 
        sanitizedTooltip (string): 
        effect (List[object]): This field is a List of List of Double.
        tooltip (string): 
        maxrank (int): 
        costBurn (string): 
        rangeBurn (string): 
        range (object): This field is either a List of Integer or the String 'self' for spells that target one's own champion.
        cost (List[int]): 
        key (string): 
        effectBurn (List[string]): 
        leveltip (LevelTip): 
        image (Image): 
        cooldown (List[double]): 
        name (string): 
    """

    def __init__(self, cooldownBurn, resource, description, vars, costType, altimages, sanitizedDescription, sanitizedTooltip, effect, tooltip, maxrank, costBurn, rangeBurn, range, cost, key, effectBurn, leveltip, image, cooldown, name):
        self.cooldownBurn = cooldownBurn
        self.resource = resource
        self.description = description
        self.vars = vars
        self.costType = costType
        self.altimages = altimages
        self.sanitizedDescription = sanitizedDescription
        self.sanitizedTooltip = sanitizedTooltip
        self.effect = effect
        self.tooltip = tooltip
        self.maxrank = maxrank
        self.costBurn = costBurn
        self.rangeBurn = rangeBurn
        self.range = range
        self.cost = cost
        self.key = key
        self.effectBurn = effectBurn
        self.leveltip = leveltip
        self.image = image
        self.cooldown = cooldown
        self.name = name
