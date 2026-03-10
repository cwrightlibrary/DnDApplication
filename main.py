import src.models.races as races
import src.models.classes as classes
from src.enums.class_constants import Skill
from src.models.character import Character


def main():
    chris = Character(
        name="Frogdo",
        player_name="Chris",
        level=1,
        character_race=races.Halfling(),
        character_class=classes.Barbarian(chosen_skills=[Skill.ANI, Skill.ATH])
    )

    chris.save_pdf_character_sheet("out/test_fill.pdf")


if __name__ == "__main__":
    main()