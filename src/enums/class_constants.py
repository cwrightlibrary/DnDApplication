from enum import Enum
from pydantic import BaseModel, Field
from typing import Literal, Union


class HitDie(int, Enum):
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12


class LightArmor(BaseModel):
    padded: int = 11
    leather: int = 11
    studded_leather: int = 12

    active_armor: Literal["padded", "leather", "studded_leather"] = "padded"


class MediumArmor(BaseModel):
    hide: int = 12
    chain_shirt: int = 13
    scale_mail: int = 14
    breastplate: int = 14
    half_plate: int = 15

    active_armor: Literal["hide", "chain_shirt", "scale_mail", "breastplate", "half_plate"] = "hide"


class HeavyArmor(BaseModel):
    ring_mail: int = 14
    chain_mail: int = 16
    splint: int = 17
    plate: int = 18

    active_armor: Literal["ring_mail", "chain_mail", "splint", "plate"] = "ring_mail"


class Shield(BaseModel):
    shield: int = 10


class Armor(BaseModel):
    armor_type: Union[
        LightArmor,
        MediumArmor,
        HeavyArmor,
        Shield
    ]


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
    INS = "Insight"
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

    armor_proficiencies: list[Armor] = Field(default_factory=list)
    weapon_proficiencies: list[WeaponType] = Field(default_factory=list)
    tool_proficiencies: list[str] = Field(default_factory=list)
