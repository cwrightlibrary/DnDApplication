from pydantic import Field, model_validator
from typing import Literal

from src.enums.class_constants import ArmorType, BaseClass, HitDie, Skill, WeaponType


# Barbarian
class Barbarian(BaseClass):
    name: Literal["Barbarian"] = "Barbarian"
    hit_die: HitDie = HitDie.D12
    primary_abilities: list[str] = Field(default_factory=lambda: ["strength"])
    saving_throws: list[str] = Field(default_factory=lambda: ["strength", "constitution"])

    armor_proficiencies: list[ArmorType] = Field(
        default_factory=lambda: [ArmorType.LIGHT, ArmorType.MEDIUM, ArmorType.SHIELD]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [WeaponType.SIMPLE_MELEE, WeaponType.MARTIAL_MELEE]
    )

    choose_skills: int = 2
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ANI,
            Skill.ATH,
            Skill.INT,
            Skill.NAT,
            Skill.PER,
            Skill.SUR,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Barbarian":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Barbarian skill choice.")
        return self
    

# Bard
class Bard(BaseClass):
    name: Literal["Bard"] = "Bard"
    hit_die: HitDie = HitDie.D8
    primary_abilities: list[str] = Field(default_factory=lambda: ["charisma"])
    saving_throws: list[str] = Field(default_factory=lambda: ["dexterity", "charisma"])

    armor_proficiencies: list[ArmorType] = Field(
        default_factory=lambda: [ArmorType.LIGHT]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [WeaponType.SIMPLE_MELEE, WeaponType.MARTIAL_MELEE, WeaponType.MARTIAL_RANGED]
    )

    choose_skills: int = 3
    skill_options: list[Skill] = Field(
        default_factory=lambda: [s for s in Skill]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Bard":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Bard skill choice.")
        return self


# Cleric
class Cleric(BaseClass):
    name: Literal["Cleric"] = "Cleric"
    