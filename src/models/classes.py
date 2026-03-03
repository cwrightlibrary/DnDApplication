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

        rage_table: List[int] = [2] * 2 + [3] * 3 + [4] * 6 + [5] * 5 + [6] * 3 + [999]
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

        cantrips_known_table: List[int] = [2] * 2 + [3] * 6 + [4] * 11
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

        cantrips_known_table: List[int] = [3] * 3 + [4] * 6 + [5] * 11
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

        cantrips_known_table: List[int] = [2] * 3 + [3] * 6 + [4] * 11
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
    6: ["Ki-Empowered Strikes", "Monastic Tradition feature"],
    7: ["Evasion", "Stillness of Mind"],
    8: ["Ability Score Improvement"],
    9: ["Unarmored Movement Improvement"],
    10: ["Purity of Body"],
    11: ["Monastic Tradition feature"],
    12: ["Ability Score Improvement"],
    13: ["Tongue of the Sun and Moon"],
    14: ["Diamond Soul"],
    15: ["Timeless Body"],
    16: ["Ability Score Improvement"],
    17: ["Monastic Tradition feature"],
    18: ["Empty Body"],
    19: ["Ability Score Improvement"],
    20: ["Perfect Self"],
}


class Monk(BaseClass):
    features: List[str] = Field(default_factory=list)
    martial_arts: str = "1d4"
    ki_points: int = Field(ge=0, le=20, default=0)
    unarmored_movement: int = Field(ge=0, le=30, default=0)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        martial_arts_table: List[str] = ["1d4"] * 4 + ["1d6"] * 6 + ["1d8"] * 6 + ["1d10"] * 4
        unarmored_movement_table: List[int] = [0] + [10] * 4 + [15] * 4 + [20] * 4 + [25] * 4 + [30] * 3
        self.martial_arts = martial_arts_table[self.level - 1]
        self.ki_points = self.level if self.level > 1 else 0
        self.unarmored_movement = unarmored_movement_table[self.level - 1]

        self.features = [
            feature
            for lvl, f_list in
            MONK_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


PALADIN_FEATURES: Dict[int, List[str]] = {
    1: ["Divine Sense", "Lay on Hands"],
    2: ["Divine Smite", "Fighting Style", "Spellcasting"],
    3: ["Divine Health", "Sacred Oath"],
    4: ["Ability Score Improvement", "Martial Versatility"],
    5: ["Extra Attack"],
    6: ["Aura of Protection"],
    7: ["Sacred Oath feature"],
    8: ["Ability Score Improvement"],
    9: [],
    10: ["Aura of Courage"],
    11: ["Improved Divine Smite"],
    12: ["Ability Score Improvement"],
    13: [],
    14: ["Cleansing Touch"],
    15: ["Sacred Oath feature"],
    16: ["Ability Score Improvement"],
    17: [],
    18: ["Aura Improvements"],
    19: ["Ability Score Improvement"],
    20: ["Sacred Oath feature"],
}


class Paladin(BaseClass):
    features: List[str] = Field(default_factory=list)
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

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

        self.spell_slots_per_spell_level = spell_slots_per_spell_level_table[self.level]

        self.features = [
            feature
            for lvl, f_list in
            PALADIN_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


RANGER_FEATURES: Dict[int, List[str]] = {
    1: ["Favored Enemy", "Favored Foe", "Natural Explorer", "Deft Explorer"],
    2: ["Fighting Style", "Spellcasting", "Spellcasting Focus"],
    3: ["Ranger Archetype", "Primeval Awareness", "Primal Awareness"],
    4: ["Ability Score Improvement", "Martial Versatility"],
    5: ["Extra Attack"],
    6: ["Favored Enemy and Natural Explorer improvements", "Deft Explorer Improvement"],
    7: ["Ranger Archetype feature"],
    8: ["Ability Score Improvement", "Land's Stride"],
    9: [],
    10: ["Hide in Plain Sight", "Nature's Veil", "Natural Explorder Improvement", "Deft Explorer Improvement"],
    11: ["Ranger Archetype feature"],
    12: ["Ability Score Improvement"],
    13: [],
    14: ["Vanish", "Favored Enemy Improvement"],
    15: ["Ranger Archetype feature"],
    16: ["Ability Score Improvement"],
    17: [],
    18: ["Feral Senses"],
    19: ["Ability Score Improvement"],
    20: ["Foe Slayer"],
}


class Ranger(BaseClass):
    features: List[str] = Field(default_factory=list)
    spells_known: int = 0
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        spells_known_table: List[int] = [0] + [2] + [3] * 2 + [4] * 2 + [5] * 2 + [6] * 2 + [7] * 2 + [8] * 2 + [9] * 2 + [10] * 2 + [11] * 2

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

        self.spells_known = spells_known_table[self.level - 1]
        self.spell_slots_per_spell_level = spell_slots_per_spell_level_table[self.level]

        self.features = [
            feature
            for lvl, f_list in
            RANGER_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


ROGUE_FEATURES: Dict[int, List[str]] = {
    1: ["Expertise", "Sneak Attack", "Thieves' Cant"],
    2: ["Cunning Action"],
    3: ["Roguish Archetype", "Steady Aim"],
    4: ["Ability Score Improvement"],
    5: ["Uncanny Dodge"],
    6: ["Expertise"],
    7: ["Evasion"],
    8: ["Ability Score Improvement"],
    9: ["Roguish Archetype feature"],
    10: ["Ability Score Improvement"],
    11: ["Reliable Talent"],
    12: ["Ability Score Improvement"],
    13: ["Roguish Archetype feature"],
    14: ["Blindsense"],
    15: ["Slippery Mind"],
    16: ["Ability Score Improvement"],
    17: ["Roguish Archetype feature"],
    18: ["Elusive"],
    19: ["Ability Score Improvement"],
    20: ["Stroke of Luck"],
}


class Rogue(BaseClass):
    features: List[str] = Field(default_factory=list)
    sneak_attack: str = "1d6"

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        sneak_attack_table: List[str] = ["1d6"] * 2 + ["2d6"] * 2 + ["3d6"] * 2 + ["4d6"] * 2 + ["5d6"] * 2 + ["6d6"] * 2 + ["7d6"] * 2 + ["8d6"] * 2 + ["9d6"] * 2 + ["10d6"] * 2

        self.sneak_attack = sneak_attack_table[self.level - 1]

        self.features = [
            feature
            for lvl, f_list in
            ROGUE_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


SORCERER_FEATURES: Dict[int, List[str]] = {
    1: ["Spellcasting", "Sorcerous Origin"],
    2: ["Font of Magic"],
    3: ["Metamagic", "Metamagic Options"],
    4: ["Ability Score Improvement", "Sorcerous Versatility"],
    5: ["Magical Guidance"],
    6: ["Sorcerous Origin feature"],
    7: [],
    8: ["Ability Score Improvement"],
    9: [],
    10: ["Metamagic"],
    11: [],
    12: ["Ability Score Improvement"],
    13: [],
    14: ["Sorcerous Origin feature"],
    15: [],
    16: ["Ability Score Improvement"],
    17: ["Metamagic"],
    18: ["Sorcerous Origin feature"],
    19: ["Ability Score Improvement"],
    20: ["Sorcerous Restoration"],
}


class Sorcerer(BaseClass):
    features: List[str] = Field(default_factory=list)
    sorcery_points: int = 0
    cantrips_known: int = 4
    spells_known: int = 2
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        cantrips_known_table: List[int] = [4] * 3 + [5] * 6 + [6] * 11
        spells_known_table: List[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] + [12] * 2 + [13] * 2 + [14] * 2 + [15] * 4
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

        self.sorcery_points = self.level if self.level > 1 else 0
        self.cantrips_known = cantrips_known_table[self.level - 1]
        self.spells_known = spells_known_table[self.level - 1]
        self.spell_slots_per_spell_level = spell_slots_per_spell_level_table[self.level]

        self.features = [
            feature
            for lvl, f_list in
            SORCERER_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]


WARLOCK_FEATURES: Dict[int, List[str]] = {
    1: ["Pact Magic", "Otherworldly Patron"],
    2: ["Eldritch Invocations"],
    3: ["Pact Boon"],
    4: ["Ability Score Improvement", "Edritch Versatility"],
    5: [],
    6: ["Otherworldly Patron feature"],
    7: [],
    8: ["Ability Score Improvement"],
    9: [],
    10: ["Otherworldly Patron feature"],
    11: ["Mystic Arcanum (6th level)"],
    12: ["Ability Score Improvement"],
    13: ["Mystic Arcanum (7th level)"],
    14: ["Otherworldly Patron feature"],
    15: ["Mystic Arcanum (8th level)"],
    16: ["Ability Score Improvement"],
    17: ["Mystic Arcanum (9th level)"],
    18: [],
    19: ["Ability Score Improvement"],
    20: ["Eldritch Master"],
}


class Warlock(BaseClass):
    features: List[str] = Field(default_factory=list)
    cantrips_known: int = 2
    spells_known: int = 2
    spell_slots: int = 1
    slot_level: int = 1
    invocations_known: int = 0

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        cantrips_known_table: List[int] = [2] * 3 + [3] * 6 + [4] * 11
        spells_known_table: List[int] = [2, 3, 4, 5, 6, 7, 8, 9] + [10] * 2 + [11] * 2 + [12] * 12 + [13] * 2 + [14] * 2 + [15] * 2
        spell_slots_table: List[int] = [1] + [2] * 9 + [3] * 6 + [4] * 4
        slot_level_table: List[int] = [1] * 2 + [2] * 2 + [3] * 2 + [4] * 2 + [5] * 12
        invocations_known_table: List[int] = [0] + [2] * 3 + [3] * 2 + [4] * 2 + [5] * 3 + [6] * 3 + [7] * 3 + [8] * 3

        self.cantrips_known = cantrips_known_table[self.level - 1]
        self.spells_known = spells_known_table[self.level - 1]
        self.spells_known = spell_slots_table[self.level - 1]
        self.slot_level = slot_level_table[self.level - 1]
        self.invocations_known = invocations_known_table[self.level - 1]


WIZARD_FEATURES: Dict[int, List[str]] = {
    1: ["Arcane Recovery", "Spellcasting"],
    2: ["Arcane Tradition"],
    3: ["Cantrip Formulas"],
    4: ["Ability Score Improvement"],
    5: [],
    6: ["Arcane Tradition feature"],
    7: [],
    8: ["Ability Score Improvement"],
    9: [],
    10: ["Arcane Tradition feature"],
    11: [],
    12: ["Ability Score Improvement"],
    13: [],
    14: ["Arcane Tradition feature"],
    15: [],
    16: ["Ability Score feature"],
    17: [],
    18: ["Spell Mastery"],
    19: ["Ability Score Improvement"],
    20: ["Signature Spells"],
}


class Wizard(BaseClass):
    features: List[str] = Field(default_factory=list)
    cantrips_known: int = 3
    spell_slots_per_spell_level: Dict[int, int] = Field(default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self._calculate_modifiers()

    def _calculate_modifiers(self) -> None:
        self.proficiency_bonus = (self.level - 1) // 4 + 2

        cantrips_known_table: List[int] = [3] * 3 + [4] * 6 + [5] * 11
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
            for lvl, f_list in
            WIZARD_FEATURES.items()
            if lvl <= self.level
            for feature in f_list
        ]
