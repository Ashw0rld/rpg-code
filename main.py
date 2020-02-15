from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# create black magic
fire = Spell("fire", 10, 100, "black")
thunder = Spell("thunder", 10, 100, "black")
blizzard = Spell("blizzard", 10, 100, "black")
meteor = Spell("meteor", 60, 200, "black")
quake = Spell("quake", 14, 140, "black")

# create white magic
cure = Spell("cure", 12, 120, "white")
cura = Spell("cura", 18, 180, "white")

#create some items
potion = Item("Potion", "potion", "Heals for 50 HP.", 50)
hipotion = Item("HI-Potion", "potion", "Heals for 100 HP.", 100)
superpotion = Item("Super Potion", "potion", "Heals for 500 HP.", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member.", 9999)
megaelixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP.", 9999)

grenade = Item("Grenade", "attack", "Deals for 500 damage.", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cura, cure]
player_items = [{'item': potion, 'quantity': 15}, {'item': hipotion, 'quantity': 5}, {'item': superpotion, 'quantity': 5},
                {'item': elixer, 'quantity': 5}, {'item': megaelixer, 'quantity': 2}, {'item': grenade, 'quantity': 5}]

# instantiate people
player1 = Person("Ash", 461, 65, 60, 34, player_spells, player_items)
player2 = Person("Kun", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Anv", 416, 65, 60, 34, player_spells, player_items)
players = [player1, player2, player3]

enemy1 = Person("Gul", 700, 65, 45, 23, player_spells, player_items)
enemy2 = Person("Pnw", 700, 65, 45, 23, player_spells, player_items)
enemies = [enemy1, enemy2]

running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!!!' + bcolors.ENDC)

while running:
    print('===================')
    print(bcolors.BOLD + "NAME                         HP                                       MP")

    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:
        player.choose_action()
        choice = input('Choose action :- ')
        print('You chose ' + player.get_action(int(choice)))
        if int(choice) == 1:
            dmg = player.gen_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print('You attacked ' + enemies[enemy].name.replace(" ", "") + ' for ' + str(dmg) + ' point.')
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

        elif int(choice) == 2:
            player.choose_magic()
            mag = int(input('Choose magic :- ')) - 1

            if mag == -1:
                continue

            spell = player.magic[mag]
            mag_dmg = spell.gen_dmg()

            curr_mp = player.get_mp()

            if curr_mp < spell.cost:
                print(bcolors.FAIL + 'NOT ENOUGH MAGIC POINTS!' + bcolors.ENDC)
                continue

            player.red_mp(spell.cost)

            if spell.type1 == "white":
                player.heal(mag_dmg)
                print(bcolors.OKBLUE + spell.name + ' heals with ' + str(mag_dmg) + ' HP. ' + bcolors.ENDC)
            elif spell.type1 == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(mag_dmg)
                print(bcolors.OKBLUE + spell.name + ' deals with ' + str(mag_dmg) + ' points of damage.' + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

        elif int(choice) == 3:
            player.choose_item()
            item_choice = int(input("Choose Item :- ")) - 1

            item = player.items[item_choice]

            if item_choice == -1:
                continue

            if item['quantity'] == 0:
                print("This item is finished!")
                continue

            if item['item'].type == "potion":
                player.heal(item['item'].prop)
                print(item['item'].name + " heals for " + str(item['item'].prop) + " HP.")

            elif item['item'].type == "elixer":
                player.hp = player.get_maxhp()
                player.mp = player.get_maxmp()
                print("Your HP is " + str(player.get_hp()) + " and MP is " + str(player.get_mp()) + ".")

            elif item['item'].type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item['item'].prop)
                print(bcolors.WARNING + item['item'].name + " damages " + enemies[enemy].name.replace(" ", "")
                      + " with " + str(item['item'].prop) + " HP." + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

            item['quantity'] -= 1

        if len(enemies) == 0:
            print(bcolors.OKGREEN + 'YOU WIN!!!' + bcolors.ENDC)
            running = False
            break

        elif len(players) == 0:
            print(bcolors.FAIL + 'ENEMY HAS DEFEATED YOU!!!' + bcolors.ENDC)
            running = False
            break

    for enemy in enemies:
        enemy_choice = random.randrange(0, 3)

        if enemy_choice == 0:
            enm_dmg = enemy.gen_damage()
            target = random.randrange(0, 3)
            players[target].take_damage(enm_dmg)
            print(enemy.name + ' attacked ' + players[target].name.replace(" ", "") + ' for ' + str(enm_dmg) + ' point.')

        elif enemy_choice == 1:
            spell, mag_dmg = enemy.choose_enemy_spell()

            if spell.type1 == "white":
                enemy.heal(mag_dmg)
                print(bcolors.OKBLUE + spell.name + ' heals ' + enemy.name.replace(" ", "") + ' with ' + str(mag_dmg)
                      + ' HP. ' + bcolors.ENDC)

            elif spell.type1 == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(mag_dmg)
                print(enemy.name + " chose " + spell.name + " on " + players[target].name.replace(" ", "")
                      + " for a damage of " + str(mag_dmg) + " HP.")
                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]

        elif enemy_choice == 2:
            item = enemy.choose_enemy_item()

            if item['item'].type == "potion":
                enemy.heal(item['item'].prop)
                print(item['item'].name + " heals " + enemy.name.replace(" ", "") + " for " + str(item['item'].prop) +
                      " HP.")

            elif item['item'].type == "elixer":
                enemy.hp = enemy.get_maxhp()
                enemy.mp = enemy.get_maxmp()
                print(enemy.name.replace(" ", "") + "'s HP is " + str(enemy.get_hp()) + " and MP is " +
                      str(enemy.get_mp()) + ".")

            elif item['item'].type == "attack":
                target = random.randrange(0, 3)
                players[target].take_damage(item['item'].prop)
                print(enemy.name + " chose " + item['item'].name + " on " + players[target].name.replace(" ", "")
                      + " for a damage of " + item['item'].prop + " HP.")
                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]

            item['quantity'] -= 1









