import numpy as np 
import cv2 as cv

class Extractor():
    def __init__(self):
        self.orb = cv.ORB_create()
        self.last = None
        self.brute_force = cv.BFMatcher(cv.NORM_HAMMING,crossCheck=True)


    def extractor(self, frame):
        # kp, des = self.orb.detectAndCompute(frame,None)
        # frame = cv.drawKeypoints(frame, kp, des, color=(0,250,0), flags=0)
        corners = cv.goodFeaturesToTrack(frame,3000,0.01,3) 
        kp = [cv.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in corners]
        kp, des = self.orb.compute(frame, kp)
        # color = cv.drawKeypoints(frame, kp, des, color=(0,255,0), flags=0)
        matches = None
        if self.last is not None:
            matches = self.brute_force.match(des, self.last['des'])
            matches = zip([kp[m.queryIdx] for m in matches], [self.last['kp'][m.trainIdx] for m in matches])
            for pt1, pt2 in matches:
                u1, v1  = map(lambda x: int(round(x)), pt1.pt)
                u2, v2  = map(lambda x: int(round(x)), pt2.pt)
                cv.circle(frame, (u1, v1), color=(0,255,0), radius=2)
                cv.line(frame, (u1, v1),(u2,v2), color=(0,255,0))
        self.last = {'kp': kp, 'des': des}
        return matches
                

