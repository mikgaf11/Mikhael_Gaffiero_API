from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load Mongo URI from .env
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to client
client = MongoClient(MONGO_URI)

# Choose database and collection
db = client["DB_Assignment"]
audio_collection = db["Audio"]

# Insert mock documents
mock_data = [
    {
        "name": "explosion.wav",
        "type": "sound_effect",
        "duration": 3.2,
        "format": "wav",
        "uploaded_by": "Mikhail",
        "tags": ["explosion", "loud", "battle"]
    },
    {
        "name": "menu_music.mp3",
        "type": "background_music",
        "duration": 45.0,
        "format": "mp3",
        "uploaded_by": "Mikhail",
        "tags": ["menu", "ambient", "loop"]
    }
]

result = audio_collection.insert_many(mock_data)
print(f"✅ Inserted {len(result.inserted_ids)} documents into 'Audio' collection.")

#sprites mock data
sprites_collection = db["Sprites"]

sprite_data = [
    {
        "name": "hero_idle.png",
        "type": "character",
        "resolution": "64x64",
        "uploaded_by": "Mikhail",
        "tags": ["idle", "hero", "sprite"]
    },
    {
        "name": "enemy_walk.png",
        "type": "enemy",
        "resolution": "64x64",
        "uploaded_by": "Mikhail",
        "tags": ["walk", "enemy", "sprite"]
    }
]

sprites_result = sprites_collection.insert_many(sprite_data)
print(f"✅ Inserted {len(sprites_result.inserted_ids)} documents into 'Sprites' collection.")

#scores mock data
scores_collection = db["Scores"]

scores_data = [
    {
        "player_name": "Alex",
        "score": 1500,
        "level": 5,
        "date": "2025-04-05"
    },
    {
        "player_name": "Sam",
        "score": 2200,
        "level": 6,
        "date": "2025-04-04"
    }
]

scores_result = scores_collection.insert_many(scores_data)
print(f"✅ Inserted {len(scores_result.inserted_ids)} documents into 'Scores' collection.")


