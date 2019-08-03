import cv2
import sys
import os
import os.path

def detect(filename, outname, cascade_file = "./lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    if len(faces) > 0:
        x, y, w, h = faces[0]
        print(x, y, w, h)
        cv2.imwrite(outname, image[int(y-0.1*h): int(y+0.9*h), x: x+w])

ct = 0
for y in range(2012, 2020):
     img_dir = './images/' + str(y)
     files = os.listdir(img_dir)
     for f in files:
         detect(os.path.join(img_dir, f), './cropped/{}.jpg'.format(ct))
         ct += 1
