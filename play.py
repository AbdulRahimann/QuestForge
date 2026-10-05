from domain.character import Character
from domain.classes import Warrior, Mage ,Cleric, Rogue
from domain.battle import run_special_round, total_party_damage
from domain.items import HealthPotion, Weapon
from domain.exceptions import QuestForgeError



if __name__ == "__main__":
    print("QuestForge booting...")
    # Character("test",100,10)

    # party = [Warrior("Bram"), Mage("Sylla"), Rogue("Kade"), Cleric("Thalia")]
    # dummy = Warrior("Dummy")
    # kade = Rogue("Kade")


    # for member in party:
    #     # Same function call, but completely different behavior each time!
    #     run_special_round(member, dummy)
    #     print(f"Dummy HP: {dummy.health}\n")


    # total_party_damage(party, dummy)
    # print(f"Dummy HP remaining: {dummy.health}")/

    # warrior = Warrior("Bram")
    
    
    # cleric = Cleric("Thalia")
    # for member in party:
    #     total_party_damage(party, kade)

    # print(f"kade HP: {kade.health}\n")
    # total_party_damage(c, kade)
    # print(f"kade HP: {kade.health}\n")

    # warrior.special_ability(mage)
    # mage.special_ability(warrior)
    # cleric.special_ability(warrior)
    # print(f"{mage.health}, {warrior.health}")

    
    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    
    try:
             # Sylla starts with 50 mana. 3 fireballs (20 cost each) will fail.
        mage.special_ability(warrior)
        mage.special_ability(warrior)
        mage.special_ability(warrior) 
    except QuestForgeError as e:
        print(f"Action failed: {e}")

    print(f"Character created: {warrior.name} | HP: {warrior.health} | ATK: {warrior.attack_power}")

    # Inflict damage to demonstrate the healing effect of the potions
    warrior.take_damage(50)
    print(f"{warrior.name} took 50 damage! Current HP: {warrior.health}\n")

    # 2. Give the character two potions and a weapon
    potion1 = HealthPotion(heal_amount=25)
    potion2 = HealthPotion(heal_amount=20)
    weapon = Weapon(name="Dragon Slayer", bonus_attack=15)

    warrior.inventory.add(potion1)
    warrior.inventory.add(potion2)
    warrior.inventory.add(weapon)

    print(f"Items in inventory: {warrior.inventory.list_items()}\n")

    # 3. Use each item from play.py
    print("--- Using Items ---")
    # Use first potion (pops index 0)
    print(warrior.inventory.use(0, warrior))
    print(f"Current HP: {warrior.health}\n")

    # Use second potion (now at index 0)
    print(warrior.inventory.use(0, warrior))
    print(f"Current HP: {warrior.health}\n")

    # Use weapon (now at index 0)
    print(warrior.inventory.use(0, warrior))
    print(f"Current ATK: {warrior.attack_power}\n")

    print("--- Final Status ---")
    print(f"{warrior.name} -> HP: {warrior.health}, ATK: {warrior.attack_power}")
    print(f"Remaining inventory: {warrior.inventory.list_items()}")

