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
