#!/usr/bin/python
import numpy as np
import cv2 as cv
import sys
import getopt


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "x:y:w:h:f:", ['help'])
    except getopt.GetoptError:
        print('color.py -x <x> -y <y> -w <w> -h <h> -f <frame_id>')
        sys.exit(2)

    x = y = w = h = frame_id = None

    for opt, arg in opts:
        if opt == '--help':
            print('Syntax: color.py -x <x> -y <y> -w <w> -h <h> -f <frame_id>')
            sys.exit()
        elif opt == "-x":
            x = int(arg)
        elif opt == "-y":
            y = int(arg)
        elif opt == "-w":
            w = int(arg)
        elif opt == "-h":
            h = int(arg)
        elif opt == "-f":
            frame_id = int(arg)
    if x is None or y is None or w is None or h is None or frame_id is None:
        sys.exit()

    x = int(x - (w / 2))
    y = int(y - (h / 2))

    image = cv.imread("../darknet/saved_frames/image_%08d.jpg" % frame_id)
    crop = image[y:y+h, x:x+w]
    pixels = np.float32(crop.reshape(-1, 3))
    n_colors = 4
    criteria = (cv.TERM_CRITERIA_EPS + cv.KMEANS_PP_CENTERS, 200, .1)
    flags = cv.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]
    print('#%02x%02x%02x' %
          (int(dominant[2]), int(dominant[1]), int(dominant[0])))


if __name__ == "__main__":
   main(sys.argv[1:])
