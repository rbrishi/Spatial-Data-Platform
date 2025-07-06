from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from .database import Base


class PointData(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    geom = Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)


class PolygonData(Base):
    __tablename__ = "polygons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    geom = Column(Geometry(geometry_type="POLYGON", srid=4326), nullable=False)
