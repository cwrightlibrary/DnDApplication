from pydantic import BaseModel, Field, computed_field
from src.enums.race_constants import BaseRace
from src.enums.class_constants import LightArmor, MediumArmor, HeavyArmor, Shield, BaseClass


class Character(BaseModel):
    name: str
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
        _armor_class = 10 + self.character_race.ability.dexterity

        if self.character_class.armor_proficiencies:
            for armor in self.character_class.armor_proficiencies:
                if isinstance(armor, HeavyArmor):
                    _armor_class = getattr(armor, "active_armor")
                elif isinstance(armor, Shield):
                    _armor_class += armor.shield
                elif isinstance(armor, MediumArmor):
                    dex = self.character_race.ability.get_modifier(self.character_race.ability.dexterity) if self.character_race.ability.get_modifier(self.character_race.ability.dexterity) <= 2 else 2
                    _armor_class = getattr(armor, armor.active_armor) + dex
                elif isinstance(armor, LightArmor):
                    dex = self.character_race.ability.get_modifier(self.character_race.ability.dexterity)
                    _armor_class = getattr(armor, armor.active_armor) + dex
        return _armor_class
    
    @computed_field
    @property
    def initiative(self) -> int:
        return self.character_race.ability.get_modifier(self.character_race.ability.dexterity)
    
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
            mod = self.character_race.ability.get_modifier(getattr(self.character_race.ability, throw))
            throws[throw] = mod + self.proficiency_bonus
        return throws
