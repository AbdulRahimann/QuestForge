from domain.character import Character
from domain.classes import Warrior, Mage ,Cleric, Rogue
from domain.battle import run_special_round, total_party_damage




if __name__ == "__main__":
    print("QuestForge booting...")

    party = [Warrior("Bram"), Mage("Sylla"), Rogue("Kade"), Cleric("Thalia")]
    dummy = Warrior("Dummy")
    kade = Rogue("Kade")


    for member in party:
        # Same function call, but completely different behavior each time!
        run_special_round(member, dummy)
        print(f"Dummy HP: {dummy.health}\n")


    # total_party_damage(party, dummy)
    # print(f"Dummy HP remaining: {dummy.health}")/

    # warrior = Warrior("Bram")
    # mage = Mage("Sylla")
    
    cleric = Cleric("Thalia")
    print(f"kade HP: {kade.health}\n")
    total_party_damage(cleric, kade)
    print(f"kade HP: {kade.health}\n")


    # warrior.special_ability(mage)
    # mage.special_ability(warrior)
    # cleric.special_ability(warrior)
    # print(f"{mage.health}, {warrior.health}")

    
    
   

        
