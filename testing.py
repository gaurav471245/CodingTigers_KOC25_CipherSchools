import random
from gtts import gTTS
import os

language = 'en'

list_story = ['one.txt', 'two.txt', 'three.txt', 'four.txt', 'five.txt']
choose = random.randint(0, 4)
with open(list_story[choose], 'r') as f:
    myobj = gTTS(text=f.read(), lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("../welcome.mp3")
