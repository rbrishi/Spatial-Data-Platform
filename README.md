# Spatial Data Platform Backend

This project is a FastAPI backend for storing, updating, and retrieving spatial point and polygon data using a PostgreSQL database with PostGIS extension.

## Features

- CRUD API for spatial points (GeoJSON)
- CRUD API for spatial polygons (GeoJSON)
- PostgreSQL + PostGIS for spatial data storage
- SQLAlchemy ORM and Pydantic validation

## Project Structure

```
spatial_api/
  app/
    database.py
    main.py
    models.py
    routers/
      points.py
      polygons.py
    schemas.py
  requirements.txt
  README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rbrishi/Spatial-Data-Platform.git
   cd Spatial-Data-Platform
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the database:**
   - Set up PostgreSQL and enable the PostGIS extension.
   - Create a `.env` file in the project root with your database credentials:
     ```
     DB_HOST=localhost
     DB_PORT=5432
     DB_NAME=spatial_db
     DB_USER=username
     DB_PASSWORD=password
     ```
4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```
5. **Access the API docs:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## API Endpoints

- `/points/` : CRUD for point data
- `/polygons/` : CRUD for polygon data

## Why `.env` is in .gitignore (and should NOT be in GitHub)

- The `.env` file contains sensitive information such as database credentials.
- **Never commit your `.env` file to a public repository.**
- Instead, share a `.env.example` file with placeholder values for others to configure their own environment securely.

## Example `.env.example`

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=spatial_db
DB_USER=username
DB_PASSWORD=password
```
