# 🎥 YouTube Video Summarizer using GPT-3.5

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit&logoColor=white)](https://your-streamlit-app-link.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This project is a simple Streamlit web app that summarizes the content of a YouTube video using OpenAI's GPT-3.5 model. It extracts the video transcript, chunks it using LangChain, and generates a concise summary in the same language as the original video.

---

## 🚀 Features

✅ Extracts transcript from YouTube videos  
✅ Splits long transcripts into chunks using LangChain  
✅ Summarizes each chunk using GPT-3.5  
✅ Merges all chunks into a complete, easy-to-read summary  
✅ Clean and interactive Streamlit web interface

---

## 📌 How It Works

1. Enter a valid YouTube video URL (with captions/subtitles enabled).
2. The app fetches the transcript using YouTube Transcript API.
3. The transcript is broken into manageable chunks.
4. Each chunk is summarized using OpenAI's GPT-3.5.
5. The final summary is displayed to the user.

---

## 💻 Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key in app.py or as an environment variable:
```python
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

4. Run the app:
```bash
streamlit run app.py
```

---

## 🧪 Example Input

Paste this video URL:  
https://www.youtube.com/watch?v=iCvmsMzlF7o

📝 The app will output a clean summary of Brené Brown’s TED Talk.

---

## 📁 Project Structure

```
youtube_summarizer/
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Technologies Used

- Python
- Streamlit
- OpenAI GPT-3.5
- YouTube Transcript API
- LangChain

---

## 🌐 Live Demo

🚀 Try it out here: [Streamlit Cloud App](https://your-streamlit-app-link.streamlit.app/)

> Make sure to set your OpenAI API key to use the app.

---

## 📸 Screenshot

You can include a screenshot of your app like this:

![App Screenshot](https://user-images.githubusercontent.com/your-username/screenshot.png)

---

## 📄 License

This project is licensed under the MIT License.

