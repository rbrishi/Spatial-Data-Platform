from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from shapely.geometry import mapping
from geoalchemy2.shape import to_shape
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Point Endpoints ---
@app.post("/points/", response_model=schemas.Point)
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    db_point = crud.create_point(db, point)
    result = schemas.Point.from_orm(db_point)
    result.geom = mapping(to_shape(db_point.geom))
    return result

@app.get("/points/", response_model=List[schemas.Point])
def read_points(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    points = crud.get_points(db, skip=skip, limit=limit)
    results = []
    for db_point in points:
        item = schemas.Point.from_orm(db_point)
        item.geom = mapping(to_shape(db_point.geom))
        results.append(item)
    return results

@app.get("/points/{point_id}", response_model=schemas.Point)
def read_point(point_id: int, db: Session = Depends(get_db)):
    db_point = crud.get_point(db, point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    result = schemas.Point.from_orm(db_point)
    result.geom = mapping(to_shape(db_point.geom))
    return result

@app.put("/points/{point_id}", response_model=schemas.Point)
def update_point(point_id: int, point: schemas.PointUpdate, db: Session = Depends(get_db)):
    db_point = crud.update_point(db, point_id, point)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    result = schemas.Point.from_orm(db_point)
    result.geom = mapping(to_shape(db_point.geom))
    return result

@app.delete("/points/{point_id}", response_model=schemas.Point)
def delete_point(point_id: int, db: Session = Depends(get_db)):
    db_point = crud.delete_point(db, point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    result = schemas.Point.from_orm(db_point)
    result.geom = mapping(to_shape(db_point.geom))
    return result

# --- Polygon Endpoints ---
@app.post("/polygons/", response_model=schemas.Polygon)
def create_polygon(polygon: schemas.PolygonCreate, db: Session = Depends(get_db)):
    db_polygon = crud.create_polygon(db, polygon)
    result = schemas.Polygon.from_orm(db_polygon)
    result.geom = mapping(to_shape(db_polygon.geom))
    return result

@app.get("/polygons/", response_model=List[schemas.Polygon])
def read_polygons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    polygons = crud.get_polygons(db, skip=skip, limit=limit)
    results = []
    for db_polygon in polygons:
        item = schemas.Polygon.from_orm(db_polygon)
        item.geom = mapping(to_shape(db_polygon.geom))
        results.append(item)
    return results

@app.get("/polygons/{polygon_id}", response_model=schemas.Polygon)
def read_polygon(polygon_id: int, db: Session = Depends(get_db)):
    db_polygon = crud.get_polygon(db, polygon_id)
    if db_polygon is None:
        raise HTTPException(status_code=404, detail="Polygon not found")
    result = schemas.Polygon.from_orm(db_polygon)
    result.geom = mapping(to_shape(db_polygon.geom))
    return result

@app.put("/polygons/{polygon_id}", response_model=schemas.Polygon)
def update_polygon(polygon_id: int, polygon: schemas.PolygonUpdate, db: Session = Depends(get_db)):
    db_polygon = crud.update_polygon(db, polygon_id, polygon)
    if db_polygon is None:
        raise HTTPException(status_code=404, detail="Polygon not found")
    result = schemas.Polygon.from_orm(db_polygon)
    result.geom = mapping(to_shape(db_polygon.geom))
    return result

@app.delete("/polygons/{polygon_id}", response_model=schemas.Polygon)
def delete_polygon(polygon_id: int, db: Session = Depends(get_db)):
    db_polygon = crud.delete_polygon(db, polygon_id)
    if db_polygon is None:
        raise HTTPException(status_code=404, detail="Polygon not found")
    result = schemas.Polygon.from_orm(db_polygon)
    result.geom = mapping(to_shape(db_polygon.geom))
    return result
