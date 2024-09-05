import moviepy.editor as mp
import os
import streamlit as st

def convert_video(input_file_path, output_file_path):
    try:
        # Load the video file
        video = mp.VideoFileClip(input_file_path)
        
        # Write the video to the desired format
        video.write_videofile(output_file_path, codec='libx264', audio_codec='aac')
        
        st.success(f"Conversion complete! The file has been saved to {output_file_path}")
    except Exception as e:
        st.error(f"An error occurred while converting the file: {e}")

# Streamlit UI
st.title("Video Format Converter")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv", "flv", "wmv"])
if uploaded_file is not None:
    input_video_path = f"temp_input.{uploaded_file.name.split('.')[-1]}"
    with open(input_video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    output_format = st.selectbox("Select the desired output format", ["avi", "mp4", "mkv", "flv", "wmv"])
    output_video_path = f"output_video.{output_format}"
    
    if st.button("Convert"):
        convert_video(input_video_path, output_video_path)
        with open(output_video_path, "rb") as f:
            st.download_button("Download Converted Video", f, file_name=output_video_path)
