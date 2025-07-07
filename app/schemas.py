from pydantic import BaseModel
from typing import Optional

class PointBase(BaseModel):
    name: str
    description: Optional[str]
    geom: dict  # GeoJSON

class PointCreate(PointBase): pass

class PointOut(PointBase):
    id: int
    class Config:
        orm_mode = True

class PolygonBase(BaseModel):
    name: str
    description: Optional[str]
    geom: dict

class PolygonCreate(PolygonBase): pass

class PolygonOut(PolygonBase):
    id: int
    class Config:
        orm_mode = True
