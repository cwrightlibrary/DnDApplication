import json
from src.models.reworking_races import Compendium

def main() -> None:
    with open("assets/usable/races.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        compendium = Compendium.model_validate(data)

        for r in compendium.race:
            print(f"{r.name} - Speed: {r.speed}")


if __name__ == "__main__":
    main()