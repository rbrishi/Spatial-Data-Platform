from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import shape, mapping
from .. import models, schemas, database

router = APIRouter(prefix="/points", tags=["Points"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PointOut)
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    shapely_geom = shape(point.geom)
    db_point = models.PointData(
        name=point.name,
        description=point.description,
        geom=from_shape(shapely_geom, srid=4326)
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

@router.get("/{point_id}", response_model=schemas.PointOut)
def get_point(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(models.PointData).filter(models.PointData.id == point_id).first()
    if not db_point:
        raise HTTPException(status_code=404, detail="Point not found")
    geo = mapping(to_shape(db_point.geom))
    return schemas.PointOut(id=db_point.id, name=db_point.name, description=db_point.description, geom=geo)

@router.put("/{point_id}", response_model=schemas.PointOut)
def update_point(point_id: int, point: schemas.PointCreate, db: Session = Depends(get_db)):
    db_point = db.query(models.PointData).filter(models.PointData.id == point_id).first()
    if not db_point:
        raise HTTPException(status_code=404, detail="Point not found")
    db_point.name = point.name
    db_point.description = point.description
    db_point.geom = from_shape(shape(point.geom), srid=4326)
    db.commit()
    return db_point
