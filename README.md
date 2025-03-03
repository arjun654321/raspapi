# Emoji Sentiment API

## Overview
The **Emoji Sentiment API** is a simple FastAPI-based web service that provides sentiment analysis for emojis. It allows users to retrieve predefined emoji sentiments, get random emoji sentiment, and add new emojis with their respective sentiment categories.


## Features
- Get a list of supported emojis
- Get a list of sentiment categories
- Retrieve sentiment for a specific emoji
- Add a new emoji with a sentiment category
- Fetch a random emoji with its sentiment
- Retrieve all emojis with their sentiment mappings
- Get information on what an emoji is and its history



## API Endpoints


| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/` | Get API documentation |
| GET | `/intro` | Get an introduction to the API |
| GET | `/whats-emoji` | Get information about what an emoji is |
| GET | `/history` | Get historical information about emojis |
| GET | `/emojis` | Get a list of supported emojis |
| GET | `/categories` | Get a list of sentiment categories |
| GET | `/random-emoji` | Get a random emoji with its sentiment |
| GET | `/all-emoji-sentiment` | Get all emojis with their sentiment categories |
| POST | `/emoji-category` | Get sentiment of a specific emoji (JSON: `{ "emoji": "😀" }`) |
| POST | `/add-emoji` | Add a new emoji with a sentiment category (JSON: `{ "emoji": "😎", "category": "cool" }`) |
| POST | `/emoji-category-nlp`|  Get sentiment of a specific emoji (JSON: `{ "emoji": "😀" }`) using AI/NLP |
| POST | `/text-to-emoji`|  Get emojis from a text (JSON: `{ "text": "I am hapay today" }`) |




## Future Enhancements
- Implement an AI model to dynamically predict emoji sentiment.
- Expand the emoji dataset to support more emojis.
- Improve API security and authentication.



