from pydantic import Field, model_validator
from typing import Literal

from src.enums.class_constants import (
    Armor,
    LightArmor,
    MediumArmor,
    HeavyArmor,
    Shield,
    BaseClass,
    HitDie,
    Skill,
    WeaponType,
)


# Barbarian
class Barbarian(BaseClass):
    name: Literal["Barbarian"] = "Barbarian"
    hit_die: HitDie = HitDie.D12
    primary_abilities: list[str] = Field(default_factory=lambda: ["strength"])
    saving_throws: list[str] = Field(
        default_factory=lambda: ["strength", "constitution"]
    )

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [
            Armor(armor_type=LightArmor()),
            Armor(armor_type=MediumArmor()),
            Armor(armor_type=Shield()),
        ]
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
                    raise ValueError(
                        f"'{skill}' is not a valid Barbarian skill choice."
                    )
        return self


# Bard
class Bard(BaseClass):
    name: Literal["Bard"] = "Bard"
    hit_die: HitDie = HitDie.D8
    primary_abilities: list[str] = Field(default_factory=lambda: ["charisma"])
    saving_throws: list[str] = Field(default_factory=lambda: ["dexterity", "charisma"])

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [Armor(armor_type=LightArmor())]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [
            WeaponType.SIMPLE_MELEE,
            WeaponType.MARTIAL_MELEE,
            WeaponType.MARTIAL_RANGED,
        ]
    )

    choose_skills: int = 3
    skill_options: list[Skill] = Field(default_factory=lambda: [s for s in Skill])
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
    hit_die: HitDie = HitDie.D8
    primary_abilities: list[str] = Field(default_factory=lambda: ["wisdom"])
    saving_throws: list[str] = Field(default_factory=lambda: ["wisdom", "charisma"])

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [
            Armor(armor_type=LightArmor()),
            Armor(armor_type=MediumArmor()),
            Armor(armor_type=Shield()),
        ]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [WeaponType.SIMPLE_MELEE]
    )

    choose_skills: int = 2
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.HIS,
            Skill.INS,
            Skill.MED,
            Skill.PER,
            Skill.REL,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Cleric":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Cleric skill choice.")
        return self


# Druid
class Druid(BaseClass):
    name: Literal["Druid"] = "Druid"
    hit_die: HitDie = HitDie.D8
    primary_abilities: list[str] = Field(default_factory=lambda: ["wisdom"])
    saving_throws: list[str] = Field(default_factory=lambda: ["intelligence", "wisdom"])

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [
            Armor(armor_type=LightArmor()),
            Armor(armor_type=MediumArmor()),
            Armor(armor_type=Shield()),
        ]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [WeaponType.SIMPLE_MELEE]
    )

    choose_skills: int = 2
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ARC,
            Skill.ANI,
            Skill.INS,
            Skill.MED,
            Skill.NAT,
            Skill.PER,
            Skill.REL,
            Skill.SUR,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Druid":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Druid skill choice.")
        return self


# Fighter
class Fighter(BaseClass):
    name: Literal["Fighter"] = "Fighter"
    hit_die: HitDie = HitDie.D10
    primary_abilities_list: list[str] = Field(
        default_factory=lambda: ["strength", "dexterity"]
    )
    primary_abilities: list[str] = Field(default_factory=list)
    choose_primary_abilities: int = 1

    saving_throws: list[str] = Field(
        default_factory=lambda: ["strength", "constitution"]
    )

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [
            Armor(armor_type=LightArmor()),
            Armor(armor_type=MediumArmor()),
            Armor(armor_type=HeavyArmor()),
            Armor(armor_type=Shield()),
        ]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [
            WeaponType.SIMPLE_MELEE,
            WeaponType.MARTIAL_MELEE,
            WeaponType.MARTIAL_RANGED,
        ]
    )

    choose_skills: int = 2
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ACR,
            Skill.ANI,
            Skill.ATH,
            Skill.HIS,
            Skill.INS,
            Skill.INT,
            Skill.PER,
            Skill.PEC,
            Skill.SUR,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_primary_abilities_and_skills(self) -> "Fighter":
        if self.primary_abilities:
            if len(self.primary_abilities) != self.choose_primary_abilities:
                raise ValueError(
                    f"Must choose exactly {self.choose_primary_abilities} primary abilities."
                )
            for ability in self.primary_abilities_list:
                if ability not in self.primary_abilities:
                    raise ValueError(
                        f"'{ability}' is not a valid Fighter ability choice."
                    )

        if self.choose_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Fighter skill choice.")
        return self


# Monk
class Monk(BaseClass):
    name: Literal["Monk"] = "Monk"
    hit_die: HitDie = HitDie.D8
    primary_abilities: list[str] = Field(
        default_factory=lambda: ["dexterity", "wisdom"]
    )
    saving_throws: list[str] = Field(default_factory=lambda: ["strength", "dexterity"])

    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [
            WeaponType.SIMPLE_MELEE,
            WeaponType.SIMPLE_RANGED,
        ]
    )


