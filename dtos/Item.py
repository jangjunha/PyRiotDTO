class Item(object):
    """ Item DTO object

    Attributes:
        gold (Gold): Data Dragon includes the gold field for basic data, which is shared by both rune and item. However, only items have a gold field on them, representing their gold cost in the store. Since runes are not sold in the store, they have no gold cost.
        plaintext (string): 
        hideFromAll (boolean): 
        inStore (boolean): 
        id (int): 
        stats (BasicDataStats): 
        from (List[string]): 
        image (Image): 
        colloq (string): 
        maps (Map[string, boolean]): 
        specialRecipe (int): 
        into (List[string]): 
        description (string): 
        tags (List[string]): 
        effect (Map[string, string]): 
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

    def __init__(self, gold, plaintext, hideFromAll, inStore, id, stats, from, image, colloq, maps, specialRecipe, into, description, tags, effect, requiredChampion, group, consumeOnFull, name, consumed, sanitizedDescription, depth, rune, stacks):
        self.gold = gold
        self.plaintext = plaintext
        self.hideFromAll = hideFromAll
        self.inStore = inStore
        self.id = id
        self.stats = stats
        self.from = from
        self.image = image
        self.colloq = colloq
        self.maps = maps
        self.specialRecipe = specialRecipe
        self.into = into
        self.description = description
        self.tags = tags
        self.effect = effect
        self.requiredChampion = requiredChampion
        self.group = group
        self.consumeOnFull = consumeOnFull
        self.name = name
        self.consumed = consumed
        self.sanitizedDescription = sanitizedDescription
        self.depth = depth
        self.rune = rune
        self.stacks = stacks
