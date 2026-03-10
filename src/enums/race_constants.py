from enum import Enum
from typing import Annotated, Optional
from pydantic import BaseModel, Field

from src.helpers.roll_dice import roll_dice


# All categories
AbilityScore = Annotated[int, Field(ge=0, le=30, default=0)]


class Ability(BaseModel):
    strength: AbilityScore = roll_dice()
    dexterity: AbilityScore = roll_dice()
    constitution: AbilityScore = roll_dice()
    intelligence: AbilityScore = roll_dice()
    wisdom: AbilityScore = roll_dice()
    charisma: AbilityScore = roll_dice()

    def get_modifier(self, stat_value: int) -> int:
        return (stat_value - 10) // 2


class Skills(str, Enum):
    ACR = "Acrobatics"
    ANM = "Animal Handling"
    ARC = "Arcane"
    ATH = "Athletics"
    DEC = "Deception"
    HIS = "History"
    INS = "Insight"
    INT = "Intimidation"
    INV = "Investigation"
    MED = "Medicine"
    NAT = "Nature"
    PER = "Perception"
    PEF = "Performance"
    PES = "Persuasion"
    REL = "Religion"
    SLE = "Sleight of Hand"
    STE = "Stealth"
    SUR = "Survival"


class HeightAndWeight(BaseModel):
    height: Annotated[int, Field(ge=1, le=200)] = 50
    height_mod: str
    weight: Annotated[int, Field(ge=1, le=1_000)] = 100
    weight_mod: str


class AgeRange(BaseModel):
    mature: int
    max: int


class Size(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"


class DamageType(str, Enum):
    ACID = "Acid"
    COLD = "Cold"
    FIRE = "Fire"
    LIGHTNING = "Lightning"
    POISON = "Poison"


# Dragonborn
class BreathShape(str, Enum):
    LINE = "5x30 ft line"
    CONE = "15 ft cone"


# Encapsulate mapping logic
class DraconicAncestry(str, Enum):
    BLACK = "Black"
    BLUE = "Blue"
    BRASS = "Brass"
    BRONZE = "Bronze"
    COPPER = "Copper"
    GOLD = "Gold"
    GREEN = "Green"
    RED = "Red"
    SILVER = "Silver"
    WHITE = "White"

    @property
    def damage_type(self) -> DamageType:
        mapping = {
            "Black": DamageType.ACID,
            "Blue": DamageType.LIGHTNING,
            "Brass": DamageType.FIRE,
            "Bronze": DamageType.LIGHTNING,
            "Copper": DamageType.ACID,
            "Gold": DamageType.FIRE,
            "Green": DamageType.POISON,
            "Red": DamageType.FIRE,
            "Silver": DamageType.COLD,
            "White": DamageType.COLD,
        }
        return mapping[self.value]

    @property
    def breath_weapon(self) -> BreathShape:
        mapping = {
            "Black": BreathShape.LINE,
            "Blue": BreathShape.LINE,
            "Brass": BreathShape.LINE,
            "Bronze": BreathShape.LINE,
            "Copper": BreathShape.LINE,
            "Gold": BreathShape.CONE,
            "Green": BreathShape.CONE,
            "Red": BreathShape.CONE,
            "Silver": BreathShape.CONE,
            "White": BreathShape.CONE,
        }
        return mapping[self.value]


# Dwarf
class DwarfToolProficiences(str, Enum):
    SMITHS_TOOLS = "Smith's Tools"
    BREWERS_SUPPLIES = "Brewer's Supplies"
    MASONS_TOOLS = "Mason's Tools"


class DwarfWeaponProficiencies(str, Enum):
    BATTLEAXE = "Battleaxe"
    HANDAXE = "Handaxe"
    LIGHT_HAMMER = "Light Hammer"
    WARHAMMER = "Warhammer"


# Tiefling
class SpellLimit(BaseModel):
    daily: Optional[dict[str, list[str]]]


class AdditionalSpells(BaseModel):
    innate: Optional[dict[str, SpellLimit]]
    known: Optional[dict[str, list[str]]]
    ability: str


class BaseRace(BaseModel):
    name: str
    size: Size = Size.MEDIUM
    speed: Annotated[int, Field(ge=10, le=40)] = 30
    age: AgeRange = Field(default_factory=lambda: AgeRange(mature=10, max=20))
    language_proficiencies: list[str] = Field(default_factory=lambda: ["Common"])
    ability: Ability = Field(default_factory=Ability)
