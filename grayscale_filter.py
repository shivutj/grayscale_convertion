
import numpy as np
from PIL import Image

def rgb_to_grayscale(rgb_img):
    assert len(rgb_img.shape) == 3 and rgb_img.shape[2] == 3, "Invalid RGB image format"
    grayscale = (
        0.299 * rgb_img[:, :, 0] +
        0.587 * rgb_img[:, :, 1] +
        0.114 * rgb_img[:, :, 2]
    ).astype(np.uint8)
    return grayscale

def apply_filter(gray_img, kernel):
    assert gray_img.ndim == 2, "Input must be a 2D grayscale image"
    assert kernel.shape == (3, 3), "Kernel must be 3x3"

    padded = np.pad(gray_img, pad_width=1, mode='constant', constant_values=0)
    result = np.zeros_like(gray_img)

    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            region = padded[i:i+3, j:j+3]
            filtered_value = np.sum(region * kernel)
            result[i, j] = np.clip(filtered_value, 0, 255)

    return result
