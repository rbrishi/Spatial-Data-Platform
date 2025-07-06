from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape
from shapely.geometry import shape
from . import models, schemas

# --- Point CRUD ---
def create_point(db: Session, point: schemas.PointCreate):
    geom = from_shape(shape(point.geom), srid=4326)
    db_point = models.PointData(
        name=point.name,
        description=point.description,
        geom=geom
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def get_point(db: Session, point_id: int):
    return db.query(models.PointData).filter(models.PointData.id == point_id).first()

def get_points(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PointData).offset(skip).limit(limit).all()

def update_point(db: Session, point_id: int, point: schemas.PointUpdate):
    db_point = db.query(models.PointData).filter(models.PointData.id == point_id).first()
    if db_point:
        db_point.name = point.name
        db_point.description = point.description
        db_point.geom = from_shape(shape(point.geom), srid=4326)
        db.commit()
        db.refresh(db_point)
    return db_point

def delete_point(db: Session, point_id: int):
    db_point = db.query(models.PointData).filter(models.PointData.id == point_id).first()
    if db_point:
        db.delete(db_point)
        db.commit()
    return db_point

# --- Polygon CRUD ---
def create_polygon(db: Session, polygon: schemas.PolygonCreate):
    geom = from_shape(shape(polygon.geom), srid=4326)
    db_polygon = models.PolygonData(
        name=polygon.name,
        description=polygon.description,
        geom=geom
    )
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return db_polygon

def get_polygon(db: Session, polygon_id: int):
    return db.query(models.PolygonData).filter(models.PolygonData.id == polygon_id).first()

def get_polygons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PolygonData).offset(skip).limit(limit).all()

def update_polygon(db: Session, polygon_id: int, polygon: schemas.PolygonUpdate):
    db_polygon = db.query(models.PolygonData).filter(models.PolygonData.id == polygon_id).first()
    if db_polygon:
        db_polygon.name = polygon.name
        db_polygon.description = polygon.description
        db_polygon.geom = from_shape(shape(polygon.geom), srid=4326)
        db.commit()
        db.refresh(db_polygon)
    return db_polygon

def delete_polygon(db: Session, polygon_id: int):
    db_polygon = db.query(models.PolygonData).filter(models.PolygonData.id == polygon_id).first()
    if db_polygon:
        db.delete(db_polygon)
        db.commit()
    return db_polygon
