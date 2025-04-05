from fastapi import FastAPI, File, UploadFile, HTTPException
from app.database import db
from app.models import PlayerScore

app = FastAPI()

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

# --- Add Player Score ---
@app.post("/player_score")
async def add_score(score: PlayerScore):
    result = await db.scores.insert_one(score.dict())
    return {"message": "Score recorded", "id": str(result.inserted_id)}
