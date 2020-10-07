#Fortnite Module
from FortniteAPI import FortniteAPI

class FortniteStats:
    def __init__(self, fortniteUserName):
        FortniteAPI.api_key = 'feeee83b-54d6-42fc-b4c3-f47a5f58f16e'
        user = FortniteAPI('all',fortniteUserName)

        self.__sScore = str(user.stats.LIFETIME_SOLO_SCORE)
        self.__dScore = str(user.stats.LIFETIME_DUO_SCORE)
        self.__sqScore = str(user.stats.LIFETIME_SQUAD_SCORE)
        self.__sKills = str(user.stats.LIFETIME_SOLO_KILLS)
        self.__dKills = str(user.stats.LIFETIME_DUO_KILLS)
        self.__sqKills = str(user.stats.LIFETIME_SQUAD_KILLS)
        self.__sWins = str(user.stats.LIFETIME_SOLO_WINS)
        self.__dWins = str(user.stats.LIFETIME_DUO_WINS)
        self.__sqWins = str(user.stats.LIFETIME_SQUAD_WINS)
        self.__tKills = str(user.stats.LIFETIME_KILLS)
        self.__tWins = str(user.stats.LIFETIME_WINS)
        self.__tScore = str(user.stats.LIFETIME_SCORE)
        self.__tWinPct = str(user.stats.LIFETIME_WIN_PERCENTAGE)
        

    def get_soloScore(self):
        return self.__sScore

    def get_duoScore(self):
        return self.__dScore

    def get_squadScore(self):
        return self.__sqScore

    def get_soloKills(self):
        return self.__sKills

    def get_duoKills(self):
        return self.__dKills

    def get_squadKills(self):
        return self.__sqKills

    def get_soloWins(self):
        return self.__sWins

    def get_duoWins(self):
        return self.__dWins

    def get_squadWins(self):
        return self.__sqWins

    def get_totalWins(self):
        return self.__tWins

    def get_totalKills(self):
        return self.__tKills

    def get_totalScore(self):
        return self.__tScore
    
    def get_totalWinPct(self):
        return self.__tWinPct


    soloScore = property(get_soloScore)
    duoScore = property(get_duoScore)
    squadScore = property(get_squadScore)

    soloKills = property(get_soloKills)
    duoKills = property(get_duoKills)
    squadKills = property(get_squadKills)

    soloWins = property(get_soloWins)
    duoWins = property(get_duoWins)
    squadWins = property(get_squadWins)

    totalWins = property(get_totalWins)
    totalKills = property(get_totalKills)
    totalScore = property(get_totalScore)
    totalWinPct = property(get_totalWinPct)
