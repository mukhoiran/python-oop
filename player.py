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

class ArgentinaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age

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
print(player.getName() + " have age " + player.setAge('26'))
