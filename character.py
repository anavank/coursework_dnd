
import json

class Character(object):
    def __init__(self, name=None, backstory=None, category=None, items=None, abilities=None, max_health=None, stats=None):
        self.name = name
        self.backstory = backstory
        self.category = category  # the word 'class' is a reserved keyword, so the solution is to use the word 'category'
        self.items = items
        self.abilities = abilities
        self.max_health = max_health
        self.stats = stats

    def set_name(self, name):
        self.name = name

    def set_back_story(self, back_story):
        self.backstory = back_story

    def get_stats(self):
        return self.stats

    def display_info(self):
        print("Name: ", self.name)
        print("Class: ", self.category)
        print("Max Health: ", self.max_health)
        print("Backstory: ", self.backstory)
        print("Inventory: ", self.items)
        print("Abilities: ", self.abilities)
        print("Stats: ", self.stats)

class CharacterBuilder:
    def get_name(self):
        pass

    def get_backstory(self):
        pass

    def get_category(self):
        pass

    def get_items(self):
        pass

    def get_abilities(self):
        pass

    def get_max_health(self):
        pass

    def get_stats(self):
        pass


# Concrete builder
class WarriorBuilder(CharacterBuilder):
    def get_category(self):
        return "Warrior"

    def get_items(self):
        return ["Axe", "Chainmail", "Helmet", "Testosterone"]

    def get_abilities(self):
        return ["Berserk", "Impenetrable", "Permanent hangover"]

    def get_max_health(self):
        return 300

    def get_stats(self):
        stats = {
            "STR": 50,
            "DEX": -1,
            "INT": 5,
            "WIS": 300
        }
        return stats


# Concrete builder
class WizardBuilder(CharacterBuilder):
    def get_category(self):
        return "Wizard"

    def get_items(self):
        return ["Magic wand", "Wizard's hat", "Estrogen"]

    def get_abilities(self):
        return ["Turn water into wine", "Cry", "Die for our sins"]

    def get_max_health(self):
        return 100

    def get_stats(self):
        stats = {
            "STR": 1,
            "DEX": -1,
            "INT": 1,
            "WIS": 1
        }
        return stats