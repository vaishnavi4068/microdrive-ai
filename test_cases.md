# API Test Cases

## 1. /generate_post
### Test Case 1
**Input:**
```json
{"photo_description": "KFC pic from my visit", "campaign_summary": "User should upload food photos to the campaign website as part of the Chicago KFC Microdrive campaign and submit a screenshot as proof.", "location": "Chicago"}
```
**Expected Output:**
- post_caption: Fun, friendly caption mentioning KFC, uploading, and the campaign, with location context
- hashtags: 4-6 relevant hashtags (e.g., #KFCChicago, #MicrodriveChallenge, etc.)

### Test Case 2
**Input:**
```json
{"photo_description": "Sunset yoga on the beach", "campaign_summary": "Promoting wellness and mindfulness through daily yoga sessions.", "location": "Miami"}
```
**Expected Output:**
- post_caption: Fun caption about yoga, wellness, and the beach
- hashtags: 4-6 relevant hashtags (e.g., #Wellness, #Yoga, #BeachLife, etc.)

### Test Case 3
**Input:**
```json
{"photo_description": "Homemade vegan tacos for dinner", "campaign_summary": "Encouraging plant-based meals for a healthier lifestyle.", "location": "Los Angeles"}
```
**Expected Output:**
- post_caption: Caption about vegan food, healthy eating
- hashtags: 4-6 relevant hashtags (e.g., #Vegan, #HealthyEats, etc.)

### Test Case 4
**Input:**
```json
{"photo_description": "Hiking with friends in the mountains", "campaign_summary": "Share your outdoor adventures for a chance to win gear.", "location": "Denver"}
```
**Expected Output:**
- post_caption: Caption about hiking, adventure, friends
- hashtags: 4-6 relevant hashtags (e.g., #AdventureTime, #Friends, etc.)

### Test Case 5
**Input:**
```json
{"photo_description": "Latte art at my favorite cafe", "campaign_summary": "Highlighting local coffee shops and baristas.", "location": "Seattle"}
```
**Expected Output:**
- post_caption: Caption about coffee, cafes, local spots
- hashtags: 4-6 relevant hashtags (e.g., #CoffeeLover, #Cafe, etc.)

---

## 2. /get_hashtags
### Test Case 1
**Input:**
```json
{"photo_description": "Delicious vegan burger with avocado and sweet potato fries", "location": "Austin"}
```
**Expected Output:**
- matched_hashtags: List of 5 relevant hashtags (e.g., #Vegan, #Yum, #HealthyEats, etc.), with location context

### Test Case 2
**Input:**
```json
{"photo_description": "Sunrise run along the river", "location": "Boston"}
```
**Expected Output:**
- matched_hashtags: List of 5 relevant hashtags (e.g., #FitLife, #Motivation, etc.)

### Test Case 3
**Input:**
```json
{"photo_description": "Family picnic in the park with homemade sandwiches", "location": "San Francisco"}
```
**Expected Output:**
- matched_hashtags: List of 5 relevant hashtags (e.g., #Family, #Foodie, #GoodTimes, etc.)

### Test Case 4
**Input:**
```json
{"photo_description": "Street art in the city center", "location": "New York"}
```
**Expected Output:**
- matched_hashtags: List of 5 relevant hashtags (e.g., #Art, #Photography, #InstaGood, etc.)

### Test Case 5
**Input:**
```json
{"photo_description": "Celebrating my birthday with friends at a rooftop bar", "location": "Chicago"}
```
**Expected Output:**
- matched_hashtags: List of 5 relevant hashtags (e.g., #Celebration, #Friends, #GoodTimes, etc.)

---

## 3. /summarize_campaign
### Test Case 1
**Input:**
```json
{"campaign_brief": "Participants are encouraged to share photos of their favorite summer activities on social media using our campaign hashtag. The most creative entries will be featured on our official page and have a chance to win exclusive merchandise."}
```
**Expected Output:**
- summary: Short, influencer-friendly summary about sharing summer activities, using the hashtag, and winning merch

### Test Case 2
**Input:**
```json
{"campaign_brief": "Share your best homemade recipes for a chance to be featured in our community cookbook. All cuisines welcome!"}
```
**Expected Output:**
- summary: Short summary about sharing recipes, being featured, and inclusivity

### Test Case 3
**Input:**
```json
{"campaign_brief": "Document your daily fitness journey and inspire others to stay active. Top posts will be highlighted on our page."}
```
**Expected Output:**
- summary: Short summary about fitness, inspiration, and being highlighted

### Test Case 4
**Input:**
```json
{"campaign_brief": "Post a photo of your favorite local business and tell us why you love it. Support your community and win prizes!"}
```
**Expected Output:**
- summary: Short summary about supporting local, sharing stories, and winning prizes

### Test Case 5
**Input:**
```json
{"campaign_brief": "Join our art challenge by submitting your original artwork. Winners will be showcased in our online gallery."}
```
**Expected Output:**
- summary: Short summary about art challenge, submitting artwork, and being showcased 