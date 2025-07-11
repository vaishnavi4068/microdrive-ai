from fastapi import FastAPI, HTTPException, Security, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from genai_utils import generate_post_caption, summarize_campaign
from embedding_utils import get_top_hashtags
from fastapi.security.api_key import APIKeyHeader
from google.cloud import vision
import io
from secrets_utils import get_secret

# Load environment variables from .env
load_dotenv()

app = FastAPI(title="Microdrive GenAI Tool", description="Endpoints for post generation, hashtag matching, and campaign summarization.")

# --- Pydantic Schemas ---
class GeneratePostRequest(BaseModel):
    photo_description: str
    campaign_summary: str
    location: Optional[str] = None  # Optional

class GeneratePostResponse(BaseModel):
    post_caption: str
    hashtags: List[str]

class GetHashtagsRequest(BaseModel):
    photo_description: str
    location: Optional[str] = None  # Optional

class GetHashtagsResponse(BaseModel):
    matched_hashtags: List[str]

class SummarizeCampaignRequest(BaseModel):
    campaign_brief: str

class SummarizeCampaignResponse(BaseModel):
    summary: str

# --- Endpoints ---
api_key_header = APIKeyHeader(name="x-api-key", auto_error=True)

PROJECT_ID = "microdrive-dev"
API_KEY = get_secret("MY_API_KEY", PROJECT_ID)
print("Loaded API KEY:", API_KEY)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

@app.post("/generate_post", response_model=GeneratePostResponse)
def generate_post(
    req: GeneratePostRequest,
    api_key: str = Security(verify_api_key)
):
    try:
        # Concatenate location if provided
        desc = req.photo_description
        summary = req.campaign_summary
        if req.location:
            desc = f"{desc} Location: {req.location}"
            summary = f"{summary} Location: {req.location}"
        post_caption, hashtags = generate_post_caption(desc, summary)
        return {"post_caption": post_caption, "hashtags": hashtags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_hashtags", response_model=GetHashtagsResponse)
def get_hashtags(
    req: GetHashtagsRequest,
    api_key: str = Security(verify_api_key)
):
    try:
        # Concatenate location if provided
        desc = req.photo_description
        if req.location:
            desc = f"{desc} Location: {req.location}"
        matched_hashtags = get_top_hashtags(desc)
        return {"matched_hashtags": matched_hashtags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize_campaign", response_model=SummarizeCampaignResponse)
def summarize_campaign_ep(
    req: SummarizeCampaignRequest,
    api_key: str = Security(verify_api_key)
):
    try:
        summary = summarize_campaign(req.campaign_brief)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_hashtags_from_image")
def get_hashtags_from_image(
    image: UploadFile = File(...),
    campaign_description: str = Form(...),
    api_key: str = Security(verify_api_key)
):
    # Read image bytes
    image_bytes = image.file.read()
    client = vision.ImageAnnotatorClient()
    vision_image = vision.Image(content=image_bytes)
    # Use label detection to get tags
    response = client.label_detection(image=vision_image)
    labels = response.label_annotations
    if not labels:
        caption = "No description could be generated from the image."
    else:
        # Join top 5 labels as a description
        caption = ", ".join([label.description for label in labels[:5]])
    # Combine with campaign description
    combined_desc = f"{caption}. {campaign_description}"
    # Use existing hashtag recommendation logic
    matched_hashtags = get_top_hashtags(combined_desc)
    return {
        "filename": image.filename,
        "generated_caption": caption,
        "campaign_description": campaign_description,
        "matched_hashtags": matched_hashtags
    } 