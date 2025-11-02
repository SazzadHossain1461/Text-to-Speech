from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def texttoSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")


entry = Entry(root)
canvas.create_window(200, 100, window=entry)

button = Button(text='Start', command=texttoSpeech)
canvas.create_window(200, 230, window=button)
root.mainloop()