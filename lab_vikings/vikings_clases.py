# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health = self.health - damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, viking):
        self.viking_army = self.viking_army.append(viking)

    def add_saxon(self, saxon):
        self.saxon_army = self.saxon_army.append(saxon)

    def viking_attack(self):
        saxon_selected = random.choice(self.saxon_army)
        viking_selected = random.choice(self.viking_army)
        hit = saxon_selected.receive_damage(viking_selected.strength)
        if saxon_selected.health <= 0:
            self.saxon_army.remove(saxon_selected)
            return hit

    def saxon_attack(self):
        saxon_selected = random.choice(self.saxon_army)
        viking_selected = random.choice(self.viking_army)
        hit = viking_selected.receive_damage(saxon_selected.strength)
        if viking_selected.health <= 0:
            self.viking_army.remove(viking_selected)
            return hit

    def show_status(self):
        if self.saxon_army == 0:
            return "Vikings have won the war of the century!"
        if self.viking_army == 0:
            return "Saxons have fought for their lives and survive another day..."
        if self.saxon_army == 1 and self.viking_army == 1:
            return "Vikings and Saxons are still in the trick of battle."
