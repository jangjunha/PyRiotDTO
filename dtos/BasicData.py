class BasicData(object):
    """ BasicData DTO object

    Attributes:
        gold (Gold): Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
        plaintext (string): 
        image (Image): 
        inStore (boolean): 
        into (List[string]): 
        id (int): 
        stats (BasicDataStats): 
        from (List[string]): 
        colloq (string): 
        maps (Map[string, boolean]): 
        specialRecipe (int): 
        hideFromAll (boolean): 
        description (string): 
        tags (List[string]): 
        requiredChampion (string): 
        group (string): 
        consumeOnFull (boolean): 
        name (string): 
        consumed (boolean): 
        sanitizedDescription (string): 
        depth (int): 
        rune (MetaData): 
        stacks (int): 
    """

    def __init__(self, gold, plaintext, image, inStore, into, id, stats, from, colloq, maps, specialRecipe, hideFromAll, description, tags, requiredChampion, group, consumeOnFull, name, consumed, sanitizedDescription, depth, rune, stacks):
        self.gold = gold
        self.plaintext = plaintext
        self.image = image
        self.inStore = inStore
        self.into = into
        self.id = id
        self.stats = stats
        self.from = from
        self.colloq = colloq
        self.maps = maps
        self.specialRecipe = specialRecipe
        self.hideFromAll = hideFromAll
        self.description = description
        self.tags = tags
        self.requiredChampion = requiredChampion
        self.group = group
        self.consumeOnFull = consumeOnFull
        self.name = name
        self.consumed = consumed
        self.sanitizedDescription = sanitizedDescription
        self.depth = depth
        self.rune = rune
        self.stacks = stacks
