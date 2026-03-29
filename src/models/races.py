from typing import Annotated, Literal
from pydantic import Field, computed_field, model_validator

from src.enums.race_constants import (
    AdditionalSpells,
    AgeRange,
    BaseRace,
    BreathShape,
    DamageType,
    DraconicAncestry,
    DwarfToolProficiences,
    DwarfWeaponProficiencies,
    HeightAndWeight,
    Size,
    SpellLimit,
)


# Dragonborn
class Dragonborn(BaseRace):
    name: Literal["Dragonborn"] = "Dragonborn"
    ancestry: DraconicAncestry

    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=66, height_mod="2d8", weight=175, weight_mod="2d6"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=15, max=80))
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Draconic"]
    )

    @computed_field
    @property
    def resistances(self) -> list[DamageType]:
        return [self.ancestry.damage_type]

    @computed_field
    @property
    def breath_weapon(self) -> BreathShape:
        return self.ancestry.breath_weapon

    @model_validator(mode="after")
    def ability_add(self) -> "Dragonborn":
        self.ability.strength += 2
        self.ability.charisma += 1
        return self


# Dwarf
class Dwarf(BaseRace):
    name: Literal["Dwarf"] = "Dwarf"

    speed: Annotated[int, Field(ge=10, le=40)] = 25
    darkvision: int = 60
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=350))
    tool_proficiencies: list[DwarfToolProficiences] = Field(default_factory=lambda: [p for p in DwarfToolProficiences])
    weapon_proficiencies: list[DwarfWeaponProficiencies] = Field(default_factory=lambda: [p for p in DwarfWeaponProficiencies])
    resistance: DamageType = DamageType.POISON
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Dwarvish"]
    )

    @model_validator(mode="after")
    def ability_add(self) -> "Dwarf":
        self.ability.constitution += 2
        return self


# Elf
class Elf(BaseRace):
    name: Literal["Elf"] = "Elf"

    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=100, max=750))
    darkvision: int = 60
    skill_proficiencies: list[str] = Field(default_factory=lambda: ["Perception"])
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Elvish"]
    )

    @model_validator(mode="after")
    def ability_add(self) -> "Elf":
        self.ability.dexterity += 2
        return self


# Gnome
class Gnome(BaseRace):
    name: Literal["Gnome"] = "Gnome"
    size: Size = Field(default_factory=lambda: Size.SMALL)

    speed: Annotated[int, Field(ge=10, le=40)] = 25
    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=35, height_mod="2d4", weight=35, weight_mod="None"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=40, max=500))
    darkvision: int = 60
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Gnomish"]
    )

    @model_validator(mode="after")
    def ability_add(self) -> "Gnome":
        self.ability.intelligence += 2
        return self


# Half-Elf
class HalfElf(BaseRace):
    name: Literal["Half-Elf"] = "Half-Elf"
    choose_abilities: int = 2
    chosen_abilities: list[
        Literal["strength", "dexterity", "constitution", "intelligence", "wisdom"]
    ]
    choose_skills: int = 2
    # chosen_skills: list[Literal[""]]

    speed: Annotated[int, Field(ge=10, le=40)] = 30
    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=57, height_mod="2d8", weight=110, weight_mod="2d4"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=180))
    darkvision: int = 60
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Elvish"]
    )

    @model_validator(mode="after")
    def apply_chosen_abilities(self) -> "HalfElf":
        if len(self.chosen_abilities) != self.choose_abilities:
            raise ValueError(f"Must choose exactly {self.choose_abilities} abilities")

        for attr_name in self.chosen_abilities:
            current_val = getattr(self.ability, attr_name)
            setattr(self.ability, attr_name, current_val + 1)

        self.ability.charisma += 2
        return self


# Half-Orc
class HalfOrc(BaseRace):
    name: Literal["Half-Orc"] = "Half-Orc"

    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=58, height_mod="2d10", weight=140, weight_mod="2d6"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=14, max=75))
    skill_proficiencies: list[str] = Field(default_factory=lambda: ["Intimidation"])
    language_proficiencies: list[str] = Field(default_factory=lambda: ["Common", "Orc"])
    darkvision: int = 60

    @model_validator(mode="after")
    def ability_add(self) -> "HalfOrc":
        self.ability.strength += 1
        self.ability.constitution += 1
        return self


# Halfling
class Halfling(BaseRace):
    name: Literal["Halfling"] = "Halfling"
    size: Size = Size.SMALL
    speed: Annotated[int, Field(ge=10, le=40)] = 25

    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=31, height_mod="2d4", weight=35, weight_mod="None"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=250))
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Halfling"]
    )

    @model_validator(mode="after")
    def ability_add(self) -> "Halfling":
        self.ability.dexterity += 2
        return self


# Human
class Human(BaseRace):
    name: Literal["Human"] = "Human"

    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=56, height_mod="2d10", weight=110, weight_mod="2d4"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=100))
    language_proficiencies: list[str] = Field(default_factory=lambda: ["Common"])

    @model_validator(mode="after")
    def ability_add(self) -> "Human":
        self.ability.strength += 1
        self.ability.dexterity += 1
        self.ability.constitution += 1
        self.ability.intelligence += 1
        self.ability.wisdom += 1
        self.ability.charisma += 1
        return self


# Tiefling
class Tiefling(BaseRace):
    name: Literal["Tiefling"] = "Tiefling"

    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=57, height_mod="2d8", weight=110, weight_mod="2d4"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=100))
    darkvision: int = 60
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Infernal"]
    )
    resist: list[str] = Field(default_factory=lambda: ["Fire"])
    additional_spells: AdditionalSpells = Field(
        default_factory=lambda: AdditionalSpells(
            innate={
                "3": SpellLimit(daily={"1": ["Hellish Rebuke"]}),
                "5": SpellLimit(daily={"1": ["Darkness"]}),
            },
            ability="charisma",
            known={
                "1": ["Thaumaturgy"],
            },
        )
    )

    @model_validator(mode="after")
    def ability_add(self) -> "Tiefling":
        self.ability.charisma += 2
        self.ability.intelligence += 1
        return self


all_races: list[str] = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Half-Orc",
    "Halfling",
    "Human",
    "Tiefling",
]
