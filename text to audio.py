from gtts import gTTS
import os

f = open("Sample.txt")
x = f.read()
f.close()  # It's a good practice to close the file after reading

language = 'en'

audio = gTTS(text=x, lang=language, slow=False)

audio.save("audio.wav")
os.system("audio.wav")