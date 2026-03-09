from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel
from typing import Any, Union


class DnDBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="allow",
    )


class SpeedData(DnDBase):
    walk: int | None = None
    fly: int | bool | None = None
    swim: int | None = None
    climb: int | None = None


class Entry(DnDBase):
    name: str | None = None
    type: str | None = None
    entries: list[Union[str, "Entry"]] | None = None
    items: list[Any] | None = None


class Race(DnDBase):
    name: str
    size: list[str]
    speed: int | SpeedData

    ability: list[dict[str, Any]] = Field(default_factory=list)
    trait_tags: list[str] = Field(default_factory=list)
    language_proficiencies: list[dict[str, Any]] = Field(default_factory=list)
    entries: list[Union[str, Entry]] = Field(default_factory=list)


class Compendium(DnDBase):
    meta: dict[str, Any] = Field(alias="_meta")
    race: list[Race]


Entry.model_rebuild()
