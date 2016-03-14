class AggregatedStats(object):
    """ AggregatedStats DTO object

    Attributes:
        totalPhysicalDamageDealt (int): 
        averageObjectivePlayerScore (int): Dominion only.
        totalTurretsKilled (int): 
        averageNodeNeutralize (int): Dominion only.
        averageChampionsKilled (int): Dominion only.
        totalSessionsPlayed (int): 
        totalAssists (int): 
        rankedPremadeGamesPlayed (int): 
        mostChampionKillsPerSession (int): 
        killingSpree (int): 
        maxNodeNeutralize (int): Dominion only.
        mostSpellsCast (int): 
        totalDoubleKills (int): 
        maxTeamObjective (int): Dominion only.
        averageNodeNeutralizeAssist (int): Dominion only.
        averageTeamObjective (int): Dominion only.
        averageAssists (int): Dominion only.
        maxChampionsKilled (int): 
        totalNodeCapture (int): Dominion only.
        totalDeathsPerSession (int): Only returned for ranked statistics.
        totalSessionsWon (int): 
        maxNodeNeutralizeAssist (int): Dominion only.
        totalGoldEarned (int): 
        totalPentaKills (int): 
        totalTripleKills (int): 
        totalNeutralMinionsKilled (int): 
        averageTotalPlayerScore (int): Dominion only.
        maxTotalPlayerScore (int): Dominion only.
        maxTimeSpentLiving (int): 
        totalDamageDealt (int): 
        rankedSoloGamesPlayed (int): 
        maxNodeCaptureAssist (int): Dominion only.
        maxLargestKillingSpree (int): 
        totalChampionKills (int): 
        maxNumDeaths (int): Only returned for ranked statistics.
        averageNodeCaptureAssist (int): Dominion only.
        totalDamageTaken (int): 
        totalNodeNeutralize (int): Dominion only.
        totalMinionKills (int): 
        maxObjectivePlayerScore (int): Dominion only.
        maxNodeCapture (int): Dominion only.
        maxCombatPlayerScore (int): Dominion only.
        totalMagicDamageDealt (int): 
        totalHeal (int): 
        normalGamesPlayed (int): 
        totalQuadraKills (int): 
        averageNumDeaths (int): Dominion only.
        totalUnrealKills (int): 
        averageNodeCapture (int): Dominion only.
        maxAssists (int): Dominion only.
        maxTimePlayed (int): 
        maxLargestCriticalStrike (int): 
        botGamesPlayed (int): 
        averageCombatPlayerScore (int): Dominion only.
        totalSessionsLost (int): 
        totalFirstBlood (int): 
    """

    def __init__(self, totalPhysicalDamageDealt, averageObjectivePlayerScore, totalTurretsKilled, averageNodeNeutralize, averageChampionsKilled, totalSessionsPlayed, totalAssists, rankedPremadeGamesPlayed, mostChampionKillsPerSession, killingSpree, maxNodeNeutralize, mostSpellsCast, totalDoubleKills, maxTeamObjective, averageNodeNeutralizeAssist, averageTeamObjective, averageAssists, maxChampionsKilled, totalNodeCapture, totalDeathsPerSession, totalSessionsWon, maxNodeNeutralizeAssist, totalGoldEarned, totalPentaKills, totalTripleKills, totalNeutralMinionsKilled, averageTotalPlayerScore, maxTotalPlayerScore, maxTimeSpentLiving, totalDamageDealt, rankedSoloGamesPlayed, maxNodeCaptureAssist, maxLargestKillingSpree, totalChampionKills, maxNumDeaths, averageNodeCaptureAssist, totalDamageTaken, totalNodeNeutralize, totalMinionKills, maxObjectivePlayerScore, maxNodeCapture, maxCombatPlayerScore, totalMagicDamageDealt, totalHeal, normalGamesPlayed, totalQuadraKills, averageNumDeaths, totalUnrealKills, averageNodeCapture, maxAssists, maxTimePlayed, maxLargestCriticalStrike, botGamesPlayed, averageCombatPlayerScore, totalSessionsLost, totalFirstBlood):
        self.totalPhysicalDamageDealt = totalPhysicalDamageDealt
        self.averageObjectivePlayerScore = averageObjectivePlayerScore
        self.totalTurretsKilled = totalTurretsKilled
        self.averageNodeNeutralize = averageNodeNeutralize
        self.averageChampionsKilled = averageChampionsKilled
        self.totalSessionsPlayed = totalSessionsPlayed
        self.totalAssists = totalAssists
        self.rankedPremadeGamesPlayed = rankedPremadeGamesPlayed
        self.mostChampionKillsPerSession = mostChampionKillsPerSession
        self.killingSpree = killingSpree
        self.maxNodeNeutralize = maxNodeNeutralize
        self.mostSpellsCast = mostSpellsCast
        self.totalDoubleKills = totalDoubleKills
        self.maxTeamObjective = maxTeamObjective
        self.averageNodeNeutralizeAssist = averageNodeNeutralizeAssist
        self.averageTeamObjective = averageTeamObjective
        self.averageAssists = averageAssists
        self.maxChampionsKilled = maxChampionsKilled
        self.totalNodeCapture = totalNodeCapture
        self.totalDeathsPerSession = totalDeathsPerSession
        self.totalSessionsWon = totalSessionsWon
        self.maxNodeNeutralizeAssist = maxNodeNeutralizeAssist
        self.totalGoldEarned = totalGoldEarned
        self.totalPentaKills = totalPentaKills
        self.totalTripleKills = totalTripleKills
        self.totalNeutralMinionsKilled = totalNeutralMinionsKilled
        self.averageTotalPlayerScore = averageTotalPlayerScore
        self.maxTotalPlayerScore = maxTotalPlayerScore
        self.maxTimeSpentLiving = maxTimeSpentLiving
        self.totalDamageDealt = totalDamageDealt
        self.rankedSoloGamesPlayed = rankedSoloGamesPlayed
        self.maxNodeCaptureAssist = maxNodeCaptureAssist
        self.maxLargestKillingSpree = maxLargestKillingSpree
        self.totalChampionKills = totalChampionKills
        self.maxNumDeaths = maxNumDeaths
        self.averageNodeCaptureAssist = averageNodeCaptureAssist
        self.totalDamageTaken = totalDamageTaken
        self.totalNodeNeutralize = totalNodeNeutralize
        self.totalMinionKills = totalMinionKills
        self.maxObjectivePlayerScore = maxObjectivePlayerScore
        self.maxNodeCapture = maxNodeCapture
        self.maxCombatPlayerScore = maxCombatPlayerScore
        self.totalMagicDamageDealt = totalMagicDamageDealt
        self.totalHeal = totalHeal
        self.normalGamesPlayed = normalGamesPlayed
        self.totalQuadraKills = totalQuadraKills
        self.averageNumDeaths = averageNumDeaths
        self.totalUnrealKills = totalUnrealKills
        self.averageNodeCapture = averageNodeCapture
        self.maxAssists = maxAssists
        self.maxTimePlayed = maxTimePlayed
        self.maxLargestCriticalStrike = maxLargestCriticalStrike
        self.botGamesPlayed = botGamesPlayed
        self.averageCombatPlayerScore = averageCombatPlayerScore
        self.totalSessionsLost = totalSessionsLost
        self.totalFirstBlood = totalFirstBlood
