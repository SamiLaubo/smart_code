import glob
import re
import ffmpy
import sys
import os

def gif_to_mp4(path):
    paths = glob.glob(f"{path}\*.gif")

    print(path)
    if not os.path.exists(path + "\\mp4"):
        os.makedirs(path + "\\mp4")

    for path2 in paths:
        name = path2.split("\\")[-1]

        path2_out = path + "\\mp4\\" + name[:-4] + ".avi"
        ff = ffmpy.FFmpeg(
            inputs = {path2: None},
            outputs = {path2_out: None}
        )
        ff.run()


def print_info():
    print("""
    -- .gif to .mp4 for all .gifs in folder --
    cmd: merge.py "Path to folder"
    """)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'info':
        print_info()
    else:
        gif_to_mp4(sys.argv[1])