from typing import Annotated, Literal
from pydantic import Field, computed_field

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

    # Resistance and breath weapons
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

    speed: Annotated[int, Field(ge=10, le=40)] = 30
    ability: Ability = Field(default_factory=lambda: Ability(charisma=2))
    height_and_weight: HeightAndWeight = Field(default_factory=lambda: HeightAndWeight(height=57, height_mod="2d8", weight=110, weight_mod="2d4"))
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=20, max=180))
    darkvision: int = 60
    language_proficiencies: list[str] = Field(default_factory=lambda: ["Common", "Elvish"])
    