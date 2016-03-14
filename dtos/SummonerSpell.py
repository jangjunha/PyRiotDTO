class SummonerSpell(object):
    """ SummonerSpell DTO object

    Attributes:
        vars (List[SpellVars]): 
        image (Image): 
        costBurn (string): 
        cost (List[int]): 
        effectBurn (List[string]): 
        id (int): 
        cooldownBurn (string): 
        tooltip (string): 
        maxrank (int): 
        rangeBurn (string): 
        description (string): 
        effect (List[object]): This field is a List of List of Double.
        key (string): 
        leveltip (LevelTip): 
        name (string): 
        resource (string): 
        modes (List[string]): 
        costType (string): 
        sanitizedDescription (string): 
        sanitizedTooltip (string): 
        range (object): This field is either a List of Integer or the String 'self' for spells that target one's own champion.
        cooldown (List[double]): 
        summonerLevel (int): 
    """

    def __init__(self, vars, image, costBurn, cost, effectBurn, id, cooldownBurn, tooltip, maxrank, rangeBurn, description, effect, key, leveltip, name, resource, modes, costType, sanitizedDescription, sanitizedTooltip, range, cooldown, summonerLevel):
        self.vars = vars
        self.image = image
        self.costBurn = costBurn
        self.cost = cost
        self.effectBurn = effectBurn
        self.id = id
        self.cooldownBurn = cooldownBurn
        self.tooltip = tooltip
        self.maxrank = maxrank
        self.rangeBurn = rangeBurn
        self.description = description
        self.effect = effect
        self.key = key
        self.leveltip = leveltip
        self.name = name
        self.resource = resource
        self.modes = modes
        self.costType = costType
        self.sanitizedDescription = sanitizedDescription
        self.sanitizedTooltip = sanitizedTooltip
        self.range = range
        self.cooldown = cooldown
        self.summonerLevel = summonerLevel
