class Character:
    
    def __init__(self, name, type, health, mana):
        self.name=name
        self.type=type
        self.health=health
        self.mana=mana
    


    @classmethod
    def createMage(cls,name):
        return cls(name,type="Mage",health=100,mana=110)
    
    @classmethod
    def createWarrior(cls,name):
        return cls(name,type="Warrior",health=115,mana=70)
    


    def showInfo(self):
        print(f"{self.name} the {self.type} | HP: {self.health} | Mana: {self.mana}")

    def attack(self, type):
        pass