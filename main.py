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
