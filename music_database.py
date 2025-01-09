import json
music_database = {
  "happy": ["Maruvarthai", "oh shala oh shala"],
  "sad": ["yaaro yaaro", "pagal iravai "],
  "neutral": ["New york nagaram", "Azhagoorial"]
}

def get_music_recommendation(emotion):
    return music_database.get(emotion, ["No recommendations available"])[0]
