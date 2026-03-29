from src.models.character import Character
from src.models.races import Halfling
from src.models.classes import Barbarian


test_char = Character(
    name="Test",
    player_name="Test",
    character_race=Halfling(),
    character_class=Barbarian(),
)

for ability in test_char.character_race.ability:
    print(ability)