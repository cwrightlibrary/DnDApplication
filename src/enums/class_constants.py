from typing import Any, Optional
from pydantic import BaseModel, Field


class HitDice(BaseModel):
    number: int
    faces: int


class SkillChoiceDetails(BaseModel):
    from_list: list[str] = Field(default_factory=list)
    count: int


class SkillChoice(BaseModel):
    choose: SkillChoiceDetails


class StartingEquipment(BaseModel):
    additional_from_background: Optional[bool] = False
    default: list[str] = Field(default_factory=list)
    gold_alternative: Optional[str] = None


class StartingProficiencies(BaseModel):
    armor: list[str] = Field(default_factory=list)
    weapons: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    skills: list[SkillChoice] = Field(default_factory=list)


class BaseClass(BaseModel):
    name: str
    hit_dice: HitDice
    proficiency: list[str] = Field(default_factory=list)

    starting_proficiencies: StartingProficiencies
    starting_equipment: StartingEquipment
