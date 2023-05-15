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

def main(video):
    video = cv.VideoCapture(f"library/road-video{video}.mp4")
    while video.isOpened():
        ret, frame = video.read()
        if ret == True:
            process(frame)
        else:
            exit()

if __name__ == "__main__":
    video = input("enter a number from 1 to 4:")
    main(video)
