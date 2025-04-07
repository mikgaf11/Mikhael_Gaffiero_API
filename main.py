# Import addons needed
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi import status
import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load the environment
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Create the FastAPI app instance
app = FastAPI()

# Connect to MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["multimedia_db"]

class PlayerScore(BaseModel):
    player_name: str
    score: int

# --- Upload Sprite ---
@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    
    # Only allow certain file types
    allowed_extensions = [".png", ".jpg", ".jpeg"]

    filename = file.filename.lower()
    if not any(filename.endswith(ext) for ext in allowed_extensions):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .png, .jpg, .jpeg allowed.")

    # Read and save the file to Mongo
    content = await file.read()
    sprite_doc = {
        "filename": filename,
        "content": content
    }
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}


# --- Upload Audio ---
@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    
    # reading and saving audio file
    content = await file.read()
    audio_doc = {
        "filename": file.filename,
        "content": content
    }
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio uploaded", "id": str(result.inserted_id)}

# --- Add Score ---
@app.post("/player_score")
async def add_score(score: PlayerScore):
    
    # Validate score before saving
    if score.score < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Score must be positive.")
    
    # Save player score to database
    result = await db.scores.insert_one(score.dict())
    return {"message": "Score recorded", "id": str(result.inserted_id)}


