
import cv2

def show_pixel_value(event, x, y, flags, param):
    img = param
    if event == cv2.EVENT_MOUSEMOVE:
        if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
            pixel = img[y, x]
            print(f"Position: ({x}, {y}), BGR: {pixel}")

def run_opencv_hover(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("Image not found or invalid path.")
    cv2.imshow('Image Viewer', img)
    cv2.setMouseCallback('Image Viewer', show_pixel_value, param=img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
