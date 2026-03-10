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

    dump = chris.model_dump()

    for k, v in dump.items():
        if isinstance(v, dict):
            print(k)
            for sk, sv in v.items():
                if isinstance(sv, dict):
                    print(f"  {sk}")
                    for ssk, ssv in sv.items():
                        print(f"    {ssk} {ssv}")
                else:
                    print(f"  {sk} {sv}")
        else:
            print(k, v)


if __name__ == "__main__":
    main()