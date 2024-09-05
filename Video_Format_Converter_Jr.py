import ffmpeg
import subprocess
import json
import os
import streamlit as st
import requests
import tarfile

def download_ffmpeg():
    url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz"
    ffmpeg_dir = "bin"
    ffmpeg_tar_path = os.path.join(ffmpeg_dir, "ffmpeg.tar.xz")

    if not os.path.exists(ffmpeg_dir):
        os.makedirs(ffmpeg_dir)

    # Download ffmpeg tar file
    if not os.path.exists(ffmpeg_tar_path):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(ffmpeg_tar_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    # Extract ffmpeg binary
    with tarfile.open(ffmpeg_tar_path) as tar:
        tar.extractall(path=ffmpeg_dir)
        extracted_dir = tar.getnames()[0].split('/')[0]
        ffmpeg_path = os.path.join(ffmpeg_dir, extracted_dir, "ffmpeg")

    return ffmpeg_path

def get_codec_info(file_path):
    """Get codec information of the video using ffprobe."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=codec_name", "-of", "json", file_path],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        codec_info = json.loads(result.stdout)
        return codec_info['streams'][0]['codec_name']
    except Exception as e:
        st.error(f"An error occurred while getting codec information: {e}")
        return None

def convert_video(input_file_path, output_file_path):
    try:
        # Download ffmpeg binary if not present
        ffmpeg_path = download_ffmpeg()
        os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

        # Check if the output file already exists
        if os.path.exists(output_file_path):
            overwrite = st.radio(f"File '{output_file_path}' already exists. Overwrite?", ('Yes', 'No'))
            if overwrite != 'Yes':
                st.warning("Not overwriting the existing file. Exiting.")
                return

        # Get the video codec of the input file
        video_codec = get_codec_info(input_file_path)
        
        # Set encoding options to strip the encoding
        encoding_options = {'vcodec': 'copy', 'acodec': 'copy'}
        
        # Convert the video to the desired format using the specified codec and options
        (
            ffmpeg
            .input(input_file_path)
            .output(output_file_path, **encoding_options)
            .run(overwrite_output=True)
        )
        st.success(f"Conversion complete! The file has been saved to {output_file_path}")
    except ffmpeg.Error as e:
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
