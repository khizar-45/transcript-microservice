# Transcript Microservice

A lightweight **Flask-based microservice** that fetches YouTube video transcripts (subtitles) and returns them as clean plain text.

---

## Features
- Fetches YouTube transcripts via [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/).
- Prioritizes **English subtitles** if available.
- Falls back to the **first available language** when English is not provided.
- Cleans transcript text (removes timestamps).
- Returns results in **JSON format**.

---

## Limitations
Transcripts **cannot** be fetched for:
- Age-restricted videos  
- Private videos  
- Live streams  
- Very recently uploaded videos (when subtitles aren’t generated yet)  
- Videos without any subtitles  

---

## Usage

### Endpoint
`POST /transcript`

### Request Body
```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

### Successful Response
```json
{
  "video_id": "VIDEO_ID",
  "language_used": "en",
  "transcript": "Full transcript text here..."
}
```

### Error Response
```json
{
  "error": "No transcript available"
}
```

---

## Tech Stack
- Python 3.9+
- Flask
- youtube-transcript-api
- Gunicorn (for production deployment)

---

## Installation


### 1. Clone the repo
```bash
git clone https://github.com/khizar-45/transcript-microservice
cd transcript-microservice
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
python app.py
```

#### Available at: http://localhost:5000/transcript

---

## Contact
For queries or contributions: skkhizarali45@gmail.com
