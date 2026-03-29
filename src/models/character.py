from fillpdf import fillpdfs
from pydantic import BaseModel, Field, computed_field
from src.enums.race_constants import BaseRace
from src.enums.class_constants import (
    LightArmor,
    MediumArmor,
    HeavyArmor,
    Shield,
    BaseClass,
    Skill,
    SkillAbilityMapping,
)
import src.models.races as races
import src.models.classes as classes

PdfCharacterData = dict[str, str]


class Character(BaseModel):
    name: str
    player_name: str
    level: int = Field(default=1, ge=1, le=20)
    character_race: BaseRace
    character_class: BaseClass

    @computed_field
    @property
    def max_hp(self) -> int:
        con_mod = (self.character_race.ability.constitution - 10) // 2
        return self.character_class.hit_die + con_mod

    @computed_field
    @property
    def armor_class(self) -> int:
        _armor_class = 10 + self.character_race.ability.dexterity_mod

        if self.character_class.armor_proficiencies:
            for armor in self.character_class.armor_proficiencies:
                if isinstance(armor, HeavyArmor):
                    _armor_class = getattr(armor, "active_armor")
                elif isinstance(armor, Shield):
                    _armor_class += armor.shield
                elif isinstance(armor, MediumArmor) or isinstance(armor, LightArmor):
                    _armor_class = (
                        getattr(armor, armor.active_armor)
                        + self.character_race.ability.dexterity_mod
                    )
        return _armor_class

    @computed_field
    @property
    def initiative(self) -> int:
        return self.character_race.ability.dexterity_mod

    @computed_field
    @property
    def proficiency_bonus(self) -> int:
        if self.level <= 4:
            return 2
        elif 5 < self.level <= 8:
            return 3
        elif 9 < self.level <= 12:
            return 4
        elif 13 < self.level <= 16:
            return 5
        else:
            return 6

    @computed_field
    @property
    def saving_throws(self) -> dict[str, int]:
        throws: dict[str, int] = {}
        for throw in self.character_class.saving_throws:
            mod = self.character_race.ability.get_modifier(
                getattr(self.character_race.ability, throw)
            )
            throws[throw] = mod + self.proficiency_bonus
        return throws

    @computed_field
    @property
    def skills(self) -> dict[Skill, int]:
        skills: dict[Skill, int] = {}
        if (
            isinstance(self.character_class, classes.Barbarian)
            or isinstance(self.character_class, classes.Bard)
            or isinstance(self.character_class, classes.Cleric)
        ):
            for skill in self.character_class.chosen_skills:
                print(skill)
                mod = self.character_race.ability.get_modifier(
                    getattr(self.character_race.ability, SkillAbilityMapping[skill])
                )
                print(mod)
                skills[skill] = mod + self.proficiency_bonus
        return skills

    def get_character_data_dict(self) -> PdfCharacterData:
        data_dict: dict[str, str] = {}

        _class = self.character_class
        _race = self.character_race
        _ability = _race.ability

        data_dict["ClassLevel"] = f"{_class.name} Level {self.level}"
        data_dict["Spellcasting Class 2"] = f"{_class.name}"
        data_dict["PlayerName"] = f"{self.player_name}"
        data_dict["CharacterName"] = f"{self.name}"
        data_dict["Race "] = f"{_race.name}"
        data_dict["ProfBonus"] = f"{self.proficiency_bonus}"
        data_dict["AC"] = f"{self.armor_class}"
        data_dict["Initiative"] = f"{self.initiative}"
        data_dict["Speed"] = f"{_race.speed}"
        data_dict["STR"] = (
            f"{_ability.strength_mod}"
            if _ability.strength_mod <= 0
            else f"+{_ability.strength_mod}"
        )
        data_dict["STRmod"] = f"{_ability.strength}"
        data_dict["DEX"] = (
            f"{_ability.dexterity_mod}"
            if _ability.dexterity_mod <= 0
            else f"+{_ability.dexterity_mod}"
        )
        data_dict["DEXmod "] = f"{_ability.dexterity}"
        data_dict["CON"] = (
            f"{_ability.constitution_mod}"
            if _ability.constitution_mod <= 0
            else f"+{_ability.constitution_mod}"
        )
        data_dict["CONmod"] = f"{_ability.constitution}"
        data_dict["INT"] = (
            f"{_ability.intelligence_mod}"
            if _ability.intelligence_mod <= 0
            else f"+{_ability.intelligence_mod}"
        )
        data_dict["INTmod"] = f"{_ability.intelligence}"
        data_dict["WIS"] = (
            f"{_ability.wisdom_mod}"
            if _ability.wisdom_mod <= 0
            else f"+{_ability.wisdom_mod}"
        )
        data_dict["WISmod"] = f"{_ability.wisdom}"
        data_dict["CHA"] = (
            f"{_ability.charisma_mod}"
            if _ability.charisma_mod <= 0
            else f"+{_ability.charisma_mod}"
        )
        data_dict["CHamod"] = f"{_ability.charisma}"

        # Saving throws
        mapping: dict[str, str] = {
            "strength": "Check Box 11",
            "dexterity": "Check Box 18",
            "constitution": "Check Box 19",
            "intelligence": "Check Box 20",
            "wisdom": "Check Box 21",
            "charisma": "Check Box 22",
        }

        for k, v in self.saving_throws.items():
            title: str = f"ST {k.title()}"
            data_dict[title] = str(v)

            check_box: str = mapping[k]
            data_dict[check_box] = "Yes"

        # Skills
        skill_mapping: dict[Skill, list[str]] = {
            Skill.ACR: ["Acrobatics", "Check Box 23", "dexterity"],
            Skill.ANI: ["Animal", "Check Box 24", "wisdom"],
            Skill.ARC: ["Arcana", "Check Box 25", "intelligence"],
            Skill.ATH: ["Athletics", "Check Box 26", "strength"],
            Skill.DEC: ["Deception ", "Check Box 27", "charisma"],
            Skill.HIS: ["History ", "Check Box 28", "intelligence"],
            Skill.INS: ["Insight", "Check Box 29", "wisdom"],
            Skill.INT: ["Intimidation", "Check Box 30", "charisma"],
            Skill.INV: ["Investigation ", "Check Box 31", "intelligence"],
            Skill.MED: ["Medicine", "Check Box 32", "wisdom"],
            Skill.NAT: ["Nature", "Check Box 33", "intelligence"],
            Skill.PEC: ["Perception ", "Check Box 34", "wisdom"],
            Skill.PER: ["Performance", "Check Box 35", "charisma"],
            Skill.PES: ["Persuasion", "Check Box 36", "charisma"],
            Skill.REL: ["Religion", "Check Box 37", "intelligence"],
            Skill.SLE: ["SleightofHand", "Check Box 38", "dexterity"],
            Skill.STE: ["Stealth ", "Check Box 39", "dexterity"],
            Skill.SUR: ["Survival", "Check Box 40", "wisdom"],
        }

        ability_mapping: dict[str, int] = {
            "strength": self.character_race.ability.strength_mod,
            "dexterity": self.character_race.ability.dexterity_mod,
            "constitution": self.character_race.ability.constitution_mod,
            "intelligence": self.character_race.ability.intelligence_mod,
            "wisdom": self.character_race.ability.wisdom_mod,
            "charisma": self.character_race.ability.charisma_mod,
        }

        assigned_skills: list[Skill] = []

        for skill, skill_val in self.skills.items():
            data_dict[skill_mapping[skill][0]] = f"{skill_val}"
            data_dict[skill_mapping[skill][1]] = "Yes"
            assigned_skills.append(skill)
        
        for ability in self.character_race.ability:
            for skill, ability_type in skill_mapping.items():
                if ability[0] == ability_type[2] and skill not in assigned_skills:
                    data_dict[ability_type[0]] = str(ability_mapping[ability[0]])

        return data_dict

    def save_pdf_character_sheet(self, filepath: str) -> None:
        fillpdfs.write_fillable_pdf(
            input_pdf_path="assets/character_sheet.pdf",
            output_pdf_path=filepath,
            data_dict=self.get_character_data_dict(),
        )
