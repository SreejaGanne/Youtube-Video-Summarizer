# YouTube Video Summarizer

This project is a simple Streamlit app that takes a YouTube video URL, fetches its transcript, splits it into chunks, and generates a summary using OpenAI GPT-3.5.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your OpenAI API key to `app.py`:
```python
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

3. Start the app:
```
streamlit run app.py
```

4. Paste a YouTube link and get the summary!

Ensure the video has subtitles (closed captions).
