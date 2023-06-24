import yt_dlp
import speech_recognition as sr
from pydub import AudioSegment


# Download the video using yt-dlp
ydl_opts = {'format': 'bestaudio/best'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info('https://www.youtube.com/watch?v=VVxXIUYjRmQ', download=False)
    audio_url = info_dict['url']

# Load audio file
r = sr.AudioFile('Запись.wav')

# Initialize recognizer
recognizer = sr.Recognizer()

# Open the audio file using the recognizer
with r as source:
    audio_text = recognizer.record(source)

# Convert audio to text
text = recognizer.recognize_google(audio_text, language='ru-RU')
print(text)

# # Download the audio file and save as .wav format
# r = sr.Recognizer()
# audio_data = sr.AudioFile(audio_url)
# # with audio_data as source:
# #     audio_file = r.record(source)
# #     audio = AudioSegment.from_file(source)
# # audio.export("audio.wav", format="wav")
#
# # Transcribe the audio into text using Google's speech recognition API
# with sr.AudioFile("Запись.wav") as source:
#     audio = r.record(source)
# text = r.recognize_google(audio)
# print(text)
#
# # Divide the text into logical paragraphs
# text = text.replace("\n", " ")
# paragraphs = text.split(". ")
# for i, para in enumerate(paragraphs):
#     # Output each paragraph with its corresponding timecode in the video
#     time_in_seconds = audio.get_position() / 1000
#     print("Paragraph {}: {} ({} seconds)".format(i+1, para, time_in_seconds))
