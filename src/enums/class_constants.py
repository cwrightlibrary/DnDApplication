from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field


class HitDie(int, Enum):
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12


class ArmorType(str, Enum):
    LIGHT = "Light"
    MEDIUM = "Medium"
    HEAVY = "Heavy"
    SHIELD = "Shield"


class WeaponType(str, Enum):
    SIMPLE_MELEE = "Simple Melee"
    SIMPLE_RANGED = "Simple Ranged"
    MARTIAL_MELEE = "Martial Melee"
    MARTIAL_RANGED = "Martial Ranged"


class Skill(str, Enum):
    ACR = "Acrobatics"
    ANI = "Animal Handling"
    ARC = "Arcana"
    ATH = "Athletics"
    DEC = "Deception"
    HIS = "History"
    INT = "Intimidation"
    INV = "Investigation"
    MED = "Medicine"
    NAT = "Nature"
    PEC = "Perception"
    PER = "Performance"
    PES = "Persuasion"
    REL = "Religion"
    SLE = "Sleight of Hand"
    STE = "Stealth"
    SUR = "Survival"


class BaseClass(BaseModel):
    name: str
    hit_die: HitDie
    primary_abilities: list[str]
    saving_throws: list[str]

    armor_proficiencies: list[ArmorType] = Field(default_factory=list)
    weapon_proficiencies: list[WeaponType] = Field(default_factory=list)
    tool_proficiencies: list[str] = Field(default_factory=list)
