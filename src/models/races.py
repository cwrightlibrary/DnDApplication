from src.enums.constants import BaseRace

from pydantic import Field
from typing import Dict, List, Literal


class Dragonborn(BaseRace):
    size: Literal["Medium"] = "Medium"
    speed: int = Field(ge=1, le=100, default=30)
    draconic_ancestry: Literal[
        "Black",
        "Blue",
        "Brass",
        "Bronze",
        "Copper",
        "Gold",
        "Green",
        "Red",
        "Silver",
        "White",
    ] = "Black"
    damage_type: Literal["Acid", "Lightning", "Fire", "Poison", "Cold"] = "Acid"
    breath_weapon: Literal["5x30 line", "15 cone"] = "5x30 line"

    def modifiers(self) -> None:
        self.abilities.strength += 2
        self.abilities.charisma += 1

        ancestry_damage: Dict[
            Literal[
                "Black",
                "Blue",
                "Brass",
                "Bronze",
                "Copper",
                "Gold",
                "Green",
                "Red",
                "Silver",
                "White",
            ],
            Literal["Acid", "Lightning", "Fire", "Poison", "Cold"],
        ] = {
            "Black": "Acid",
            "Blue": "Lightning",
            "Brass": "Fire",
            "Bronze": "Lightning",
            "Copper": "Acid",
            "Gold": "Fire",
            "Green": "Poison",
            "Red": "Fire",
            "Silver": "Cold",
            "White": "Cold",
        }

        ancestry_weapon: Dict[
            Literal[
                "Black",
                "Blue",
                "Brass",
                "Bronze",
                "Copper",
                "Gold",
                "Green",
                "Red",
                "Silver",
                "White",
            ],
            Literal["5x30 line", "15 cone"],
        ] = {
            "Black": "5x30 line",
            "Blue": "5x30 line",
            "Brass": "5x30 line",
            "Bronze": "5x30 line",
            "Copper": "5x30 line",
            "Gold": "15 cone",
            "Green": "15 cone",
            "Red": "15 cone",
            "Silver": "15 cone",
            "White": "15 cone",
        }

        self.damage_type = ancestry_damage[self.draconic_ancestry]
        self.breath_weapon = ancestry_weapon[self.draconic_ancestry]


class Dwarf(BaseRace):
    size: Literal["Medium"] = "Medium"
    speed: int = Field(ge=1, le=100, default=25)
    subrace: Literal["None", "Hill", "Mountain"] = "None"
    darkvision: int = 60
    dwarven_resilience: Dict[
        Literal["Saving Throws", "Resistance"], Literal["Poison"]
    ] = {
        "Saving Throws": "Poison",
        "Resistance": "Poison",
    }
    languages: List[str] = ["Common", "Dwarvish"]

    def modifiers(self) -> None:
        self.abilities.constitution += 2

        if self.subrace == "Hill":
            self.abilities.wisdom += 1
        elif self.subrace == "Mountain":
            self.abilities.strength += 2


class Elf(BaseRace):
    size: Literal["Medium"] = "Medium"
    speed: int = Field(ge=1, le=100, default=30)
    subrace: Literal["None", "Drow", "High", "Wood"] = "None"
    darkvision: int = 60
    languages: List[str] = ["Common", "Elvish"]

    def modifiers(self) -> None:
        if self.subrace == "Drow":
            self.abilities.charisma += 1
        elif self.subrace == "High":
            self.abilities.intelligence += 1
        elif self.subrace == "Wood":
            self.abilities.wisdom += 1


class Gnome(BaseRace):
    size: Literal["Small"] = "Small"
    speed: int = Field(ge=1, le=100, default=25)
    subrace: Literal["None", "Forest", "Rock"] = "None"
    languages: List[str] = ["Common", "Gnomish"]

    def modifiers(self) -> None:
        self.abilities.intelligence += 2
        if self.subrace == "Forest":
            self.abilities.dexterity += 1
        elif self.subrace == "Rock":
            self.abilities.constitution += 1


class HalfElf(BaseRace):
    size: Literal["Medium"] = "Medium"
    speed: int = Field(ge=1, le=100, default=30)
    darkvision: int = 60
    languages: List[str] = ["Common", "Elvish"]

    def modifiers(
        self,
        ability_add: Literal[
            "strength", "dexterity", "constitution", "intelligence", "wisdom"
        ],
        num_abilities_add: int = 1,
    ) -> None:
        self.abilities.charisma += 2
        can_add: List[
            Literal["strength", "dexterity", "constitution", "intelligence", "wisdom"]
        ] = ["strength", "dexterity", "constitution", "intelligence", "wisdom"]
        for i in range(0, num_abilities_add + 1):
            if ability_add in can_add:
                if ability_add == "strength":
                    self.abilities.strength += 1
                elif ability_add == "dexterity":
                    self.abilities.dexterity += 1
                elif ability_add == "constitution":
                    self.abilities.constitution += 1
                elif ability_add == "intelligence":
                    self.abilities.intelligence += 1
                elif ability_add == "wisdom":
                    self.abilities.wisdom += 1
                can_add.remove(ability_add)
