# By: Brian Sayre
# 11-13-16
# Python Text Based Adventure Game
# DO MAP
# COAT MOUNTAIN

import time
import random

startMission = 0
destination = 0
gold = 0
inventory = []


def intro():
    global name
    print("Welcome to Brian's Text-Based Adventure Game.")
    print("============================================\n")
    name = str(input("What is your name? ")).upper()
    print("You have had a pretty rough day...")
    time.sleep(1.5)
    print("But finally you are back in your apartment downtown...")
    time.sleep(1.5)
    print("You lay down in your bed, hoping tomorrow will be a better day...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("You wake up from the sun shining brightly into your eyes...")
    time.sleep(1.5)
    print("Wait... this isn't your house!")
    time.sleep(1.5)
    print("Everything here seems old...")
    time.sleep(1.5)
    print("You walk out out of the front door...")
    time.sleep(1.5)
    west()

def town():
    global destination
    destination = 1
    print("\n=====================")
    print("LONGDALE TOWN SQUARE")
    print("=====================")
    print("This town seems to be quick small and isolated...")
    time.sleep(1.5)
    print("There's a map too, let's choose a direction to go!\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nNorth Road(n)\nEast Town(e)\nSouth Road(s)\nWest Town(w)\nView map(m)\n")
    choice = str(input("> "))
    valid = 0
    while valid == 0:
        try:
            if choice == "n":
                valid = 1
                north()
            elif choice == "e":
                valid = 1
                east()
            elif choice == "i":
                valid = 1
                inv()
            elif choice == "s":
                valid = 1
                south()
            elif choice == "w":
                valid = 1
                west()
            elif choice == "m":
                print()
                print("           +------------+       +------------+")
                print("           |            | North |            |")
                print("           |  Building  |  Road |   Store    |")
                print("           |            |       |            |")
                print("           +-------  ---+       +---  -------+")
                print("+--------+                                     +--------+")
                print("|Crafting|                                     |        |")
                print("| Station|                                     |Building|")
                print("|                                                       |")
                print("|        |                                     |        |")
                print("+--------+                                     +--------+")
                print("  WEST                   X <--(You are Here)      EAST")
                print("+--------+                                     +--------+")
                print("|        |                                     |        |")
                print("| Home   |                                     |Building|")
                print("|                                                       |")
                print("|        |                                     |        |")
                print("+--------+                                     +--------+")
                print("           +-------  ---+       +---  -------+")
                print("           |            | South |            |")
                print("           |    Job     |  Road |   Shack    |")
                print("           |            |       |            |")
                print("           +------------+       +------------+")
                print()
                choice = str(input("> ")).lower()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def east():
    global destination
    destination = 2
    print("\n=====================")
    print("EAST TOWN SQUARE")
    print("=====================")
    print("There seems to be a store, a couple brick buildings, and a wooden shack...\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nStore(s)\nBuildings(b)\nShack(sh)\nBack to Town Square(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "s":
                valid = 1
                store()
            elif choice == "b":
                print("\nThese seem like really old buildings....\n")
                time.sleep(1.5)
                choice = str(input("> ")).lower()
            elif choice == "i":
                valid = 1
                inv()
            elif choice == "sh":
                valid = 1
                if startMission == 0:
                    shack1()
                elif startMission == 1:
                    shack2()
            elif choice == "t":
                valid = 1
                town()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def west():
    global destination
    destination = 3
    print("\n=====================")
    print("WEST TOWN SQUARE")
    print("=====================")
    print("There seems to be a neighborhood with my house...")
    time.sleep(1.5)
    print("And a store with a wooden sign that reads 'Crafting Station'...\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nYour House(h)\nCrafting Station(c)\nYour Job(j)\nBack to Town Square(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "h":
                valid = 1
                home()
            elif choice == "c":
                valid = 1
                craft()
            elif choice == "i":
                valid = 1
                inv()
            elif choice == "j":
                valid = 1
                job()
            elif choice == "t":
                valid = 1
                town()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def north():
    global destination
    destination = 4
    print("\n=====================")
    print("NORTHERN ROAD")
    print("=====================")
    print("This road seems to lead out of town...")
    time.sleep(1.5)
    print("it looks like it heading toward the base of the mountains ahead...")
    time.sleep(1.5)
    print("You arrive to the base and you notice there are some make-shift stairs leading up the mountain...")
    time.sleep(1.5)
    print("there are also some caves to your right...\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nUp the mountain(m)\nCaves(c)\nBack to town(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "m":
                valid = 1
                mountain()
            elif choice == "c":
                valid = 1
                cave()
            elif choice == "i":
                valid = 1
                inv()
            elif choice == "t":
                valid = 1
                town()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def south():
    global destination
    destination = 5
    print("\n=====================")
    print("SOUTHERN ROAD")
    print("=====================")
    print("This road leads into the forest...")
    time.sleep(1.5)
    print("The sign reads 'Sherwood Forest'...")
    time.sleep(1.5)
    print("You run into a fork in the road...\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nLeft(l)\nRight(r)\nBack to town(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "l":
                valid = 1
                left()
            elif choice == "r":
                valid = 1
                right()
            elif choice == "i":
                valid = 1
                inv()
            elif choice == "t":
                valid = 1
                town()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def shack1():
    global name
    global startMission
    print("\nOh, why hello there " + name + "...")
    time.sleep(1.5)
    print("Im glad you finally found me!\n")
    time.sleep(1.5)
    print("CHOICES:\nWhere am I?(1)\nWhat do I need to do to get back?(2)\nWho are you?(3)\nBack to town(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "1":
                print("You are in Longdale, it's a small village in eastern Europe and the year is 1440.\n")
                time.sleep(1.5)
                choice = str(input("> ")).lower()
            elif choice == "2":
                print("You see you will need to create a device...")
                time.sleep(1.5)
                print("This device's technology hasn't been invented yet however...")
                time.sleep(1.5)
                print("Although I think I know how you can create it...")
                time.sleep(1.5)
                print("You will need: Crystal, a Magic Glasyus Tree Leaf, Steel, and some Leather...")
                time.sleep(1.5)
                print("Come back to me once you have these items.\n")
                time.sleep(1.5)
                startMission = 1
                choice = str(input("> ")).lower()
            elif choice == "3":
                print("I can't exactly tell you that...\n")
                time.sleep(1.5)
                choice = str(input("> ")).lower()
            elif choice == "t":
                valid = 1
                east()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def shack2():
    print("Let's see how your doing...")
    time.sleep(1.5)
    if "Crystal" and "Magic Glasyus Tree Leaf" and "Steel" and "Leather" in inventory:
        end()
    else:
        print("You need Crystal, a Magic Glasyus Tree Leaf, Steel, and some Leather to create the device...")
        time.sleep(1.5)
        print("Keep adventuring to get back to your time, good luck!")
        time.sleep(1.5)
        east()


def home():
    global destination
    global name
    destination = 6
    print("\n=====================")
    print(name + "'S HOME")
    print("=====================")
    print("This must be your house...")
    time.sleep(1.5)
    print("It's not very big at all...\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nUpstairs(u)\nKitchen(k)\nBack to town(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "i":
                valid = 1
                inv()
            elif choice == "u":
                valid = 1
                upstairs()
            elif choice == "k":
                valid = 1
                kitchen()
            elif choice == "t":
                valid = 1
                west()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def kitchen():
    global destination
    destination = 7
    print("\n=====================")
    print(name + "'S KITCHEN")
    print("=====================")
    print("There's not a lot in here...")
    time.sleep(1.5)
    print("Just some pots...\n")
    time.sleep(1.5)
    print("CHOICES:\nInventory(i)\nBack to living room(b)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "i":
                valid = 1
                inv()
            elif choice == "b":
                valid = 1
                home()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def upstairs():
    global gold
    global destination
    destination = 8
    print("\n=====================")
    print(name + "'S BEDROOM")
    print("=====================")
    print("This is my bedroom...")
    time.sleep(1.5)
    if startMission == 0:
        print("There are just some random items in here I don't need right now...\n")
        time.sleep(1.5)
        print("CHOICES:\nInventory(i)\nBack to living room(b)\n")
        choice = str(input("> ")).lower()
        valid = 0
        while valid == 0:
            try:
                if choice == "i":
                    valid = 1
                    inv()
                elif choice == "b":
                    valid = 1
                    home()
                else:
                    choice = str(input("> ")).lower()
            except ValueError:
                choice = str(input("> ")).lower()
    else:
        print("I may need these items now...\n")
        time.sleep(1.5)
        print("CHOICES:\nInventory(i)\nTake items(t)\nBack to living room(b)\n")
        choice = str(input("> ")).lower()
        valid = 0
        while valid == 0:
            try:
                if choice == "i":
                    valid = 1
                    inv()
                elif choice == "b":
                    valid = 1
                    home()
                elif choice == "t":
                    print("You gained some string and 13 gold...\n")
                    time.sleep(1.5)
                    inventory.append("String")
                    gold += 13
                    choice = str(input("> ")).lower()
                else:
                    choice = str(input("> ")).lower()
            except ValueError:
                choice = str(input("> ")).lower()


def job():
    global name
    global gold
    print("\n=====================")
    print(name + "'S JOB")
    print("=====================")
    time.sleep(1.5)
    can = random.randint(0, 3)
    if can == 2:
        print("You get some of your work done...")
        time.sleep(1.5)
        print("You gained 5 gold from your boss.")
        time.sleep(1.5)
        gold += 5
        west()
    else:
        print("There's no work to do at the moment...")
        time.sleep(1.5)
        print("Try again later.")
        time.sleep(1.5)
        west()


def inv():
    global destination
    global name
    print()
    print("\n=====================")
    print(name + "'S INVENTORY")
    print("=====================")
    print()
    print("Gold:", gold)
    print()
    for i in inventory:
        print(str(inventory.index(i) + 1) + ". " + i)
    print()
    print("Press (b) to go back.")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "b":
                valid = 1
                if destination == 1:
                    town()
                elif destination == 2:
                    east()
                elif destination == 3:
                    west()
                elif destination == 4:
                    north()
                elif destination == 5:
                    south()
                elif destination == 6:
                    home()
                elif destination == 7:
                    kitchen()
                elif destination == 8:
                    upstairs()
                elif destination == 9:
                    cave()
                elif destination == 10:
                    mountain()
                else:
                    town()
        except ValueError:
            choice = str(input("> ")).lower()


def store():
    global gold
    print()
    print("===================================")
    print("      You are in the store")
    print(" To buy an item enter its number")
    print("      Or hit (b) to go back")
    print("==================================")
    print()
    print("Gold: ", gold)
    print()
    print("1. Food - 3 gold & Rocks")
    print("2. Leather - 16 gold & Crystal Necklace")
    print("3. Coat - 25 gold")
    print()
    choice = str(input("> "))
    valid = 0
    while valid == 0:
        try:
            if choice == "1":
                if "Food" in inventory:
                    print()
                    print("You already have food.")
                    print()
                    choice = str(input("> "))
                elif gold >= 3 and "Rocks" in inventory:
                    print()
                    print("You bought food")
                    gold -= 3
                    inventory.remove("Rocks")
                    inventory.append("Food")
                    print()
                    print("Gold: ", gold)
                    print()
                    choice = str(input("> "))
                else:
                    print()
                    print("You do not have enough items.")
                    choice = str(input("> "))
            elif choice == "2":
                if "Leather" in inventory:
                    print()
                    print("You already have leather.")
                    print()
                    choice = str(input("> "))
                elif gold >= 16 and "Crystal Necklace" in inventory:
                    print()
                    print("You bought leather")
                    inventory.append("Leather")
                    gold -= 16
                    inventory.remove("Crystal Necklace")
                    print("Gold: ", gold)
                    print()
                    print()
                    choice = str(input("> "))
                else:
                    print()
                    print("You do not have enough items.")
                    choice = str(input("> "))
            elif choice == "3":
                if "Coat" in inventory:
                    print()
                    print("You already have a coat.")
                    print()
                    choice = str(input("> "))
                elif gold >= 25:
                    print()
                    print("You bought a coat")
                    inventory.append("Coat")
                    gold -= 5
                    print()
                    print("Gold: ", gold)
                    print()
                    choice = str(input("> "))
                else:
                    print()
                    print("You do not have enough gold.")
                    choice = str(input("> "))
            elif choice == "b":
                valid = True
                east()
            else:
                choice = str(input("> "))
        except ValueError:
            choice = str(input("> "))


def craft():
    print("===================================")
    print("  You are in the Crafting Station")
    print(" To craft an item enter its number")
    print("      Or hit (b) to go back")
    print("==================================")
    print()
    print("1. Crystal Necklace - Crystal & String")
    print("2. Pickaxe - Rocks & Wood")
    print("3. Steel - Steel ore")
    print()
    choice = str(input("> "))
    valid = 0
    while valid == 0:
        try:
            if choice == "1":
                if "Crystal Necklace" in inventory:
                    print()
                    print("You already have a Crystal Necklace.")
                    print()
                    choice = str(input("> "))
                elif "Crystal" and "String" in inventory:
                    print()
                    print("You crafted a Crystal Necklace.")
                    inventory.remove("Crystal")
                    inventory.remove("String")
                    inventory.append("Crystal Necklace")
                    print()
                    choice = str(input("> "))
                else:
                    print()
                    print("You do not have enough items.\n")
                    choice = str(input("> "))
            elif choice == "2":
                if "Pickaxe" in inventory:
                    print()
                    print("You already have a pickaxe.")
                    print()
                    choice = str(input("> "))
                elif "Wood" and "Rocks" in inventory:
                    print()
                    print("You crafted a pickaxe")
                    inventory.remove("Wood")
                    inventory.remove("Rocks")
                    inventory.append("Pickaxe")
                    print()
                    choice = str(input("> "))
                else:
                    print()
                    print("You do not have enough items.\n")
                    choice = str(input("> "))
            elif choice == "3":
                if "Coat" in inventory:
                    print()
                    print("You already have a coat.")
                    print()
                    choice = str(input("> "))
                elif "Steel ore" in inventory:
                    print()
                    print("You gained steel.")
                    inventory.remove("Steel ore")
                    inventory.append("Steel")
                    print()
                    choice = str(input("> "))
                else:
                    print()
                    print("You do not have enough items.\n")
                    choice = str(input("> "))
            elif choice == "b":
                valid = True
                west()
            else:
                choice = str(input("> "))
        except ValueError:
            choice = str(input("> "))


def cave():
    global destination
    destination = 9
    print("\n=====================")
    print("CAVES")
    print("=====================")
    if startMission == 0:
        print("These caves look way to deep and dangerous...")
        time.sleep(1.5)
        print("There are a lot of loose rocks that I could get hurt on...\n")
        time.sleep(1.5)
        print("CHOICES:\nInventory(i)\nBack to road(b)\n")
        choice = str(input("> ")).lower()
        valid = 0
        while valid == 0:
            try:
                if choice == "i":
                    valid = 1
                    inv()
                elif choice == "b":
                    valid = 1
                    north()
                else:
                    choice = str(input("> ")).lower()
            except ValueError:
                choice = str(input("> ")).lower()
    elif startMission == 1:
        print("These caves look way to deep and dangerous...")
        time.sleep(1.5)
        print("There are a lot of loose rocks that I could get hurt on...")
        time.sleep(1.5)
        print("Maybe I could use these rocks!\n")
        time.sleep(1.5)
        print("CHOICES:\nInventory(i)\nBack to road(b)\nTake rocks(t)\n")
        choice = str(input("> ")).lower()
        valid = 0
        while valid == 0:
            try:
                if choice == "i":
                    valid = 1
                    inv()
                elif choice == "b":
                    valid = 1
                    north()
                elif choice == "t":
                    print("You gained rocks!\n")
                    inventory.append("Rocks")
                    time.sleep(1.5)
                    choice = str(input("> ")).lower()
                else:
                    choice = str(input("> ")).lower()
            except ValueError:
                choice = str(input("> ")).lower()


def mountain():
    global destination
    destination = 10
    print("\n=====================")
    print("MOUNTAIN")
    print("=====================")
    if "Pickaxe" in inventory:
        print("Its really cold up here I can't go any further up the mountain...")
        time.sleep(1.5)
        print("Now I can get the steel ore and crystal with my pickaxe...\n")
        time.sleep(1.5)
        print("CHOICES:\nInventory(i)\nBack to road(b)\nMine the steel ore(m)\nMine the crystal(c)\n")
        choice = str(input("> ")).lower()
        valid = 0
        while valid == 0:
            try:
                if choice == "i":
                    valid = 1
                    inv()
                elif choice == "b":
                    valid = 1
                    north()
                elif choice == "m":
                    print("You gained steel ore!\n")
                    inventory.append("Steel ore")
                    time.sleep(1.5)
                    choice = str(input("> ")).lower()
                elif choice == "c":
                    print("You gained crystal!\n")
                    inventory.append("Crystal")
                    time.sleep(1.5)
                    choice = str(input("> ")).lower()
                else:
                    choice = str(input("> ")).lower()
            except ValueError:
                choice = str(input("> ")).lower()
    else:
        print("It's really cold up here I can't go any further up the mountain...")
        time.sleep(1.5)
        print("There seems to be exposed steel ore and crystal...")
        time.sleep(1.5)
        print("I'd need a pickaxe to get it though...\n")
        time.sleep(1.5)
        print("CHOICES:\nInventory(i)\nBack to road(b)\n")
        choice = str(input("> ")).lower()
        valid = 0
        while valid == 0:
            try:
                if choice == "i":
                    valid = 1
                    inv()
                elif choice == "b":
                    valid = 1
                    north()
                else:
                    choice = str(input("> ")).lower()
            except ValueError:
                choice = str(input("> ")).lower()


def right():
    global destination
    destination = 12
    print("You head down the trail...")
    time.sleep(1.5)
    print("the trail splits again...\n")
    time.sleep(1.5)
    print("CHOICES:\nLeft(l)\nRight(r)\nBack to town(t)\n")
    choice = str(input("> ")).lower()
    valid = 0
    while valid == 0:
        try:
            if choice == "l":
                valid = 1
                correct = random.randint(0, 1)
                if correct == 1:
                    print("There's a trap!")
                    time.sleep(1.5)
                    print("Rocks come flying in from every direction!")
                    time.sleep(1.5)
                    print("One large rock hits you in the head and knocks you out...")
                    time.sleep(1.5)
                    print("...")
                    time.sleep(1.5)
                    print("...")
                    time.sleep(1.5)
                    print("You wake up in your home again with your head bandaged up...")
                    time.sleep(1.5)
                    home()
                else:
                    print("In the distance you see a figure standing next to a glowing tree...")
                    time.sleep(1.5)
                    print("You slowly approach it...")
                    time.sleep(1.5)
                    print("The figure yells your name!!!")
                    time.sleep(1.5)
                    print("You try running but you can't!")
                    time.sleep(1.5)
                    troll()
            elif choice == "r":
                valid = 1
                correct = random.randint(0, 1)
                if correct == 1:
                    print("There's a trap!")
                    time.sleep(1.5)
                    print("The ground falls beneath your feet!")
                    time.sleep(1.5)
                    print("When you hit the ground your head smashes in the ground knocking you out...")
                    time.sleep(1.5)
                    print("...")
                    time.sleep(1.5)
                    print("...")
                    time.sleep(1.5)
                    print("You wake up in your home again with your head bandaged up...")
                    time.sleep(1.5)
                    home()
                else:
                    print("In the distance you see a figure standing next to a glowing tree...")
                    time.sleep(1.5)
                    print("You slowly approach it...")
                    time.sleep(1.5)
                    print("The figure yells your name!!!")
                    time.sleep(1.5)
                    print("You try running but you can't!")
                    time.sleep(1.5)
                    troll()
            elif choice == "t":
                valid = 1
                town()
            else:
                choice = str(input("> ")).lower()
        except ValueError:
            choice = str(input("> ")).lower()


def left():
    global destination
    destination = 13
    print("You head down the trail...")
    time.sleep(1.5)
    if "Wood" in inventory:
        print("Hopefully that animal is gone...")
        time.sleep(1.5)
    else:
        print("There is a bundle of wood laying in the middle...")
        time.sleep(1.5)
        print("You pick it up and store it just in case you need it...")
        time.sleep(1.5)
        inventory.append("Wood")
    print("You see a cute animal...")
    time.sleep(1.5)
    print("It is a raccoon...")
    time.sleep(1.5)
    print("IT IS CRAZY! IT BITES YOU!")
    time.sleep(1.5)
    print("Everything goes blurry...")
    time.sleep(1.5)
    print("You don't feel very well...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("You wake up in your home again with the bite bandaged up...")
    time.sleep(1.5)
    home()


def troll():
    question = random.randint(0, 2)
    print("I've heard you need a Glasyus Tree leaf...")
    time.sleep(1.5)
    print("I am the guardian troll of this tree...")
    time.sleep(1.5)
    print("Only the sharpest may ge one of its magic leaves...")
    time.sleep(1.5)
    print("If you answer this question correctly you may have a leaf..")
    time.sleep(1.5)
    print("Ready...")
    time.sleep(1.5)
    if question == 0:
        print("Can you lift elephant with one hand? [Y or N]")
        answer = input("> ")
        valid = 0
        while valid == 0:
            try:
                if answer in ("Yes", "yes", "y", "Y"):
                    print("You are not worthy...")
                    time.sleep(1.5)
                    print("Try again later...")
                    time.sleep(1.5)
                    print("The troll zaps you and you black out...")
                    time.sleep(1.5)
                    print("You wake up in your house...")
                    time.sleep(1.5)
                    home()
                elif answer in ("No", "no", "n", "N"):
                    print("You got lucky...")
                    time.sleep(1.5)
                    print("I grant you one Glasyus Tree leaf...")
                    time.sleep(1.5)
                    print("Now get out of here...")
                    time.sleep(1.5)
                    print("The troll zaps you and you black out...")
                    time.sleep(1.5)
                    print("You wake up in your house...")
                    time.sleep(1.5)
                    inventory.append("Magic Glasyus Tree Leaf")
                    home()
                else:
                    answer = input("> ")
            except ValueError:
                answer = input("> ")
    elif question == 1:
        print("Does England have a 4th of July? [Y or N]")
        answer = input("> ")
        valid = 0
        while valid == 0:
            try:
                if answer in ("Yes", "yes", "y", "Y"):
                    print("You got lucky...")
                    time.sleep(1.5)
                    print("I grant you one Glasyus Tree leaf...")
                    time.sleep(1.5)
                    print("Now get out of here...")
                    time.sleep(1.5)
                    print("The troll zaps you and you black out...")
                    time.sleep(1.5)
                    print("You wake up in your house...")
                    time.sleep(1.5)
                    inventory.append("Magic Glasyus Tree Leaf")
                    home()
                elif answer in ("No", "no", "n", "N"):
                    print("You are not worthy...")
                    time.sleep(1.5)
                    print("Try again later...")
                    time.sleep(1.5)
                    print("The troll zaps you and you black out...")
                    time.sleep(1.5)
                    print("You wake up in your house...")
                    time.sleep(1.5)
                    home()
                else:
                    answer = input("> ")
            except ValueError:
                answer = input("> ")
    elif question == 2:
        print("Is a square a rectangle? [Y or N]")
        answer = input("> ")
        valid = 0
        while valid == 0:
            try:
                if answer in ("Yes", "yes", "y", "Y"):
                    print("You got lucky...")
                    time.sleep(1.5)
                    print("I grant you one Glasyus Tree leaf...")
                    time.sleep(1.5)
                    print("Now get out of here...")
                    time.sleep(1.5)
                    print("The troll zaps you and you black out...")
                    time.sleep(1.5)
                    print("You wake up in your house...")
                    time.sleep(1.5)
                    inventory.append("Magic Glasyus Tree Leaf")
                    home()
                elif answer in ("No", "no", "n", "N"):
                    print("You are not worthy...")
                    time.sleep(1.5)
                    print("Try again later...")
                    time.sleep(1.5)
                    print("The troll zaps you and you black out...")
                    time.sleep(1.5)
                    print("You wake up in your house...")
                    time.sleep(1.5)
                    home()
                else:
                    answer = input("> ")
            except ValueError:
                answer = input("> ")


def end():
    print("I see you have all of the items...")
    time.sleep(1.5)
    print("Congratulations....")
    time.sleep(1.5)
    print("Now give me a moment to create the device...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("You gain the device...")
    time.sleep(1.5)
    print("Your body begins to tingle as your vision gets blurry...")
    time.sleep(1.5)
    print("As your vision clears the sun is shining brightly into your eyes...")
    time.sleep(1.5)
    print("It's morning and you're in your apartment downtown...")
    time.sleep(1.5)
    print("Did that all really happen...?")
    time.sleep(1.5)
    print("Or was it just a dream...?")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("=====================")
    print("THANK YOU FOR PLAYING")
    print("=====================")
    time.sleep(5)
    quit()

intro()
