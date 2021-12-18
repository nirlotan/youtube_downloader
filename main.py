import streamlit as st
from pytube import YouTube

st.title("YouTube Downloader")

# The following code executes if the users clicks the Submit button
with st.form(key='Submit'):
    type = st.selectbox("Select the type of output", ["Audio", "Video"])
    url = st.text_input("Enter the URL of the video", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    yt = YouTube(url)
    with st.spinner('Wait for it...'):
        if type == "Audio":
            t = yt.streams.filter(only_audio=True)
            t[0].download("downloads")
        elif type == "Video":
            t = yt.streams.filter(progressive=True, file_extension='mp4')
            t[0].download("downloads")
    st.success('Done!')

# Select a file to download
# --------------------------
import os

file_list = []
for filename in os.listdir("downloads"):
    file_list.append(filename)

if file_list:
    download_box = st.expander("Download", expanded=True)

    file_to_download = download_box.selectbox("Select a file to download:", file_list)
    path_to_download = "downloads/" + file_to_download
            
    with open(path_to_download, "rb") as file:
        btn = download_box.download_button(
                label="Download",
                data=file,
                file_name=file_to_download,
                mime="application/octet-stream")








