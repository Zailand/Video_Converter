{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "935f8102-c619-4199-835d-21b3f4018d70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the desired output format (e.g., avi, mp4, mkv):  avi\n",
      "File 'RPReplay_Final1725520768 1.avi' already exists. Overwrite? [y/N]:  y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conversion complete! The file has been saved to RPReplay_Final1725520768 1.avi\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ffmpeg version 4.2.7-0ubuntu0.1 Copyright (c) 2000-2022 the FFmpeg developers\n",
      "  built with gcc 9 (Ubuntu 9.4.0-1ubuntu1~20.04.1)\n",
      "  configuration: --prefix=/usr --extra-version=0ubuntu0.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-avresample --disable-filter=resample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librsvg --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-nvenc --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared\n",
      "  libavutil      56. 31.100 / 56. 31.100\n",
      "  libavcodec     58. 54.100 / 58. 54.100\n",
      "  libavformat    58. 29.100 / 58. 29.100\n",
      "  libavdevice    58.  8.100 / 58.  8.100\n",
      "  libavfilter     7. 57.100 /  7. 57.100\n",
      "  libavresample   4.  0.  0 /  4.  0.  0\n",
      "  libswscale      5.  5.100 /  5.  5.100\n",
      "  libswresample   3.  5.100 /  3.  5.100\n",
      "  libpostproc    55.  5.100 / 55.  5.100\n",
      "Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'RPReplay_Final1725520768 1.mov':\n",
      "  Metadata:\n",
      "    major_brand     : qt  \n",
      "    minor_version   : 0\n",
      "    compatible_brands: qt  \n",
      "    creation_time   : 2024-09-05T07:21:23.000000Z\n",
      "    com.apple.quicktime.author: ReplayKitRecording\n",
      "  Duration: 00:00:36.33, start: 0.000000, bitrate: 16435 kb/s\n",
      "    Stream #0:0(und): Video: hevc (Main) (hvc1 / 0x31637668), yuvj420p(pc, bt709/bt709/iec61966-2-1), 888x1178, 16424 kb/s, 56.98 fps, 60 tbr, 600 tbn, 600 tbc (default)\n",
      "    Metadata:\n",
      "      creation_time   : 2024-09-05T07:21:23.000000Z\n",
      "      handler_name    : Core Media Video\n",
      "      encoder         : HEVC\n",
      "    Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 2 kb/s (default)\n",
      "    Metadata:\n",
      "      creation_time   : 2024-09-05T07:21:23.000000Z\n",
      "      handler_name    : Core Media Audio\n",
      "Output #0, avi, to 'RPReplay_Final1725520768 1.avi':\n",
      "  Metadata:\n",
      "    major_brand     : qt  \n",
      "    minor_version   : 0\n",
      "    compatible_brands: qt  \n",
      "    com.apple.quicktime.author: ReplayKitRecording\n",
      "    ISFT            : Lavf58.29.100\n",
      "    Stream #0:0(und): Video: hevc (Main) (hvc1 / 0x31637668), yuvj420p(pc, bt709/bt709/iec61966-2-1), 888x1178, q=2-31, 16424 kb/s, 56.98 fps, 60 tbr, 120 tbn, 120 tbc (default)\n",
      "    Metadata:\n",
      "      creation_time   : 2024-09-05T07:21:23.000000Z\n",
      "      handler_name    : Core Media Video\n",
      "      encoder         : HEVC\n",
      "    Stream #0:1(und): Audio: aac (LC) ([255][0][0][0] / 0x00FF), 44100 Hz, stereo, fltp, 2 kb/s (default)\n",
      "    Metadata:\n",
      "      creation_time   : 2024-09-05T07:21:23.000000Z\n",
      "      handler_name    : Core Media Audio\n",
      "Stream mapping:\n",
      "  Stream #0:0 -> #0:0 (copy)\n",
      "  Stream #0:1 -> #0:1 (copy)\n",
      "Press [q] to stop, [?] for help\n",
      "frame= 2070 fps=0.0 q=-1.0 Lsize=   73000kB time=00:00:36.31 bitrate=16466.9kbits/s speed= 510x    \n",
      "video:72841kB audio:9kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.205448%\n"
     ]
    }
   ],
   "source": [
    "import ffmpeg\n",
    "import subprocess\n",
    "import json\n",
    "import os\n",
    "\n",
    "def get_codec_info(file_path):\n",
    "    \"\"\"Get codec information of the video using ffprobe.\"\"\"\n",
    "    try:\n",
    "        result = subprocess.run(\n",
    "            [\"ffprobe\", \"-v\", \"error\", \"-select_streams\", \"v:0\",\n",
    "             \"-show_entries\", \"stream=codec_name\", \"-of\", \"json\", file_path],\n",
    "            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)\n",
    "        codec_info = json.loads(result.stdout)\n",
    "        return codec_info['streams'][0]['codec_name']\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred while getting codec information: {e}\")\n",
    "        return None\n",
    "\n",
    "def convert_video(input_file_path, output_file_path):\n",
    "    try:\n",
    "        # Check if the output file already exists\n",
    "        if os.path.exists(output_file_path):\n",
    "            overwrite = input(f\"File '{output_file_path}' already exists. Overwrite? [y/N]: \").strip().lower()\n",
    "            if overwrite != 'y':\n",
    "                print(\"Not overwriting the existing file. Exiting.\")\n",
    "                return\n",
    "\n",
    "        # Get the video codec of the input file\n",
    "        video_codec = get_codec_info(input_file_path)\n",
    "        \n",
    "        # Set encoding options to strip the encoding\n",
    "        encoding_options = {'vcodec': 'copy', 'acodec': 'copy'}\n",
    "        \n",
    "        # Convert the video to the desired format using the specified codec and options\n",
    "        (\n",
    "            ffmpeg\n",
    "            .input(input_file_path)\n",
    "            .output(output_file_path, **encoding_options)\n",
    "            .run(overwrite_output=True)\n",
    "        )\n",
    "        print(f\"Conversion complete! The file has been saved to {output_file_path}\")\n",
    "    except ffmpeg.Error as e:\n",
    "        print(f\"An error occurred while converting the file: {e}\")\n",
    "\n",
    "# Example usage:\n",
    "input_video_path = 'RPReplay_Final1725520768 1.mov'  # Replace with your input file path\n",
    "output_format = input(\"Enter the desired output format (e.g., avi, mp4, mkv): \")\n",
    "output_video_path = f'RPReplay_Final1725520768 1.{output_format}'  # Replace with your desired output file path\n",
    "\n",
    "convert_video(input_video_path, output_video_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "225527e5-a69c-4fd5-822b-59df6c53d259",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
