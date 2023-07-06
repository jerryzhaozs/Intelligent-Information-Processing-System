import cv2
import numpy
import numpy as np
from PIL import Image


def and_operator(img1, img2):
    res= cv2.bitwise_and(img1, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
def or_operator(img1, img2):
    res= cv2.bitwise_or(img1, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
def not_operator(img):
    res= cv2.bitwise_not(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
def xor_operator(img1, img2):
    res= cv2.bitwise_xor(img1, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
