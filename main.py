#   Organize Desktop
#   Files: Images, Videos, ScreenShots audio files
#   Into specifed folders

import os
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", ".MOV")
img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif", ".JPG")

#TODO 1, Automaticly create images, Audio, screens and video folders in users documents. not if already exisits
# Use crontab.guru to set up automation of this task every sunday

def is_video(file):
    """
    Takes files from given directory as input
    .splitext: splits extention from filename
    if extention is in our list of video file extentions it returns
    """
    return os.path.splitext(file)[1] in video
def is_screenshot(file):
    name, ext = os.path.splitext(file)
    #If screen shot is specified within the name
    return (ext in img) and "screenshot" or "screen shot" in name.lower()
def is_image(file):
    return os.path.splitext(file)[1] in img
def is_audio(file):
    return os.path.splitext(file)[1] in audio

#   Change working Directory to desktop
os.chdir("/Users/apjenkins/Desktop")



#   For file in working Directory
for file in os.listdir():
    if is_video(file):
        shutil.move(file, "/Users/apjenkins/Documents/Videos")
    elif is_audio(file):
        shutil.move(file, "/Users/apjenkins/Documents/Audio")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, "/Users/apjenkins/Documents/ScreenShots")
        else:
            shutil.move(file, "/Users/apjenkins/Documents/Images")
    else:
        shutil.move(file, "/Users/apjenkins/Documents")