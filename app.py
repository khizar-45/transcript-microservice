from flask import Flask, request, jsonify
from youtube_transcript_api import ( YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled )
from youtube_transcript_api.proxies import WebshareProxyConfig

app = Flask(__name__)

ytt_api = YouTubeTranscriptApi()

def get_video_id(url_link):
    if "youtu.be/" in url_link:
        return url_link.split("youtu.be/")[-1].split("?")[0]
    elif "watch?v=" in url_link:
        return url_link.split("watch?v=")[-1].split("&")[0]
    return None

@app.route("/transcript", methods=["POST"])
def fetch_transcript():
    data = request.get_json() or {}
    video_url = data.get("video_url")
    if not video_url:
        return jsonify({"error": "No video_url provided"}), 400

    video_id = get_video_id(video_url)
    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    try:
        transcript = ytt_api.fetch(video_id, languages=["en"])
        lang_used = "en"

    except NoTranscriptFound:
        try:
            t_list = ytt_api.list(video_id)
            chosen = next(iter(t_list))
            transcript = chosen.fetch()
            lang_used = chosen.language_code
        except (NoTranscriptFound, TranscriptsDisabled):
            return jsonify({"error": "No transcript available"}), 404 
        
    except Exception as e:
        return jsonify({"error": str(e).replace("\n", " ")}), 400

    plain_text = " ".join([seg.text for seg in transcript])

    return jsonify({
        "video_id": video_id,
        "language_used": lang_used,
        "transcript": plain_text
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)