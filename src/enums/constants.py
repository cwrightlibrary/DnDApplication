from typing import List, Literal
from pydantic import BaseModel, Field

from src.helpers.roll_dice import roll_dice


class Abilities(BaseModel):
    strength: int = Field(ge=0, le=30, default=roll_dice())
    dexterity: int = Field(ge=0, le=30, default=roll_dice())
    constitution: int = Field(ge=0, le=30, default=roll_dice())
    intelligence: int = Field(ge=0, le=30, default=roll_dice())
    wisdom: int = Field(ge=0, le=30, default=roll_dice())
    charisma: int = Field(ge=0, le=30, default=roll_dice())
    
    available_points: int = Field(ge=0, le=30, default=roll_dice())

    def get_modifier(self, stat: int) -> int:
        return (stat - 10) // 2


class BaseRace(BaseModel):
    size: Literal["Small", "Medium"] = "Small"
    speed: int = Field(ge=1, le=100, default=30)
    languages: List[str] = ["Common"]
    abilities: Abilities = Field(default_factory=Abilities)