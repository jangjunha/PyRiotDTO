class RawStats(object):
    """ RawStats DTO object

    Attributes:
        championsKilled (int): 
        consumablesPurchased (int): 
        totalPlayerScore (int): 
        gold (int): 
        unrealKills (int): 
        visionWardsBought (int): 
        wardPlaced (int): 
        objectivePlayerScore (int): 
        totalDamageDealt (int): 
        magicDamageDealtToChampions (int): 
        firstBlood (int): 
        largestMultiKill (int): 
        largestKillingSpree (int): 
        legendaryItemsCreated (int): Number of tier 3 items built.
        quadraKills (int): 
        magicDamageTaken (int): 
        barracksKilled (int): Number of enemy inhibitors killed.
        spell4Cast (int): Number of times fourth champion spell was cast.
        bountyLevel (int): 
        trueDamageDealtPlayer (int): 
        neutralMinionsKilledEnemyJungle (int): 
        spell2Cast (int): Number of times second champion spell was cast.
        item2 (int): 
        item3 (int): 
        item0 (int): 
        item1 (int): 
        item6 (int): 
        item4 (int): 
        item5 (int): 
        minionsKilled (int): 
        teamObjective (int): 
        nexusKilled (boolean): Flag specifying if the summoner got the killing blow on the nexus.
        tripleKills (int): 
        wardKilled (int): 
        nodeNeutralizeAssist (int): 
        neutralMinionsKilledYourJungle (int): 
        numItemsBought (int): 
        itemsPurchased (int): 
        timePlayed (int): 
        doubleKills (int): 
        spell1Cast (int): Number of times first champion spell was cast.
        spell3Cast (int): Number of times third champion spell was cast.
        largestCriticalStrike (int): 
        nodeCaptureAssist (int): 
        trueDamageTaken (int): 
        nodeNeutralize (int): 
        summonSpell2Cast (int): 
        damageDealtPlayer (int): 
        assists (int): 
        totalScoreRank (int): 
        neutralMinionsKilled (int): 
        combatPlayerScore (int): 
        nodeCapture (int): 
        playerRole (int): Player role (Legal values: DUO(1), SUPPORT(2), CARRY(3), SOLO(4))
        win (boolean): Flag specifying whether or not this game was won.
        physicalDamageDealtToChampions (int): 
        goldSpent (int): 
        playerPosition (int): Player position (Legal values: TOP(1), MIDDLE(2), JUNGLE(3), BOT(4))
        trueDamageDealtToChampions (int): 
        killingSprees (int): 
        totalTimeCrowdControlDealt (int): 
        minionsDenied (int): 
        level (int): 
        victoryPointTotal (int): 
        summonSpell1Cast (int): 
        physicalDamageDealtPlayer (int): 
        totalHeal (int): 
        sightWardsBought (int): 
        goldEarned (int): 
        turretsKilled (int): 
        totalDamageDealtToChampions (int): 
        totalUnitsHealed (int): 
        team (int): 
        numDeaths (int): 
        superMonsterKilled (int): 
        totalDamageTaken (int): 
        pentaKills (int): 
        magicDamageDealtPlayer (int): 
        physicalDamageTaken (int): 
    """

    def __init__(self, championsKilled, consumablesPurchased, totalPlayerScore, gold, unrealKills, visionWardsBought, wardPlaced, objectivePlayerScore, totalDamageDealt, magicDamageDealtToChampions, firstBlood, largestMultiKill, largestKillingSpree, legendaryItemsCreated, quadraKills, magicDamageTaken, barracksKilled, spell4Cast, bountyLevel, trueDamageDealtPlayer, neutralMinionsKilledEnemyJungle, spell2Cast, item2, item3, item0, item1, item6, item4, item5, minionsKilled, teamObjective, nexusKilled, tripleKills, wardKilled, nodeNeutralizeAssist, neutralMinionsKilledYourJungle, numItemsBought, itemsPurchased, timePlayed, doubleKills, spell1Cast, spell3Cast, largestCriticalStrike, nodeCaptureAssist, trueDamageTaken, nodeNeutralize, summonSpell2Cast, damageDealtPlayer, assists, totalScoreRank, neutralMinionsKilled, combatPlayerScore, nodeCapture, playerRole, win, physicalDamageDealtToChampions, goldSpent, playerPosition, trueDamageDealtToChampions, killingSprees, totalTimeCrowdControlDealt, minionsDenied, level, victoryPointTotal, summonSpell1Cast, physicalDamageDealtPlayer, totalHeal, sightWardsBought, goldEarned, turretsKilled, totalDamageDealtToChampions, totalUnitsHealed, team, numDeaths, superMonsterKilled, totalDamageTaken, pentaKills, magicDamageDealtPlayer, physicalDamageTaken):
        self.championsKilled = championsKilled
        self.consumablesPurchased = consumablesPurchased
        self.totalPlayerScore = totalPlayerScore
        self.gold = gold
        self.unrealKills = unrealKills
        self.visionWardsBought = visionWardsBought
        self.wardPlaced = wardPlaced
        self.objectivePlayerScore = objectivePlayerScore
        self.totalDamageDealt = totalDamageDealt
        self.magicDamageDealtToChampions = magicDamageDealtToChampions
        self.firstBlood = firstBlood
        self.largestMultiKill = largestMultiKill
        self.largestKillingSpree = largestKillingSpree
        self.legendaryItemsCreated = legendaryItemsCreated
        self.quadraKills = quadraKills
        self.magicDamageTaken = magicDamageTaken
        self.barracksKilled = barracksKilled
        self.spell4Cast = spell4Cast
        self.bountyLevel = bountyLevel
        self.trueDamageDealtPlayer = trueDamageDealtPlayer
        self.neutralMinionsKilledEnemyJungle = neutralMinionsKilledEnemyJungle
        self.spell2Cast = spell2Cast
        self.item2 = item2
        self.item3 = item3
        self.item0 = item0
        self.item1 = item1
        self.item6 = item6
        self.item4 = item4
        self.item5 = item5
        self.minionsKilled = minionsKilled
        self.teamObjective = teamObjective
        self.nexusKilled = nexusKilled
        self.tripleKills = tripleKills
        self.wardKilled = wardKilled
        self.nodeNeutralizeAssist = nodeNeutralizeAssist
        self.neutralMinionsKilledYourJungle = neutralMinionsKilledYourJungle
        self.numItemsBought = numItemsBought
        self.itemsPurchased = itemsPurchased
        self.timePlayed = timePlayed
        self.doubleKills = doubleKills
        self.spell1Cast = spell1Cast
        self.spell3Cast = spell3Cast
        self.largestCriticalStrike = largestCriticalStrike
        self.nodeCaptureAssist = nodeCaptureAssist
        self.trueDamageTaken = trueDamageTaken
        self.nodeNeutralize = nodeNeutralize
        self.summonSpell2Cast = summonSpell2Cast
        self.damageDealtPlayer = damageDealtPlayer
        self.assists = assists
        self.totalScoreRank = totalScoreRank
        self.neutralMinionsKilled = neutralMinionsKilled
        self.combatPlayerScore = combatPlayerScore
        self.nodeCapture = nodeCapture
        self.playerRole = playerRole
        self.win = win
        self.physicalDamageDealtToChampions = physicalDamageDealtToChampions
        self.goldSpent = goldSpent
        self.playerPosition = playerPosition
        self.trueDamageDealtToChampions = trueDamageDealtToChampions
        self.killingSprees = killingSprees
        self.totalTimeCrowdControlDealt = totalTimeCrowdControlDealt
        self.minionsDenied = minionsDenied
        self.level = level
        self.victoryPointTotal = victoryPointTotal
        self.summonSpell1Cast = summonSpell1Cast
        self.physicalDamageDealtPlayer = physicalDamageDealtPlayer
        self.totalHeal = totalHeal
        self.sightWardsBought = sightWardsBought
        self.goldEarned = goldEarned
        self.turretsKilled = turretsKilled
        self.totalDamageDealtToChampions = totalDamageDealtToChampions
        self.totalUnitsHealed = totalUnitsHealed
        self.team = team
        self.numDeaths = numDeaths
        self.superMonsterKilled = superMonsterKilled
        self.totalDamageTaken = totalDamageTaken
        self.pentaKills = pentaKills
        self.magicDamageDealtPlayer = magicDamageDealtPlayer
        self.physicalDamageTaken = physicalDamageTaken
