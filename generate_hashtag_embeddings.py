import os
import csv
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
EMBED_MODEL = "models/embedding-001"

# Broad, general list of hashtags
HASHTAGS = [
    '#Foodie', '#Yum', '#Delicious', '#FoodLover', '#InstaFood', '#HealthyEats', '#HomeCooking',
    '#TravelGram', '#Wanderlust', '#AdventureTime', '#ExploreMore', '#VacationVibes',
    '#OOTD', '#Fashionista', '#StyleInspo', '#Trendy',
    '#FitLife', '#Wellness', '#HealthyLifestyle', '#WorkoutMotivation',
    '#LifeGoals', '#Inspiration', '#Motivation', '#GoodVibes',
    '#Memories', '#GoodTimes', '#Celebration', '#HappyDays',
    '#Viral', '#Trending', '#ForYou', '#InstaGood',
    '#Nature', '#Photography', '#Art', '#Beauty', '#SelfCare', '#Love', '#Friends', '#Family'
]

def embed_text(text: str):
    response = genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )
    if not response['embedding']:
        raise ValueError(f"No embedding returned for {text}")
    return response['embedding']

with open('hashtags.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for tag in HASHTAGS:
        emb = embed_text(tag)
        writer.writerow([tag, str(emb)])

print(f"Wrote {len(HASHTAGS)} hashtag embeddings to hashtags.csv") 