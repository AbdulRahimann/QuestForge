import domain.character as character

if __name__ == "__main__":
    print("QuestForge booting...(level 0 skeleton)")

    hero = character.Character("Aria", 100, 15)
    goblin = character.Character("Goblin", 30, 5)
    sensei_moro = character.Character("Sensei Moro", 130, 25)
    wizard = character.Character("Wizard", 120, 20)
    
    

    # print(hero.describe())
    # print(goblin.describe())


    # hero.attack(goblin)
    # print(goblin.describe())
    # print(goblin.heal(15))
    # print(goblin.describe())
    print("====== Battle Begins ======:")
    print(sensei_moro.describe())
    print(wizard.describe())
    for i in range(3):
        print(f"====== Attack_Round {i + 1} ======:")
        sensei_moro.attack(wizard)
        print(wizard.describe())
        wizard.attack(sensei_moro)
        print(sensei_moro.describe())
    print("====== Battle Ends ======:")
    print(wizard.describe())
    print(sensei_moro.describe())
    print("====== Healing Begins ======:")
    print(wizard.heal(30))
    print(sensei_moro.heal(30))
    print("======health status after healing ======:")
    print(wizard.describe())
    print(sensei_moro.describe())

        
