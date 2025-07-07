from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from .database import Base

class PointData(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    geom = Column(Geometry("POINT"))

class PolygonData(Base):
    __tablename__ = "polygons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    geom = Column(Geometry("POLYGON"))