# Paladin
class Paladin(BaseClass):
    name: Literal["Paladin"] = "Paladin"
    hit_die: HitDie = HitDie.D10
    primary_abilities: list[str] = Field(
        default_factory=lambda: ["strength", "charisma"]
    )
    saving_throws: list[str] = Field(default_factory=lambda: ["wisdom", "charisma"])

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [
            Armor(armor_type=LightArmor()),
            Armor(armor_type=MediumArmor()),
            Armor(armor_type=HeavyArmor()),
            Armor(armor_type=Shield()),
        ]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [
            WeaponType.SIMPLE_MELEE,
            WeaponType.SIMPLE_RANGED,
            WeaponType.MARTIAL_MELEE,
            WeaponType.MARTIAL_RANGED,
        ]
    )

    choose_skills: int = 2
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ATH,
            Skill.INS,
            Skill.INT,
            Skill.MED,
            Skill.PES,
            Skill.REL,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Paladin":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Paladin skill choice.")
        return self


# Ranger
class Ranger(BaseClass):
    name: Literal["Ranger"] = "Ranger"
    hit_die: HitDie = HitDie.D10
    primary_abilities: list[str] = Field(
        default_factory=lambda: ["dexterity", "wisdom"]
    )
    saving_throws: list[str] = Field(default_factory=lambda: ["strength", "dexterity"])

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [
            Armor(armor_type=LightArmor()),
            Armor(armor_type=MediumArmor()),
            Armor(armor_type=Shield()),
        ]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [
            WeaponType.SIMPLE_MELEE,
            WeaponType.SIMPLE_RANGED,
            WeaponType.MARTIAL_MELEE,
            WeaponType.MARTIAL_RANGED,
        ]
    )

    choose_skills: int = 3
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ANI,
            Skill.ATH,
            Skill.INS,
            Skill.INV,
            Skill.NAT,
            Skill.PEC,
            Skill.STE,
            Skill.SUR,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Ranger":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Ranger skill choice.")
        return self


# Rogue
class Rogue(BaseClass):
    name: Literal["Rogue"] = "Rogue"
    hit_die: HitDie = HitDie.D8
    primary_abilities: list[str] = Field(default_factory=lambda: ["dexterity"])
    saving_throws: list[str] = Field(
        default_factory=lambda: ["dexterity", "intelligence"]
    )

    armor_proficiencies: list[Armor] = Field(
        default_factory=lambda: [Armor(armor_type=LightArmor())]
    )
    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [
            WeaponType.SIMPLE_MELEE,
            WeaponType.SIMPLE_RANGED,
            WeaponType.MARTIAL_MELEE,
            WeaponType.MARTIAL_RANGED,
        ]
    )

    choose_skills: int = 4
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ACR,
            Skill.ATH,
            Skill.DEC,
            Skill.INS,
            Skill.INT,
            Skill.INV,
            Skill.PEC,
            Skill.PES,
            Skill.SLE,
            Skill.STE,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Rogue":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Rogue skill choice.")
        return self


# Sorcerer
class Sorcerer(BaseClass):
    name: Literal["Sorcerer"] = "Sorcerer"
    hit_die: HitDie = HitDie.D6
    primary_abilities: list[str] = Field(default_factory=lambda: ["charisma"])
    saving_throws: list[str] = Field(
        default_factory=lambda: ["constitution", "charisma"]
    )

    weapon_proficiencies: list[WeaponType] = Field(
        default_factory=lambda: [WeaponType.SIMPLE_MELEE, WeaponType.SIMPLE_RANGED]
    )

    choose_skills: int = 2
    skill_options: list[Skill] = Field(
        default_factory=lambda: [
            Skill.ARC,
            Skill.DEC,
            Skill.INS,
            Skill.INT,
            Skill.PES,
            Skill.REL,
        ]
    )
    chosen_skills: list[Skill] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_skills(self) -> "Sorcerer":
        if self.chosen_skills:
            if len(self.chosen_skills) != self.choose_skills:
                raise ValueError(f"Must choose exactly {self.choose_skills} skills.")
            for skill in self.chosen_skills:
                if skill not in self.skill_options:
                    raise ValueError(f"'{skill}' is not a valid Sorcerer skill choice.")
        return self


# Warlock
class Warlock(BaseClass):
    name: Literal["Warlock"] = "Warlock"
    hit_die: HitDie = HitDie.D8


all_classes: list[str] = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    # "Warlock",
    # "Wizard",
]

"""
primary abilities:
Barbarian: Strength
Bard: Charisma
Cleric: Wisdom
Druid: Wisdom
Fighter: Strength or Dexterity
Monk: Dexterity & Wisdom
Paladin: Strength & Charisma
Ranger: Dexterity & Wisdom
Rogue: Dexterity
Sorcerer: Charisma
Warlock: Charisma
Wizard: Intelligence
"""
