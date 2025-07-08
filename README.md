# GenAI Influencer Content Utility

## Overview
This project provides a GenAI-powered utility to help influencers and campaign managers transform casual photo descriptions into engaging social media captions and campaign-relevant hashtags. It also summarizes campaign briefs and recommends hashtags using semantic similarity.

## Features
- Generate fun, friendly post captions and trendy hashtags from influencer-written descriptions and campaign summaries.
- Summarize campaign briefs into short, influencer-friendly text.
- Recommend relevant hashtags for any photo description using semantic embeddings.
- Easily extensible for new hashtags, campaigns, or locations.

## Setup Instructions
1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv_new
   .\venv_new\Scripts\Activate.ps1  # On Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up your environment variables:**
   - Create a `.env` file with your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     MY_API_KEY=your_super_secret_api_key_here
     ```
5. **Generate hashtag embeddings:**
   ```sh
   python generate_hashtag_embeddings.py
   ```
6. **Run the API server:**
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

### 1. `/generate_post`
- **POST**
- **Request Body:**
  ```json
  {
    "photo_description": "string",
    "campaign_summary": "string",
    "location": "string"  // Optional, if enabled
  }
  ```
- **Response:**
  ```json
  {
    "post_caption": "string",
    "hashtags": ["string", ...]
  }
  ```

### 2. `/get_hashtags`
- **POST**
- **Request Body:**
  ```json
  {
    "photo_description": "string",
    "location": "string"  // Optional, if enabled
  }
  ```
- **Response:**
  ```json
  {
    "matched_hashtags": ["string", ...]
  }
  ```

### 3. `/summarize_campaign`
- **POST**
- **Request Body:**
  ```json
  {
    "campaign_brief": "string"
  }
  ```
- **Response:**
  ```json
  {
    "summary": "string"
  }
  ```

## Regenerating Hashtag Embeddings
- Edit the hashtag list in `generate_hashtag_embeddings.py` as needed.
- Run:
  ```sh
  python generate_hashtag_embeddings.py
  ```
- This will update `hashtags.csv` with new embeddings.

## Extensibility Notes
- To add new hashtags, update the list in `generate_hashtag_embeddings.py` and rerun the script.
- To support new input fields (e.g., location), update the request models and logic in `main.py` and `embedding_utils.py`.
- For production, consider using managed services like Vertex AI Vector Search and Endpoints.

## Example Test Cases
See the `test_cases.md` file for sample inputs and expected outputs. 

from fastapi import Security
from fastapi.security.api_key import APIKeyHeader 

api_key_header = APIKeyHeader(name="x-api-key", auto_error=True)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

@app.post("/generate_post", response_model=GeneratePostResponse, dependencies=[Depends(verify_api_key)])
# ...etc...
