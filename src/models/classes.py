from typing import Literal
from pydantic import Field
from src.enums.constants import BaseClass


class Barbarian(BaseClass):
    subclass: Literal[
        "None",
        "Berserker",
        "Bear Totem Warrior",
        "Eagle Totem Warrior",
        "Wolf Totem Warrior",
    ] = Field(default="None")


class Bard(BaseClass):
    subclass: Literal[
        "None",
        "Lore",
        "Valor",
    ] = Field(default="None")


class Cleric(BaseClass):
    subclass: Literal[
        "None",
        "Knowledge",
        "Life",
        "Light",
        "Nature",
        "Tempest",
        "Trickery",
        "War",
    ] = Field(default="None")


class Druid(BaseClass):
    subclass: Literal[
        "None",
        "Land",
        "Moon",
    ] = Field(default="None")


class Fighter(BaseClass):
    subclass: Literal[
        "None",
        "Battle Master",
        "Champion",
        "Eldritch Knight",
    ] = Field(default="None")


class Monk(BaseClass):
    subclass: Literal[
        "None",
        "Four Elements",
        "Open Hand",
        "Shadow",
    ] = Field(default="None")


class Paladin(BaseClass):
    subclass: Literal[
        "None",
        "Ancients",
        "Devotion",
        "Vengeance",
    ] = Field(default="None")


class Ranger(BaseClass):
    subclass: Literal[
        "None",
        "Beast Master",
        "Hunter",
    ] = Field(default="None")


class Rogue(BaseClass):
    subclass: Literal[
        "None",
        "Arcane Trickster",
        "Assassin",
        "Thief",
    ] = Field(default="None")


class Sorcerer(BaseClass):
    subclass: Literal[
        "None",
        "Draconic Bloodline",
        "Wild Magic",
    ] = Field(default="None")


class Warlock(BaseClass):
    subclass: Literal[
        "None",
        "Archfey",
        "Fiend",
        "Great Old One",
    ] = Field(default="None")


class Wizard(BaseClass):
    subclass: Literal[
        "None",
        "Abjuration",
        "Conjuration",
        "Diviniation",
        "Enchantment",
        "Evocation",
        "Illusion",
        "Necromancy",
        "Transmutation",
    ] = Field(default="None")
