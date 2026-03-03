import json
from gc import collect
from pathlib import Path


def read_json(filepath: Path):
    try:
        if filepath.exists():
            with filepath.open(mode="r", encoding="utf-8") as f:
                data = json.load(f)
                f.close()

            if data:
                return data
    except Exception as e:
        print(e)


if __name__ == "__main__":
    data = read_json(Path("assets/races.json"))
    collected_data = {}

    for item in data["race"]:
        if item["source"] == "PHB":
            if item["name"] not in collected_data:
                collected_data[item["name"]] = {
                    "size": item["size"],
                    "speed": item["speed"],
                }

                if "ability" in item:
                    if "ability" not in collected_data[item["name"]]:
                        collected_data[item["name"]]["ability"] = {}

                    if "choose" in item["ability"][0]:
                        for k, v in item["ability"][0].items():
                            if k == "choose":
                                if (
                                    "choose_from"
                                    not in collected_data[item["name"]]["ability"]
                                ):
                                    collected_data[item["name"]]["ability"][
                                        "choose_from"
                                    ] = {"count": item["ability"][0]["choose"]["count"]}
                                collected_data[item["name"]]["ability"]["choose_from"][
                                    k
                                ] = v

                    else:
                        for k, v in item["ability"][0].items():
                            collected_data[item["name"]]["ability"][k] = v

                if "heightAndWeight" in item:
                    for k, v in item["heightAndWeight"].items():
                        if "height_weight" not in collected_data[item["name"]]:
                            collected_data[item["name"]]["height_weight"] = {}
                        collected_data[item["name"]]["height_weight"][k] = v

                if "age" in item:
                    for k, v in item["age"].items():
                        if "age" not in collected_data[item["name"]]:
                            collected_data[item["name"]]["age"] = {}
                        collected_data[item["name"]]["age"][k] = v

                if "languageProficiencies" in item:
                    for k, v in item["languageProficiencies"].items():
                        if "language_proficiencies" not in collected_data[item["name"]]:
                            collected_data[item["name"]]["language_proficiencies"] = {}
                        collected_data[item["name"]]["language_proficiencies"][k] = v

    for k, v in collected_data.items():
        print(k, v)
