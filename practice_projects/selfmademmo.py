class Character:
    
    def __init__(self , * , level:int) -> None:
        self.level = level 
        self.health_points = self.base_health_points * 100
        self.attack_points = self.base_attack_power * 10
        
    def Attack(self):
        print (f"{self.character_name} attack with {self.attack_points} power!")
    
    def __str__(self) -> str:
        return f"{self.character_name} has lvl = {self.level} ,  hp = {self.health_points} , damage = {self.attack_points}"
    
    def is_Alive(self) -> bool:
        return self.health_points > 0 
    
class Knight(Character):
    base_health_points = 100
    base_attack_power = 5
    character_name = "Knight"
    
class Barbarian(Character):
    base_health_points = 5
    base_attack_power = 10
    character_name = "Barbarian"
    
knight = Knight(level = 1)
barbarian = Barbarian(level = 1)


def Fight(* , character_1:Character , character_2:Character):
    while character_1.is_Alive() and character_2.is_Alive():
        print("Win")
        


