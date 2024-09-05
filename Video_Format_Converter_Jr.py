import moviepy.editor as mp
import os
import streamlit as st

# Define available codecs for each format
codecs = {
    "mp4": ["libx264", "libx265", "mpeg4", "None"],
    "avi": ["mpeg4", "libxvid", "None"],
    "mkv": ["libx264", "libx265", "mpeg4", "None"],
    "flv": ["libx264", "None"],
    "wmv": ["wmv2", "vc1", "None"]
}

def convert_video(input_file_path, output_file_path, codec):
    try:
        # Load the video file
        video = mp.VideoFileClip(input_file_path)
        
        # Write the video to the desired format
        if codec == "None":
            video.write_videofile(output_file_path, audio_codec='aac')
        else:
            video.write_videofile(output_file_path, codec=codec, audio_codec='aac')
        
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
    
    # Display codec options based on selected format
    codec = st.selectbox("Select the codec for the output format", codecs[output_format])
    
    output_video_path = f"output_video.{output_format}"
    
    if st.button("Convert"):
        convert_video(input_video_path, output_video_path, codec)
        with open(output_video_path, "rb") as f:
            st.download_button("Download Converted Video", f, file_name=output_video_path)
