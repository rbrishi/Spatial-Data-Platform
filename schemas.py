from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PointBase(BaseModel):
    name: str
    description: Optional[str] = None
    geom: Dict[str, Any] = Field(..., description="GeoJSON Point geometry")


class PointCreate(PointBase):
    pass


class PointUpdate(PointBase):
    pass


class Point(PointBase):
    id: int

    class Config:
        orm_mode = True


class PolygonBase(BaseModel):
    name: str
    description: Optional[str] = None
    geom: Dict[str, Any] = Field(..., description="GeoJSON Polygon geometry")


class PolygonCreate(PolygonBase):
    pass


class PolygonUpdate(PolygonBase):
    pass


class Polygon(PolygonBase):
    id: int

    class Config:
        orm_mode = True
