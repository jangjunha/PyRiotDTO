class MapDetails(object):
    """ MapDetails DTO object

    Attributes:
        mapName (string): 
        image (Image): 
        mapId (long): 
        unpurchasableItemList (List[long]): 
    """

    def __init__(self, mapName, image, mapId, unpurchasableItemList):
        self.mapName = mapName
        self.image = image
        self.mapId = mapId
        self.unpurchasableItemList = unpurchasableItemList
