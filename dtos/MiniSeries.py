class MiniSeries(object):
    """ MiniSeries DTO object

    Attributes:
        progress (string): String showing the current, sequential mini series progress where 'W' represents a win, 'L' represents a loss, and 'N' represents a game that hasn't been played yet.
        losses (int): Number of current losses in the mini series.
        target (int): Number of wins required for promotion.
        wins (int): Number of current wins in the mini series.
    """

    def __init__(self, progress, losses, target, wins):
        self.progress = progress
        self.losses = losses
        self.target = target
        self.wins = wins
