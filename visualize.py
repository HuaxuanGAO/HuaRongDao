import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
import cv2
import glob

norm = matplotlib.colors.Normalize(0,10)
colors = [[norm(0), "white"],
        [norm(1), "red"],
        [norm(2), "orange"],
        [norm(3), "yellow"],
        [norm(4), "green"],
        [norm(5), "blue"],
        [norm(6), "cyan"],
        [norm(7), "purple"],
        [norm(8), "gray"],
        [norm(9), "pink"],
        [norm(10), "black"],]

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

def to_image(trace, path):
    for i, board in enumerate(trace):
        print(i)
        plt.matshow(board.to_int(), cmap=cmap)
        plt.title("Step: " + str(i))
        plt.savefig(path + "/" + str(i))
        plt.close()

def name(filaname):
    index = filaname.split("/")[-1].split(".")[0]
    return int(index)

def to_video(in_path, out_path):
    files = glob.glob(in_path + '*.png')
    files.sort(key=name)

    img_array = []
    for filename in files:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'DIVX'), 3, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()