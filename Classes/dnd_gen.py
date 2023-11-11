import random


def modifier(stat: int) -> int:
    return ((stat - 10) // 2)

class Character:
    """Representation of a Dungeons & Dragons character"""
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return Character.roll(4, 3)

    @staticmethod
    def roll(num_dice: int, dice_kept: int = -1, dye_total: int = 6) -> int:

        result = sorted(random.randint(1, dye_total) for _ in range(num_dice))

        return (sum(result[num_dice - dice_kept:]) 
                if 0 <= dice_kept <= num_dice 
                else sum(result))

