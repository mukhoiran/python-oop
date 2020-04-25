# ================
# Class and Object
# ================

class Player:
    # name = 'Mbappe'
    name = ''
    speed = ''
    job = 'Football player'

    def __init__(self, param1, param2):
        self.name = param1
        self.speed = param2
        # private variable (use __)
        self.__age = 23

    def getName(self):
        # self.name = param
        return self.name

    def getSpeed(self):
        # self.speed = param
        return self.speed

    def getSkill(self):
        return 'balance'

    def getAge(self):
        return self.__age

    @staticmethod
    def retiredIn(age):
        return str(40 - age)

    @classmethod
    def generalInfo(cls):
        return cls.job + ' will retired in 40 years'

    @property
    def playerInfo(self):
        return self.name + ' is ' + self.speed

#inhertance class
class ArgentinaPlayer(Player):
    def __init__(self, param1, param2):
        # Player.__init__(self, param1, param2)
        super().__init__(param1, param2)
        print('argentina player')

    def setAge(self, age):
        self.age = age
        return self.age

    def getSkill(self):
        return 'shoot'

class SpanyolPlayer(Player):
    pass

class IndonesianPlayer(Player):
    def getSkill(self):
        return 'tackle'

# outside class
# actor = Player()
# print(actor.name)
# print(actor.getName())
# print(actor.getName('Messi'))

# player1 = Player('Dybala','86')
# player2 = Player('Messi','95')
# print(player1.getName() + " have speed "+ player1.getSpeed())
# print(player2.getName() + " have speed "+ player2.getSpeed())

player = ArgentinaPlayer('Dybala','86')
player2 = SpanyolPlayer('Iniesta','87')
player3 = Player('Messi','10')
# print(player.getName() + " have age " + player.setAge('26'))
print(player.getName() + " have skill "+ player.getSkill())
print(player2.getName() + " have skill "+ player2.getSkill())
print(player.getAge())

# Call static method (no need declare object)
print('Retired on ' + Player.retiredIn(25))

# Call class method (no need declare object)
print(Player.generalInfo())

#Call property
print(player3.playerInfo)
