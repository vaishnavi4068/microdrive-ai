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
   python -m venv venv_new  
   .\venv_new\Scripts\Activate.ps1  # On Windows
3. **Install dependencies:**  
   pip install -r requirements.txt
4. **Store your API key in Google Cloud Secret Manager:**
   - Go to [Secret Manager](https://console.cloud.google.com/security/secret-manager) in your GCP project.
   - Create a secret named `MY_API_KEY` and paste your API key as the value.
   - Authenticate your local environment with:
     ```
     gcloud auth application-default login
     ```
5. **Generate hashtag embeddings:**  
   python generate_hashtag_embeddings.py
6. **Run the API server:**  
   uvicorn main:app --reload

## Using Google Cloud Secret Manager
- The API key for endpoint authentication is securely managed in Google Cloud Secret Manager.
- The app fetches the key at runtime using the Secret Manager client library.
- No sensitive keys are stored in code or local files.

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

### 4. `/get_hashtags_from_image`
- **POST**
- **Request:** multipart/form-data with an image file and a campaign description
- **Response:**
  ```json
  {
    "filename": "string",
    "generated_caption": "string",
    "campaign_description": "string",
    "matched_hashtags": ["string", ...]
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

## Troubleshooting
- If you see authentication errors, make sure you have run:
  ```
  gcloud auth application-default login
  ```
  and are logged in with an account that has access to Secret Manager in your GCP project.
