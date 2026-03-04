# Name: David Haim Liav lugasi ID: 213007271

import random

class Warrior:
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack

    def __repr__(self):
        return f"Warrior(name={self.name}, hp={self.hp}, defense={self.defense}, attack={self.attack})"

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        if enemy.defense > 0:
            damage = min(self.attack, enemy.defense)
            enemy.defense -= damage
        else:
            enemy.hp -= self.attack

        enemy.defense = max(enemy.defense, 0)
        enemy.hp = max(enemy.hp, 0)

        print(f"{self.name} attacks {enemy.name}! {enemy.name} now has {enemy.hp} HP and {enemy.defense} defense.")

    def special_move(self, enemy):
        if self.is_alive():
            damage = self.attack * 2
            if enemy.defense > 0:
                damage_dealt = min(damage, enemy.defense)
                enemy.defense -= damage_dealt
            else:
                enemy.hp -= damage

            enemy.defense = max(enemy.defense, 0)
            enemy.hp = max(enemy.hp, 0)

            if self.defense > 0:
                self.defense = max(self.defense - 10, 0)
            else:
                self.hp = max(self.hp - 10, 0)

            print(f"{self.name} uses Special Move on {enemy.name}! {enemy.name} now has {enemy.hp} HP and {enemy.defense} defense.")


class Mage:
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack

    def __repr__(self):
        return f"Mage(name={self.name}, hp={self.hp}, defense={self.defense}, attack={self.attack})"

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        if enemy.defense > 0:
            damage = min(self.attack, enemy.defense)
            enemy.defense -= damage
        else:
            enemy.hp -= self.attack

        enemy.defense = max(enemy.defense, 0)
        enemy.hp = max(enemy.hp, 0)

        print(f"{self.name} attacks {enemy.name}! {enemy.name} now has {enemy.hp} HP and {enemy.defense} defense.")

    def special_move(self, enemy):
        self.hp += 10
        if enemy.defense > 0:
            enemy.defense = max(enemy.defense - 5, 0)
        else:
            enemy.hp = max(enemy.hp - 5, 0)
        print(
            f"{self.name} uses Special Move! {self.name} now has {self.hp} HP. {enemy.name} has {enemy.hp} HP and {enemy.defense} defense.")


class Game:
    def __init__(self, name):
        self.name = name
        self.characters = []

    def add_player(self, character):
        if isinstance(character, (Warrior, Mage)):
            self.characters.append(character)
        else:
            raise ValueError("Only Warrior or Mage can be added to the game.")

    def remove_player(self, name):
        self.characters = [c for c in self.characters if c.name != name]

    def battle(self, name1, name2):
        player1 = next((c for c in self.characters if c.name == name1), None)
        player2 = next((c for c in self.characters if c.name == name2), None)

        if not player1 or not player2:
            print("One or both players not found in the game.")
            return

        while player1.is_alive() and player2.is_alive():
            action = random.randint(0, 3)
            if action == 0:
                player1.attack_enemy(player2)
            elif action == 1:
                player2.attack_enemy(player1)
            elif action == 2 and isinstance(player1, (Warrior, Mage)):
                player1.special_move(player2)
            elif action == 3 and isinstance(player2, (Warrior, Mage)):
                player2.special_move(player1)

            print(f"Status: {player1}, {player2}")

        winner = player1 if player1.is_alive() else player2
        print(f"{winner.name} wins the battle!")

    def __repr__(self):
        return f"Game(name={self.name}, characters={self.characters})"



warrior1 = Warrior("Son Goku", 20000, 10000, 1000)
warrior2 = Warrior("Monkey D.Luffy", 5400, 3500, 510)
mage1 = Mage("Sung Jin-Woo", 12000, 4000, 800)
mage2 = Mage("Aizen", 3600, 3000, 420)

game1 = Game("Anime Battle Royale")

game1.add_player(warrior1)
game1.add_player(warrior2)
game1.add_player(mage1)
game1.add_player(mage2)

print(game1)

game1.battle("Sung Jin-Woo", "Monkey D.Luffy")

game1.battle("Son Goku", "Aizen")


print(game1)

