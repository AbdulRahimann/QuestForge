from domain.item import  Usable, Equippable

'''composition over inheritance''' 


class HealthPotion(Usable):

    def __init__(self, heal_amount: int = 25):
        self.heal_amount = heal_amount


    def apply(self, character) -> str:
        character.heal(self.heal_amount)
        return f"{character.name} drinks a potion and heals {self.heal_amount} HP!"



class Weapon(Equippable):
    def __init__(self, name: str, bonus_attack: int):
        self.name = name
        self.bonus_attack = bonus_attack


    def equip(self, character) -> str:
        character.attack_power += self.bonus_attack
        return f"{character.name} equips {self.name} (+{self.bonus_attack} ATK)"