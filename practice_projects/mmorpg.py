class Character :
    def __init__(self , * ,  level) -> None:
        self.level = level
        self.health = self.base_hp * level
        self.damage = self.base_damage * level
        
        
    def Attack(self , * ,  target: "Character") -> None:
         target.got_damaged(damage = self.damage)
         
    def got_damaged(self , damage) -> None:
        damage = damage * (100 - self.defense) / 100
        damage = round(damage)
        self.health -= damage
        
             
        
    def is_Alive(self) -> bool :
        return self.health > 0 
    
    @property 
    def defense(self) -> int:
        defense = self.base_defense * self.level  
        return defense
    
    
    
    def health_points_percent(self):
        return 100 * (self.level / round(self.level *self.base_hp))
        
   
        
        
        
    def __str__(self) -> str:
        return f"{self.character_name} has level = {self.level} , hp = {self.health}"
    

 
    
class Ork(Character):
    base_hp = 100
    base_damage = 10
    base_defense = 10
    character_name = "Ork"
    @property 
    def defense(self) -> int:
        defense = super().defense
        
        if self.health < 50:
            defense *= 3
        return defense
    
    
class Elf(Character) :
    base_hp =50
    base_damage = 15
    base_defense = 10
    character_name = "Elf"
    
    def attack(self , * ,target = "Character") -> None:
        if target.health_points_percent() < 30 :
            attack_power = self.damage * 3
        target.got_damaged(damage = attack_power)
        
        


def fight(*, character_1 : Character , character_2 : Character) -> None:
    while character_1.is_Alive() and character_2.is_Alive():
        character_1.Attack( target=character_2)
        if character_2.is_Alive():
            character_2.Attack(target=character_1)
    print(f"Character 1 :{character_1} is alive : {character_1.is_Alive()}")
    print(f"Character 2 :{character_2} is alive : {character_2.is_Alive()}")
    


ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1=ork , character_2=elf)

