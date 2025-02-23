from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import random
from typing import List, Dict
from scalar_fastapi import get_scalar_api_reference
from emoji import demojize,emojize
import re

app = FastAPI()


emoji_category = {
    "😀": "happy", "😢": "sad", "😡": "angry", "😂": "happy",
    "😍": "happy", "😔": "sad", "🤬": "angry", "😭": "sad",
    "😆": "happy", "😠": "angry", "😊": "happy", "😞": "sad",
    "😁": "happy", "😖": "sad", "😤": "angry", "😇": "happy"
}


class EmojiRequest(BaseModel):
    emoji: str

class AddEmojiRequest(BaseModel):
    emoji: str
    category: str


@app.get("/")
def root():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )



@app.get("/intro")
def intro():
    return {
        "Message": (
            "Welcome to the Emoji Sentiment API! \n (Currently, this API works only for the emojis mentioned in the code, and emojis are premapped to the sentiment categories. In future enhancements, an AI model will be used to predict the sentiment of the emoji.) \n To get the information on what is emoji, use /whats-emoji endpoint. \n To get the information on emoji history, use /history endpoint. \n To get the list of supported emojis, use /emojis endpoint. \n To get the list of sentiment categories, use /categories endpoint. \n To get a random emoji and its sentiment, use /random-emoji endpoint. \n To get all emojis and their category, use /all-emoji-sentiment endpoint. \n To get the sentiment of a specific emoji, use /emoji-category endpoint, post request with JSON data {'emoji': '<emoji>'}. \n To add an emoji and its sentiment category, use /add-emoji endpoint, post request with JSON data {'emoji': '<emoji>', 'category': '<category>'}.\n  To get the sentiment of a specific emoji by using AI/nlp, use /emoji-category-nlp endpoint, post request with JSON data {'emoji': '<emoji>'}. \n To get the emoji for a given text, use /text-to-emoji endpoint, post request with JSON data {'text': '<text>'}.  "
        )
    }


@app.get("/whats-emoji")
def whats_emoji():
    message = (
        "A small digital image or icon used to express an idea or emotion. The primary function of modern emoji is to fill in emotional cues otherwise missing from typed conversation. Emojis exist in various genres, including facial expressions, activity, food and drinks, celebrations, flags, objects, symbols, places, types of weather, animals, and nature."
    )
    return {"message": message}




@app.get("/history")
def emoji_history():
    history = (
        "Emojis were first created in 1999 by Shigetaka Kurita, a Japanese designer, who was working for the company NTT DoCoMo. Kurita developed a set of 176 characters for mobile phones. These initial emojis were influenced by Japanese comic art and road signs, and they quickly became popular in Japan. Over time, emojis were standardized globally by Unicode."
    )
    return {"history": history}




@app.get("/emojis")
def emojis():
    return {"supported_emojis": list(emoji_category.keys())}



@app.get("/categories")
def get_sentiment_categories():
    categories = list(set(emoji_category.values()))
    return {"categories": categories}



@app.get("/random-emoji")
def random_emoji():
    emoji = random.choice(list(emoji_category.keys()))
    category = emoji_category.get(emoji, "unknown")
    return {"emoji": emoji, "category": category}





@app.get("/all-emoji-sentiment")
def all_sentiment():
    return {"emoji_categories": emoji_category}




@app.post("/emoji-category")
def get_sentiment(request: EmojiRequest):
    emoji = request.emoji
    category = emoji_category.get(emoji, "unknown")
    return {"emoji": emoji, "category": category}



@app.post("/add-emoji")
def add_emoji(request: AddEmojiRequest):
    emoji = request.emoji
    category = request.category

    if emoji in emoji_category:
        raise HTTPException(status_code=400, detail=f"emoji '{emoji}' already present, try another emoji.")

    emoji_category[emoji] = category
    return {"message": f"emoji '{emoji}' added with category '{category}'."}







@app.post("/emoji-category-nlp")
def detect_using_nlp(request: EmojiRequest):
    emoji_text = demojize(request.emoji) 
    
    if emoji_text.startswith(":") and emoji_text.endswith(":"):
        words = re.findall(r'\b\w+\b', emoji_text)  
        if words:
            return {"emoji": request.emoji, "category": words[0]}
    
    return {"emoji": request.emoji, "category": "unknown"}




@app.post("/text-to-emoji")
def text_to_emoji(request: TextRequest):
    
    text = request.text.lower()
    

    category = "neutral"
    if any(word in text for word in ["happy", "joy", "excited", "good"]):
        category = "happy"
    elif any(word in text for word in ["sad", "unhappy", "depressed", "down"]):
        category = "sad"
    elif any(word in text for word in ["angry", "mad", "furious"]):
        category = "angry"


    emoji = [key for key, value in emoji_category.items() if value == category]
    return {"text": text, "category": category, "emoji": emoji[0] if emoji else "no emoji found"}
