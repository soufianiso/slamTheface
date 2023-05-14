import cv2 as cv 
from display import Display 
import pygame
import numpy as np
from extractor import Extractor
# receiving the input from the user 

W = 1920//2 
H = 1080//2
disp   = Display(W,H)
ext = Extractor()

def process(frame:object) -> object:
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    frame = cv.resize(gray,(W,H))
    matches = ext.extractor(frame)
    if matches is not None: 
        disp.draw(frame)

if __name__ == "__main__":
    input = input("enter the number video here: ")
    video = cv.VideoCapture(f"library/road-video{input}.mp4")
    while video.isOpened():
        ret, frame = video.read()
        if ret == True:
            process(frame)
        else:
            exit()

