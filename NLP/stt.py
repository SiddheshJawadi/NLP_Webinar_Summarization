import speech_recognition as sr
import moviepy.editor as mp


clip = mp.VideoFileClip(r"trial_video.mp4") 
clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()

harvard = sr.AudioFile('converted.wav')

with harvard as source:
    audio = r.record(source, duration=200)
print(type(audio))
result = r.recognize_google(audio)
with open('recognized.txt',mode ='w') as file: 
    file.write(result) 
    print("ready!")