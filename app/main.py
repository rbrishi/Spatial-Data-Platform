from fastapi import FastAPI
from .routers import points, polygons
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Spatial Data Platform")

app.include_router(points.router)
app.include_router(polygons.router)