from pydantic import BaseModel, conlist
from typing import List


class Housing(BaseModel):
    # data: List
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    ocean_proximity: str

