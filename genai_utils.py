import os
from dotenv import load_dotenv
import google.generativeai as genai
import re

# Load environment variables from .env
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Gemini Pro model name
MODEL_NAME = "models/gemini-1.5-pro-latest"

def generate_post_caption(photo_description: str, campaign_summary: str):
    """
    Generate a fun, friendly post caption and 4-6 trendy hashtags using Gemini Pro.
    """
    prompt = f"""
    Write a polished, fun, friendly Instagram caption for this photo:
    Description: {photo_description}
    Campaign summary: {campaign_summary}
    Then suggest 4-6 relevant, trendy hashtags (as a Python list).
    Respond ONLY with a JSON object like:
    {{"post_caption": "...", "hashtags": ["#tag1", "#tag2", ...]}}
    Do not include any extra text or explanation.
    """
    
    # Create the model
    model = genai.GenerativeModel(MODEL_NAME)
    
    # Generate content
    response = model.generate_content(prompt)
    
    # Parse response as JSON
    import json
    text = response.text if hasattr(response, 'text') and response.text else ''
    print("RAW MODEL OUTPUT:", text)  # Debug logging
    try:
        result = json.loads(text)
        return result["post_caption"], result["hashtags"]
    except Exception:
        # Try to extract JSON substring using regex
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            try:
                result = json.loads(match.group(0))
                return result.get("post_caption", ""), result.get("hashtags", [])
            except Exception:
                pass
        # Fallback: try to extract manually
        lines = text.splitlines() if text else []
        caption = lines[0].replace('post_caption:', '').strip() if lines else ''
        hashtags = []
        for line in lines:
            if line.strip().startswith('['):
                try:
                    hashtags = json.loads(line.strip())
                except Exception:
                    pass
        return caption, hashtags

def summarize_campaign(campaign_brief: str):
    """
    Summarize a campaign brief into 2-3 influencer-friendly sentences using Gemini Pro.
    """
    prompt = f"""
    Summarize the following campaign brief into 2-3 short, influencer-friendly sentences:
    {campaign_brief}
    """
    
    # Create the model
    model = genai.GenerativeModel(MODEL_NAME)
    
    # Generate content
    response = model.generate_content(prompt)
    
    text = response.text if hasattr(response, 'text') and response.text else ''
    return text.strip() 