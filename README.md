# GenAI Influencer Content Utility

A FastAPI-based tool for generating social media content, recommending hashtags, and summarizing campaigns using Google's Generative AI and Vision APIs.

## Features

- **Post Generation**: Create engaging social media captions based on campaign descriptions
- **Hashtag Recommendations**: Get relevant hashtags for your content
- **Campaign Summaries**: Generate concise summaries of marketing campaigns
- **Image Analysis**: Upload images to get caption suggestions and hashtag recommendations
- **Secure API Key Management**: Uses Google Cloud Secret Manager for secure credential storage

## Setup

### Prerequisites
- Python 3.8+
- Google Cloud Project with APIs enabled
- Google Cloud credentials configured

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd genai-rebuild
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Google Cloud authentication:
```bash
gcloud auth application-default login
```

4. Enable required APIs in Google Cloud Console:
   - Generative Language API
   - Vision API
   - Secret Manager API

5. Store your API key in Google Cloud Secret Manager:
```bash
echo -n "your-api-key-here" | gcloud secrets create genai-api-key --data-file=-
```

### Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication
All endpoints require an API key passed in the `X-API-Key` header.

### Generate Post Caption
- **POST** `/generate_post`
- Generates social media captions based on campaign description and location

### Get Hashtag Recommendations
- **POST** `/get_hashtags`
- Recommends relevant hashtags based on campaign description

### Summarize Campaign
- **POST** `/summarize_campaign`
- Creates concise summaries of marketing campaigns

### Upload Image for Hashtags
- **POST** `/upload_image_hashtags`
- Upload an image to get caption suggestions and hashtag recommendations

## Usage Examples

### Generate a post caption:
```bash
curl -X POST "http://localhost:8000/generate_post" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "campaign_description": "Summer sale for beachwear collection",
    "location": "Miami, FL"
  }'
```

### Get hashtag recommendations:
```bash
curl -X POST "http://localhost:8000/get_hashtags" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "campaign_description": "New fitness app launch"
  }'
```

## Security

- API keys are stored securely in Google Cloud Secret Manager
- All endpoints require authentication
- No sensitive data is logged or stored locally

## Contributing

Feel free to submit issues and enhancement requests!

---

*Last updated: July 11, 2025*
