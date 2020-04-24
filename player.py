# ================
# Class and Object
# ================

class Player:
    # name = 'Mbappe'
    name = ''

    def getName(self, param):
        self.name = param
        return self.name

# outside class
actor = Player()
# print(actor.name)
# print(actor.getName())
print(actor.getName('Messi'))
