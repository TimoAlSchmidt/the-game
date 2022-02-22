sword = False
option = "a"

def story():
    sword = False
    while True:
        option = input("""You're an adventurer, looking for treasure inside a dungeon. You walk into a room, the door disappearing behind you. You see 3 potions laid up on the table, a [red] one, a [blue] one and a [yellow] one. There's also a [read]able note on the table.\n""")
        while True:
            if option == "read":
                option = input("""The note says: "Two of these potions are poisonous, the third one contains the solution to leaving this room. The correct color is the same as the blood of the most common inhabitant of the forest""")
            elif option == "red":
                input("Red, like blood, right? You drink the red potion, hoping that your answer was correct. Unfortunately, you suddenly feel a burning deep inside your stomach, and burn from inside out. R.I.P.")
                quit()
            elif option == "blue":
                input("""Blue, like water, right? You drink the blue potion, hoping that your answer was correct. You don't feel anything at first, but then you feel your lungs fill with water. No matter how much you try to cough up the water, nothing comes out. R.I.P.""")
                quit()
            elif option == "yellow":
                option = input("""Yellow, like sap of trees, right? You drink the yellow potion, hoping that your answer was correct. You feel incredibly sick, but the feeling quickly subsides. The table suddenly combusts into flames, and reveals a trapdoor underneath. You open the trapdoor, seeing a [ladder] and some water underneath. You can't gauge the depth of the water from here, but you can always try [jumping] in. You also consider [stay]ing in the room, anything better than going down there.""")
                while True:
                    if option == "stay":
                        input("""You stay in the room, and the trapdoor disappears. I suppose this is the room where doorways just stop existing once they're opened. You no longer have a way out, and starve to death. R.I.P.""")
                        quit()
                    elif option == "ladder":
                        print("""You climb the ladder downward, halfway on the ladder, the trapdoor, and ladder, disappears. You fall down to the floor, luckily unharmed. You see that the water puddle is just that, a puddle.""")
                        while True:
                            option = input("""In this room, you see a [bookshelf] with books scattered about. You also see a [chest], with a bloody puddle next to it.""")
                            if option == "chest":
                                input("""You hope that bloody puddle is just ketchup. It wasn't, as the chest comes alive, and devours you whole. R.I.P.""")
                                quit()
                            elif option == "bookshelf":
                                print("""You decide it's better not to mess around with the blood chest, you check around the books and see a lever hidden behind one the books. How clever. You pull the lever, and the bookshelf reveals a secret passageway downward.""")
                                return sword
                    elif option == "jumping":
                        print("""You jump into the water, hoping for the best, and you fall down through the water into another room.""")
                        while True:
                            option = input("""In this room, you see a [sword] on a pedestal, and a [door].""")
                            if option == "door":
                                input("You decide that going through the door is your top priority, because you don't want to get stuck in a room. Unfortunately, you'd probably be better off if you grabbed that sword, as a skeleton strikes you down when you exit. R.I.P.")
                                quit()
                            elif option == "sword":
                                sword = True
                                while True:
                                    option = input("You grab the sword from the pedestal, it's surprisingly light. You calmly exit the room, and enter another room. A big dining room, with tables all around. You see an skeleton with a wizard's hat, ready to cast a spell. Do you [roll] towards cover, [run] towards the skeleton or [throw] your sword.")
                                    if option == "run":
                                        input("The skeleton casts a fireball and you light up in flames. R.I.P.")
                                        quit()
                                    elif option == "throw":
                                        input("You threw your sword. The skeleton casts a haunting spell on your sword. Your sword kills you. R.I.P.")
                                        quit()
                                    elif option == "roll":
                                        print("You roll towards one of the tables and flip them over as cover, safe for now, but not for long. The skeleton casts a fireball, and the table combusts into flames. Now what?")
                                        while True:
                                            option = input("Knocking over the table dropped some metal dining plates which you can [throw] at the skeleton, you can try [run]ning at him or you can also throw your [sword].")
                                            if option == "run":
                                                input("You ran towards the skeleton. He had some trapping magic surrounding him, and you get killed by the venomous plants the trap produces. R.I.P.")
                                                quit()
                                            elif option == "sword":
                                                input("You ran towards the skeleton. He had some trapping magic surrounding him, and you get killed by the venomous plants the trap produces. R.I.P.")
                                                quit()
                                            elif option == "throw":
                                                while True:
                                                    option = input("You hit the wizard skeleton straight in the face, confusing him. Now is your change to strike. Do you run at him to [strike] him or do you [throw] your sword from a distance?")
                                                    if option == "strike":
                                                        input("You run at him, but just because a wizard is dazed doesn't mean his magic doesn't work. You get trapped by some venomous plants, and they bite you. R.I.P.")
                                                        quit()
                                                    elif option == "throw":
                                                        print("You throw your sword at the skeleton, and kill him. Good job. You leave the dining room.")
                                                        return sword
                    else:
                        break


sword = story()

while True:
    option = input("You enter a treasure room of some sort and see a lot of chests around, and a door outside. Do you [investigate] the chests or do you decide to [leave] this place as fast as possible?")
    if option == "investigate":
        print("You decide that investigating the chests can't hurt. In one of the chests, you see a pile of gold, so you decide you want to take that.")
        if sword:
            print("But then, the chest comes alive, a mimic! You quickly strike it down. You decide to quickly grab the contents of the chests, and run outside, and to the nearby town. Unfortunately most of the other chests didn't contain anything of use.")
            input("You reach the nearby town, and complete your quest. In the bar, the blacksmith looks at your sword, and requests to investigate it. You let him, and it turns out it's a dragonsteel sword, forged in the fire of dragons. You decide to sell it for piles of gold. \nEnding 3/3: Rich")
            quit()
        else:
            print("But then, the chest comes alive, a mimic! You barely escape through the door, with a heavy scratch to your right leg. Unfortunately you had to leave the pile of gold.")
            input("You barely reach the nearby town, and have to get into debt to afford the potions to survive. \nEnding 2/3: Indebted")
            quit()
    elif option == "leave":
        input("You've had it with this dungeon, and decide to leave. You enter a nearby town. You check the bounty board and see that there's another dungeon... I guess it can't hurt to try, right? \nEnding 1/3: Safe and Sound")
        quit()

