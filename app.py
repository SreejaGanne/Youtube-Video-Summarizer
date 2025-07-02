import os
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import OpenAI

# Set your OpenAI API Key here
os.environ["OPENAI_API_KEY"] = "your-openai-key"

client = OpenAI()

st.title("🎥 YouTube Video Summarizer")
st.write("Summarize any YouTube video that has subtitles using GPT-3.5")

video_url = st.text_input("Enter YouTube video URL")

if st.button("Summarize"):
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([t['text'] for t in transcript])

        st.subheader("Transcript Preview:")
        st.write(full_text[:800] + "...")

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(full_text)

        summaries = []
        for i, chunk in enumerate(chunks):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Summarize the following transcript chunk:"},
                    {"role": "user", "content": chunk}
                ]
            )
            summary = response.choices[0].message.content
            summaries.append(summary)

        final_summary = "\n\n".join(summaries)
        st.subheader("Final Summary:")
        st.write(final_summary)

    except Exception as e:
        st.error(f"An error occurred: {e}")
