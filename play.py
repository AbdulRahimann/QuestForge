from domain.character import Character
from domain.classes import Warrior, Mage ,Cleric




if __name__ == "__main__":
    print("QuestForge booting...")

   

    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    cleric = Cleric("Thalia")

    warrior.special_ability(mage)
    mage.special_ability(warrior)
    cleric.special_ability(warrior)
    print(f"{mage.health}, {warrior.health}")

    
    
   

        
