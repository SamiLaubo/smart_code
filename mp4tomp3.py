# Env: Python 3.8.2 32-bit

import os
from moviepy.editor import *
# video = VideoFileClip(os.path.join("path","to","movie.mp4"))
# video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))


# video = VideoFileClip(r"C:\Users\Sami Laubo\Downloads\Tweeka TV - 50th Anniversary Marathon.mp4")
# video.audio.write_audiofile(r"C:\Users\Sami Laubo\Downloads\Tweeka TV - 50th Anniversary Marathon.mp3")

video = VideoFileClip(r"C:\Users\Sami Laubo\OneDrive - NTNU\Misc\Alarm\last ned.mp4")
video.audio.write_audiofile(r"C:\Users\Sami Laubo\OneDrive - NTNU\Misc\Alarm\jefferson.mp3")
