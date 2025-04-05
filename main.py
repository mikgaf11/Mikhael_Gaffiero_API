from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

app = FastAPI()

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["multimedia_db"]

# Pydantic model for scores
class PlayerScore(BaseModel):
    player_name: str
    score: int

# --- Upload Sprite ---
@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    content = await file.read()
    sprite_doc = {
        "filename": file.filename,
        "content": content
    }
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

# --- Upload Audio ---
@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
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
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}
