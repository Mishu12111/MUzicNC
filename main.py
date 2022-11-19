import os
from playsound import playsound
import time
from pygame import mixer
import enumerare
from enumerare import algoritm
from mutagen.mp3 import MP3
timp = 0
k = 0
ora = 45
pauza = 10
j = 0
mixer.init()
# folder path
print(enumerare.count , "fisiere")
run = True
i = 1
k = 0
for i in range(enumerare.count):
    while i:
            time.sleep(1) # se verifica valorile la fiecare 6 secunde
            now = time.gmtime()
            print("acesta este i: ",i)
            print("acesta este timpul redat in afara functiei else:", timp)
            if (now[3]  == 6+i):
                if((now[3]==10) or (now[3]==15)):
                    if (now[4] == 45):
                        algoritm(j,k,i,timp)
                if (now[4] == 50):
                    algoritm(j,k,i,timp)
                    print("acesta este timpul redat in functia else:", timp)
                    i = 0
                    k += 2
