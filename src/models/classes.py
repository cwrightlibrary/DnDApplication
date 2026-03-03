from typing import Any, Dict, List, Literal
from pydantic import Field
from src.enums.constants import BaseClass

BARBARIAN_FEATURES: Dict[int, List[str]] = {
    1: ["Rage", "Unarmored Defense"],
    2: ["Danger Sense", "Reckless Attack"],
    3: ["Primal Path", "Primal Knowledge"],
    4: ["Ability Score Improvement"],
    5: ["Extra Attack", "Fast Movement"],
    6: ["Path Feature"],
    7: ["Feral Instinct", "Instinctive Pounce"],
    8: ["Ability Score Improvement"],
    9: ["Brutal Critical (1 die)"],
    10: ["Path Feature"],
    11: ["Relentless Rage"],
    12: ["Ability Score Improvement"],
    13: ["Brutal Critical (2 dice)"],
    14: ["Path Feature"],
    15: ["Persistent Rage"],
    16: ["Ability Score Improvement"],
    17: ["Brutal Critical (3 dice)"],
    18: ["Indomitable Might"],
    19: ["Ability Score Improvement"],
    20: ["Primal Champion"],
}


class Barbarian(BaseClass):
    features: List[str] = Field(default_factory=list)
    rages: int = 2
    rage_damage: int = 2

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        rage_table: List[int] = [
            2,
            2,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            5,
            5,
            5,
            5,
            5,
            6,
            6,
            6,
            999,
        ]
        damage_table = [2] * 8 + [3] * 7 + [4] * 5

        self.rages = rage_table[self.level - 1]
        self.rage_damage = damage_table[self.level - 1]

        self.features = [
            feature
            for lvl, f_list in BARBARIAN_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


BARD_FEATURES: Dict[int, List[str]] = {
    1: ["Bardic Inspiration", "Spellcasting"],
    2: ["Jack of All Trades", "Song of Rest (d6)", "Magical Inspiration"],
    3: ["Bard College", "Expertise"],
    4: ["Ability Score Improvement", "Bardic Versatility"],
    5: ["Bardic Inspiration (d8)", "Font of Inspiration"],
    6: ["Countercharm", "Bard College feature"],
    7: [],
    8: ["Ability Score Improvement"],
    9: ["Song of Rest (d8)"],
    10: ["Bardic Inspiration (d10)", "Expertise", "Magical Secrets"],
    11: [],
    12: ["Ability Score Improvement"],
    13: ["Song of Rest (d10)"],
    14: ["Magical Secrets", "Bard College feature"],
    15: ["Bardic Inspiration (d12)"],
    16: ["Ability Score Improvement"],
    17: ["Song of Rest (d12)"],
    18: ["Magical Secrets"],
    19: ["Ability Score Improevment"],
    20: ["Superior Inspiration"],
}


class Bard(BaseClass):
    features: List[str] = Field(default_factory=list)
    cantrips_known: int = 2
    spells_known: int = 4
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        cantrips_known_table: List[int] = [
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
        ]
        spells_known_table: List[int] = [
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            12,
            13,
            14,
            15,
            15,
            16,
            18,
            19,
            19,
            20,
            22,
            22,
            22,
        ]
        spell_slots_per_spell_level_table: Dict[int, Dict[int, int]] = {
            1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
            10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
            11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
            12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
            13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
            14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
            15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
            16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
            17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
            18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
            19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
            20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
        }

        self.cantrips_known = cantrips_known_table[self.level - 1]
        self.spells_known = spells_known_table[self.level - 1]
        self.spell_slots_per_spell_level = spell_slots_per_spell_level_table[self.level]

        self.features = [
            feature
            for lvl, f_list in BARD_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


CLERIC_FEATURES: Dict[int, List[str]] = {
    1: ["Spellcasting", "Divine Domain"],
    2: [
        "Channel Divinity (1/rest)",
        "Channel Divinity: Harness Divine Power",
        "Divine Domain feature",
    ],
    3: [],
    4: ["Ability Score Improvement", "Cantrip Versatility"],
    5: ["Destroy Undead (CR 1/2)"],
    6: ["Channel Divinity (2/rest)", "Divine Domain feature"],
    7: [],
    8: ["Ability Score Improvement", "Destroy Undead (CR 1)", "Divine Domain feature"],
    9: [],
    10: ["Divine Intervention"],
    11: ["Destroy Undead (CR 2)"],
    12: ["Ability Score Improvement"],
    13: [],
    14: ["Destroy Undead (CR 3)"],
    15: [],
    16: ["Ability Score Improvement"],
    17: ["Destroy Undead (CR 4)", "Divine Domain feature"],
    18: ["Channel Divinity (3/rest)"],
    19: ["Ability Score Improvement"],
    20: ["Divine Intervention Improvement"],
}


class Cleric(BaseClass):
    features: List[str] = Field(default_factory=list)
    cantrips_known: int = 3
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        cantrips_known_table: List[int] = [
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
        ]
        spell_slots_per_spell_level_table: Dict[int, Dict[int, int]] = {
            1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
            10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
            11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
            12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
            13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
            14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
            15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
            16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
            17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
            18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
            19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
            20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
        }

        self.cantrips_known = cantrips_known_table[self.level - 1]
        self.spell_slots_per_spell_level = spell_slots_per_spell_level_table[self.level]

        self.features = [
            feature
            for lvl, f_list in CLERIC_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


DRUID_FEATURES: Dict[int, List[str]] = {
    1: ["Druidic", "Spellcasting"],
    2: ["Wild Shape", "Wild Companion", "Druid Circle"],
    3: [],
    4: ["Wild Shape Improvement", "Ability Score Improvement", "Cantrip Versatility"],
    5: [],
    6: ["Druid Circle feature"],
    7: [],
    8: ["Wild Shape Improvement", "Ability Score Improvement"],
    9: [],
    10: ["Druid Circle feature"],
    11: [],
    12: ["Ability Score Improvement"],
    13: [],
    14: ["Druid Circle feature"],
    15: [],
    16: ["Ability Score Improvement"],
    17: [],
    18: ["Timeless Body", "Beast Spells"],
    19: ["Ability Score Improvement"],
    20: ["Archdruid"],
}


class Druid(BaseClass):
    features: List[str] = Field(default_factory=list)
    cantrips_known: int = 2
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        cantrips_known_table: List[int] = [
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            4,
        ]
        spell_slots_per_spell_level_table: Dict[int, Dict[int, int]] = {
            1: {1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            2: {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            3: {1: 4, 2: 2, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            4: {1: 4, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            5: {1: 4, 2: 3, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            6: {1: 4, 2: 3, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            7: {1: 4, 2: 3, 3: 3, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            8: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            9: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
            10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 0, 7: 0, 8: 0, 9: 0},
            11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
            12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
            13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
            14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 0, 9: 0},
            15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
            16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 0},
            17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
            18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
            19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
            20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
        }

        self.cantrips_known = cantrips_known_table[self.level - 1]
        self.spell_slots_per_spell_level = spell_slots_per_spell_level_table[self.level]

        self.features = [
            feature
            for lvl, f_list in DRUID_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


FIGHTER_FEATURES: Dict[int, List[str]] = {
    1: ["Fighting Style", "Second Wind"],
    2: ["Action Surge"],
    3: ["Martial Archetype"],
    4: ["Ability Score Improvement", "Martial Versatility"],
    5: ["Extra Attack"],
    6: ["Ability Score Improvement"],
    7: ["Martial Archetype feature"],
    8: ["Ability Score Improvement"],
    9: ["Indomitable"],
    10: ["Martial Archetype feature"],
    11: ["Extra Attack (2)"],
    12: ["Ability Score Improvement"],
    13: ["Indomitable (two uses)"],
    14: ["Ability Score Improvement"],
    15: ["Martial Archetype feature"],
    16: ["Ability Score Improvement"],
    17: ["Action Surge (two uses)", "Indomitable (three uses)"],
    18: ["Martial Archetype feature"],
    19: ["Ability Score Improvement"],
    20: ["Extra Attack (3)"],
}


class Fighter(BaseClass):
    features: List[str] = Field(default_factory=list)

    def model_post_init(self, context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        self.features = [
            feature
            for lvl, f_list in FIGHTER_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


MONK_FEATURES: Dict[int, List[str]] = {
    1: ["Unarmored Defense", "Martial Arts"],
    2: ["Ki", "Dedicated Weapon", "Unarmored Movement"],
    3: ["Deflect Missiles", "Monastic Tradition", "Ki-Fueled Attack"],
    4: ["Ability Score Improvement", "Slow Fall", "Quickened Healing"],
    5: ["Extra Attack", "Stunning Strike", "Focused Aim"],
}