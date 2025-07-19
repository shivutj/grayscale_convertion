
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def format_coord(x, y, img):
    x, y = int(x), int(y)
    if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
        r, g, b = img[y, x]
        return f"x={x}, y={y}, R={r}, G={g}, B={b}"
    else:
        return ""

def run_matplotlib_hover(image_path):
    img = np.array(Image.open(image_path))
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.format_coord = lambda x, y: format_coord(x, y, img)
    plt.title("Hover to view pixel values")
    plt.show()
