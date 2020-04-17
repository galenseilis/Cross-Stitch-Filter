from skimage import io
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import cv2
from time import ctime

if __name__ == '__main__':
    import argparse
    DESC = '''Filter that makes gives an appearance similar to cross-stitching.'''
    PARSER = argparse.ArgumentParser(description=DESC)
    PARSER.add_argument('-i', dest='IN_IMG', type=str, help='Path of input file.', required=True)
    PARSER.add_argument('-W', dest='WIDTH', type=int, help='Target width of image in inches.', default=21)
    PARSER.add_argument('-H', dest='HEIGHT', type=int, help='Target height of image in inches.', default=10)
    PARSER.add_argument('-d', dest='IS_DARK', type=bool, help='Use dark canvas (True/False).', default=True)
    PARSER.add_argument('-o', dest='OUT_IMG', type=str, help='Path of output file.', required=True)
    ARGS = PARSER.parse_args()

    # Load image
    IMG = io.imread(ARGS.IN_IMG)
    IMG = np.flipud(IMG)

    # Prepare canvas
    if ARGS.IS_DARK:
        plt.style.use('dark_background')
    FIGSIZE = (ARGS.WIDTH, ARGS.HEIGHT)
    FIGURE = plt.figure(figsize=FIGSIZE)
    AX = plt.axes([0,0,1,1], frameon=False)
    AX.get_xaxis().set_visible(False)
    AX.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)

    # Draw cross-stich pattern
    for i in range(IMG.shape[0]):
        print(f'{ctime()}: Completed {i+1} out of {IMG.shape[0]} rows... {round((i+1) / IMG.shape[0] * 100, 2)}%.')
        for j in range(IMG.shape[1]):
            plt.plot([j-0.5, j+0.5], [i-0.5, i+0.5], c=IMG[i][j] / 255)
            plt.plot([j-0.5, j+0.5], [i+0.5, i-0.5], c=IMG[i][j] / 255)

    plt.savefig(ARGS.OUT_IMG)
    plt.close()
