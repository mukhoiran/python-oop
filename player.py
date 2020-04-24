# ================
# Class and Object
# ================

class Player:
    # name = 'Mbappe'
    name = ''
    speed = ''

    def __init__(self, param1, param2):
        self.name = param1
        self.speed = param2

    def getName(self):
        # self.name = param
        return self.name

    def getSpeed(self):
        # self.speed = param
        return self.speed

    def getSkill(self):
        return 'balance'

#inhertance class
class ArgentinaPlayer(Player):
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
# print(player.getName() + " have age " + player.setAge('26'))
print(player.getName() + " have skill "+ player.getSkill())
print(player2.getName() + " have skill "+ player2.getSkill())
