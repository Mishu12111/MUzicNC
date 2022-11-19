import os
from mutagen.mp3 import MP3
from pygame import mixer
import time
import __main__
mixer.init()
n = 0

dir_path = r'D:\python\VaraPython\PyCharm Community Edition 2022.1.2\MUSICAINPAUZE\Music'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
def algoritm( j,k,i,timp):
    for j in range(2):
        print("j este :", j)
        print("acesta este k:",k)
        audio = MP3(f'Music/{j+k}.mp3')
        print("sa inceapa muzica")
        pauza = int(audio.info.length)
        mixer.music.load(f'Music/{j + k }.mp3')
        mixer.music.play()
        time.sleep(pauza)
        timp += int(audio.info.length)
        print("acesta este timpul redat in enumerare:", timp)
        global n
        n += 1
        print("acesta este n= ", n)
        if (timp < 460 and n == 2):
            print("test timp mai mic n=2")
            mixer.music.load(f'Music/{j + k + 1}.mp3')
            mixer.music.play()
            time.sleep(600 - timp)
            print(i)
        elif(timp > 610 and n == 1):
            print("test timp > n = 1")
            mixer.music.load(f'Music/{j + k + 1}.mp3')
            mixer.music.play()
            time.sleep(600 - timp)


        timp = 0
        n = 0
