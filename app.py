$updateMultimediaDB = @'
import json
from pathlib import Path

db_path = Path(r"D:\fluency-data-mar12\reference_data\word_dictionaries\multi_entertainment_entities_db_defn.json")

# Load existing DB
if db_path.exists():
    with open(db_path, 'r', encoding='utf-8') as f:
        ent_db = json.load(f)
else:
    ent_db = {}

# 1. BOOKS DOMAIN
ent_db['books'] = {
    "keywords": ["author", "book", "novel", "reading", "series", "chapter"],
    "entities": {
        "harry potter": "Harry Potter",
        "hogwarts": "Hogwarts",
        "j k rowling": "J.K. Rowling"
    }
}

# 2. MOVIES DOMAIN
ent_db['movies'] = {
    "keywords": ["sequel", "actor", "actress", "movie", "film", "cliff", "villain"],
    "entities": {
        "mission impossble": "Mission Impossible",
        "tom cruise": "Tom Cruise",
        "supporting actoress": "supporting actress",
        "supporting mal e actor": "supporting male actor"
    }
}

# 3. TV SHOWS DOMAIN
ent_db['tv_shows'] = {
    "keywords": ["tv show", "episode", "season", "adaptation", "streaming"],
    "entities": {
        "tv show": "TV show",
        "new season": "new season"
    }
}

# 4. SPORTS DOMAIN
ent_db['sports'] = {
    "keywords": ["match", "game", "goal", "referee", "player", "coach"],
    "entities": {
        "football match": "football match",
        "penalty kick": "penalty kick",
        "striker": "striker",
        "winning goal": "winning goal"
    }
}

# Save
with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(ent_db, f, indent=4, ensure_ascii=False)

print("✅ Multimedia Entertainment DB updated successfully!")
print(f"   Domains active: {list(ent_db.keys())}")
'@

$updateMultimediaDB | Out-File -FilePath "D:\fluency-mvp\code\update_multimedia_db.py" -Encoding utf8
& "D:\fluency-mvp\venv\Scripts\python.exe" "D:\fluency-mvp\code\update_multimedia_db.py"
