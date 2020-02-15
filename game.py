import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']
        self.name = name

    def gen_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def red_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.FAIL + 'ACTIONS:' + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ':' + item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + 'MAGIC:' + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ':' + spell.name + '(cost: ' + str(spell.cost) + ')')
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + 'ITEMS:' + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + '. ' + bcolors.BOLD + item['item'].name + bcolors.ENDC + '(' + item['item'].descrip
                  + ') : x' + str(item['quantity']))
            i += 1

    def get_action(self, i):
        return self.actions[i-1]

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_enemy_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 50

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                             __________________________________________________")
        print(self.name + " :               " + current_hp + " |" + bcolors.FAIL +
              hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 25

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        if len(mp_string) < 5:
            decreased1 = 5 - len(mp_string)
            while decreased1 > 0:
                current_mp += " "
                decreased1 -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string
        print("                             _________________________                __________")
        print(self.name + " :               " + current_hp + " |" + bcolors.OKGREEN +
              hp_bar + bcolors.ENDC + "|        " + current_mp + " |" +
              bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_target(self, enemies):
        print(bcolors.FAIL + "TARGET:" + bcolors.ENDC)
        i = 1
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ":" + enemy.name)
                i += 1
        choice = int(input("Choose target :-")) - 1
        return choice

    def choose_enemy_spell(self):
        mag = random.randrange(0, len(self.magic))
        spell = self.magic[mag]
        mag_dmg = spell.gen_dmg()

        curr_mp = self.get_mp()

        if curr_mp < spell.cost:
            self.choose_enemy_spell()
        else:
            self.red_mp(spell.cost)
            return spell, mag_dmg

    def choose_enemy_item(self):
        item_choice = random.randrange(0, len(self.items))
        item = self.items[item_choice]
        if item['quantity'] == 0:
            self.choose_enemy_item()
        else:
            return item













