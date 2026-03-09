from typing import Annotated, Literal
from pydantic import Field, computed_field, model_validator

from src.enums.race_constants import (
    Ability,
    AgeRange,
    BaseRace,
    BreathShape,
    DamageType,
    DraconicAncestry,
    DwarfToolProficiences,
    DwarfWeaponProficiencies,
    HeightAndWeight,
    Size,
)


# Dragonborn
class Dragonborn(BaseRace):
    name: Literal["Dragonborn"] = "Dragonborn"
    ancestry: DraconicAncestry

    ability: Ability = Field(default_factory=lambda: Ability(strength=2, charisma=1))
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


# Dwarf
class Dwarf(BaseRace):
    name: Literal["Dwarf"] = "Dwarf"

    ability: Ability = Field(default_factory=lambda: Ability(constitution=2))
    speed: Annotated[int, Field(ge=10, le=40)] = 25
    darkvision: int = 60
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=350))
    tool_proficiencies: DwarfToolProficiences
    weapon_proficiencies: DwarfWeaponProficiencies
    resistance: DamageType = DamageType.POISON
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Dwarvish"]
    )


# Elf
class Elf(BaseRace):
    name: Literal["Elf"] = "Elf"

    ability: Ability = Field(default_factory=lambda: Ability(dexterity=2))
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=100, max=750))
    darkvision: int = 60
    skill_proficiencies: list[str] = Field(default_factory=lambda: ["Perception"])
    language_proficiencies: list[str] = Field(
        default_factory=lambda: ["Common", "Elvish"]
    )


# Gnome
class Gnome(BaseRace):
    name: Literal["Gnome"] = "Gnome"
    size: Size = Field(default_factory=lambda: Size.SMALL)

    speed: Annotated[int, Field(ge=10, le=40)] = 25
    ability: Ability = Field(default_factory=lambda: Ability(intelligence=2))
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
    ability: Ability = Field(default_factory=lambda: Ability(charisma=2))
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

        return self


# Half-Orc
class HalfOrc(BaseRace):
    name: Literal["Half-Orc"] = "Half-Orc"
    ability: Ability = Field(
        default_factory=lambda: Ability(strength=1, constitution=1)
    )

    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=58, height_mod="2d10", weight=140, weight_mod="2d6"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=14, max=75))
    skill_proficiencies: list[str] = Field(default_factory=lambda: ["Intimidation"])
    language_proficiencies: list[str] = Field(default_factory=lambda: ["Common", "Orc"])
    darkvision: int = 60


# Halfling
class Halfling(BaseRace):
    name: Literal["Halfling"] = "Halfling"
    size: Size = Size.SMALL
    speed: Annotated[int, Field(ge=10, le=40)] = 25

    ability: Ability = Field(default_factory=lambda: Ability(dexterity=2))
    height_and_weight: HeightAndWeight = Field(
        default_factory=lambda: HeightAndWeight(
            height=31, height_mod="2d4", weight=35, weight_mod="None"
        )
    )
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=250))
    language_proficiencies: list[str] = Field(default_factory=lambda: ["Common", "Halfling"])


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
    