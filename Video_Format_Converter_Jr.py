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

# Define default codecs for each format
default_codecs = {
    "mp4": "libx264",
    "avi": "mpeg4",
    "mkv": "libx264",
    "flv": "libx264",
    "wmv": "wmv2"
}

# Define bitrates for quality settings
bitrates = {
    "High": "5000k",
    "Medium": "2500k",
    "Low": "1000k"
}

def convert_video(input_file_path, output_file_path, codec, bitrate, orientation):
    try:
        # Load the video file
        video = mp.VideoFileClip(input_file_path)
        
        # Get the original dimensions
        width, height = video.size
        
        # Adjust dimensions based on the chosen orientation
        if orientation == "Portrait" and width > height:
            video = video.resize(height=width)
        elif orientation == "Landscape" and height > width:
            video = video.resize(width=height)
        
        # Write the video to the desired format with the specified quality
        if codec == "None":
            codec = default_codecs[output_file_path.split('.')[-1]]
        
        video.write_videofile(output_file_path, codec=codec, audio_codec='aac', bitrate=bitrate)
        
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
    
    # Load the video file to get its properties
    video = mp.VideoFileClip(input_video_path)
    width, height = video.size
    original_orientation = "Landscape" if width > height else "Portrait"
    
    # Display original video properties
    st.write(f"**Original Resolution:** {width} x {height}")
    st.write(f"**Original Orientation:** {original_orientation}")
    
    output_format = st.selectbox("Select the desired output format", ["avi", "mp4", "mkv", "flv", "wmv"])
    
    # Display codec options based on selected format
    codec = st.selectbox("Select the codec for the output format", codecs[output_format])
    
    # Display quality options
    quality = st.selectbox("Select the quality level", ["High", "Medium", "Low"])
    bitrate = bitrates[quality]
    
    # Display orientation options
    orientation = st.selectbox("Select the desired orientation", ["Original", "Landscape", "Portrait"])
    
    # Calculate expected output dimensions and orientation
    if orientation == "Portrait" and width > height:
        output_width, output_height = height, width
    elif orientation == "Landscape" and height > width:
        output_width, output_height = height, width
    else:
        output_width, output_height = width, height
    
    output_orientation = "Landscape" if output_width > output_height else "Portrait"
    
    # Display expected output video properties
    st.write(f"**Expected Output Resolution:** {output_width} x {output_height}")
    st.write(f"**Expected Output Orientation:** {output_orientation}")
    
    output_video_path = f"output_video.{output_format}"
    
    if st.button("Convert"):
        convert_video(input_video_path, output_video_path, codec, bitrate, orientation)
        with open(output_video_path, "rb") as f:
            st.download_button("Download Converted Video", f, file_name=output_video_path)
