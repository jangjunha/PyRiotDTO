class Rune(object):
    """ Rune DTO object

    Attributes:
        plaintext (string): 
        into (List[string]): 
        inStore (boolean): 
        id (int): 
        stats (BasicDataStats): 
        from (List[string]): 
        colloq (string): 
        maps (Map[string, boolean]): 
        specialRecipe (int): 
        image (Image): 
        description (string): 
        hideFromAll (boolean): 
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

    def __init__(self, plaintext, into, inStore, id, stats, from, colloq, maps, specialRecipe, image, description, hideFromAll, tags, requiredChampion, group, consumeOnFull, name, consumed, sanitizedDescription, depth, rune, stacks):
        self.plaintext = plaintext
        self.into = into
        self.inStore = inStore
        self.id = id
        self.stats = stats
        self.from = from
        self.colloq = colloq
        self.maps = maps
        self.specialRecipe = specialRecipe
        self.image = image
        self.description = description
        self.hideFromAll = hideFromAll
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
