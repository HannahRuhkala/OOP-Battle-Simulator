import random
class Hero:
   

    def __init__(self,name):
        self.name = name
        self.health = 138
        self.attack_power = 18
    def attack(self):
            
            return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
            self.health = max(0, self.health - damage)
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
    
    def is_alive(self):
            return self.health > 0
    def __init__(self, name, cry):
        self.name = name
        self.cry = cry

    def battle_cry(self):
        print(f"{self.name} charges into battle shouting: '{self.cry}'!!")

    