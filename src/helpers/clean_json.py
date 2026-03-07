import json
from pathlib import Path


def clean_races() -> None:
    with open("assets/races.json", "r", encoding="utf-8") as f:
        data = json.load(f)
       
    if not data:
        return
    
    data["race"] = [x for x in data["race"] if x["source"].startswith("PHB")]
    
    with open("assets/usable/races.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data["race"], indent=4))


def clean_classes() -> None:
    dir = Path("assets/class")

    for fp in dir.iterdir():
        if fp.is_file():
            with open(fp, "r") as f:
                data = json.load(f)
            
            if not data:
                break

            data["class"] = [x for x in data["class"] if x["source"].startswith("PHB")]

            with open(f"assets/usable/class/{fp.stem.split("-")[-1]}.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(data["class"], indent=4))


if __name__ == "__main__":
    # clean_races()
    clean_classes()