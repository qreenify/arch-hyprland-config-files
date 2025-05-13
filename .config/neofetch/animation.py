import os
from time import sleep

def animation(frams:str):

    FPS = 0.1 # speed of frames

    frams = frams.split("split")
    while True:
    for fr in frams :
        os.system("clear")
        print(fr)
        sleep(FPS)
