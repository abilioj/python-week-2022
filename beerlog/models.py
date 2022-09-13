# from dataclasses import dataclass
from datetime import datetime
from statistics import mean  # pra estatitica
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel

# @dataclass
# class Beer:


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    # valida campo de 1 a 10
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    # valida a pontuação da bebida,
    @validator("rate", always=True)
    def calculete_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


# objeto
# brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=5, cost=8)
