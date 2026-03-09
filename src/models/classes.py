from pydantic import BaseModel, Field
from typing import Literal

from src.enums.class_constants import BaseClass, HitDice, SkillChoice, SkillChoiceDetails, StartingEquipment, StartingProficiencies


# Barbarian
class Barbarian(BaseClass):
    name: Literal["Barbarian"] = "Barbarian"
    hit_dice: HitDice = Field(default_factory=lambda: HitDice(number=1, faces=12))

    proficiency: list[str] = Field(default_factory=lambda: ["strength", "constitution"])
    starting_proficiencies: StartingProficiencies = Field(
        default_factory=lambda: StartingProficiencies(
            armor=["Light", "Medium", "Shield"],
            weapons=["Simple", "Martial"],
            skills=[
                SkillChoice(choose=SkillChoiceDetails(
                    from_list=[
                        "Animal Handling",
                        "Athletics",
                        "Intimidation",
                        "Nature",
                        "Perception",
                        "Survival",
                    ],
                    count=2,
                )),
            ]
        )
    )
    starting_equipment: StartingEquipment = Field(
        default_factory=lambda: StartingEquipment(
            additional_from_background=True,
            default=[
                "Greataxe",
                "Handaxe",
                "Handaxe",
            ],
            gold_alternative="2d4 10 Starting Gold",
        )
    )