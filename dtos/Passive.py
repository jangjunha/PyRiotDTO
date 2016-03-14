class Passive(object):
    """ Passive DTO object

    Attributes:
        image (Image): 
        sanitizedDescription (string): 
        description (string): 
        name (string): 
    """

    def __init__(self, image, sanitizedDescription, description, name):
        self.image = image
        self.sanitizedDescription = sanitizedDescription
        self.description = description
        self.name = name
