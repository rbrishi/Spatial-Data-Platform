from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import shape, mapping
from .. import models, schemas, database

router = APIRouter(prefix="/polygons", tags=["Polygons"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PolygonOut)
def create_polygon(poly: schemas.PolygonCreate, db: Session = Depends(get_db)):
    shapely_geom = shape(poly.geom)
    db_poly = models.PolygonData(
        name=poly.name,
        description=poly.description,
        geom=from_shape(shapely_geom, srid=4326)
    )
    db.add(db_poly)
    db.commit()
    db.refresh(db_poly)
    return db_poly

@router.get("/{poly_id}", response_model=schemas.PolygonOut)
def get_polygon(poly_id: int, db: Session = Depends(get_db)):
    db_poly = db.query(models.PolygonData).filter(models.PolygonData.id == poly_id).first()
    if not db_poly:
        raise HTTPException(status_code=404, detail="Polygon not found")
    geo = mapping(to_shape(db_poly.geom))
    return schemas.PolygonOut(id=db_poly.id, name=db_poly.name, description=db_poly.description, geom=geo)

@router.put("/{poly_id}", response_model=schemas.PolygonOut)
def update_polygon(poly_id: int, poly: schemas.PolygonCreate, db: Session = Depends(get_db)):
    db_poly = db.query(models.PolygonData).filter(models.PolygonData.id == poly_id).first()
    if not db_poly:
        raise HTTPException(status_code=404, detail="Polygon not found")
    db_poly.name = poly.name
    db_poly.description = poly.description
    db_poly.geom = from_shape(shape(poly.geom), srid=4326)
    db.commit()
    return db_poly
