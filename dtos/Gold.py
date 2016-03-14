class Gold(object):
    """ Gold DTO object

    Attributes:
        sell (int): 
        total (int): 
        base (int): 
        purchasable (boolean): 
    """

    def __init__(self, sell, total, base, purchasable):
        self.sell = sell
        self.total = total
        self.base = base
        self.purchasable = purchasable
