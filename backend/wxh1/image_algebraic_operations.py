import cv2
import matplotlib.pyplot as plt
def image_algebraic_operations_add(image1,image2,a=0.5,b=0.5):
    res = cv2.addWeighted(image1, a, image2, b, 0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
def image_algebraic_operations_cut(image1,image2):
    res = cv2.subtract(image1,image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
def image_algebraic_operations_multiply(image1,image2):
    res = cv2.multiply(image1,image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res
def image_algebraic_operations_division(image1,image2):
    res = cv2.divide(image1,image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return res