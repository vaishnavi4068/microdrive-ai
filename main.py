from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
from genai_utils import generate_post_caption, summarize_campaign
from embedding_utils import get_top_hashtags

# Load environment variables from .env
load_dotenv()

app = FastAPI(title="Microdrive GenAI Tool", description="Endpoints for post generation, hashtag matching, and campaign summarization.")

# --- Pydantic Schemas ---
class GeneratePostRequest(BaseModel):
    photo_description: str
    campaign_summary: str

class GeneratePostResponse(BaseModel):
    post_caption: str
    hashtags: List[str]

class GetHashtagsRequest(BaseModel):
    photo_description: str

class GetHashtagsResponse(BaseModel):
    matched_hashtags: List[str]

class SummarizeCampaignRequest(BaseModel):
    campaign_brief: str

class SummarizeCampaignResponse(BaseModel):
    summary: str

# --- Endpoints ---
@app.post("/generate_post", response_model=GeneratePostResponse)
def generate_post(req: GeneratePostRequest):
    try:
        post_caption, hashtags = generate_post_caption(req.photo_description, req.campaign_summary)
        return {"post_caption": post_caption, "hashtags": hashtags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get_hashtags", response_model=GetHashtagsResponse)
def get_hashtags(req: GetHashtagsRequest):
    try:
        matched_hashtags = get_top_hashtags(req.photo_description)
        return {"matched_hashtags": matched_hashtags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize_campaign", response_model=SummarizeCampaignResponse)
def summarize_campaign_ep(req: SummarizeCampaignRequest):
    try:
        summary = summarize_campaign(req.campaign_brief)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 