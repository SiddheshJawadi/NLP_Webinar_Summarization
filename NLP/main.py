import moviepy.editor as mp
from assembly_api import *
def convert(name):
    video = mp.VideoFileClip(name)
    video.audio.write_audiofile("converted.wav")

print("Please enter the name of video file you want to summarize along with its type...... eg: test.mp4")
name = input()
convert(name)
def start():
    filename = "converted.wav"
    audio_url = upload(filename)

    save_transcript(audio_url, "output1")
print("The video has been converted to wav format successfully.")
start()