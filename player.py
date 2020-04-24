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

# outside class
# actor = Player()
# print(actor.name)
# print(actor.getName())
# print(actor.getName('Messi'))

player1 = Player('Dybala','86')
player2 = Player('Messi','95')
print(player1.getName() + " have speed "+ player1.getSpeed())
print(player2.getName() + " have speed "+ player2.getSpeed())
