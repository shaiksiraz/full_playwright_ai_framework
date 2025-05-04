import cv2

def compare_images(img1_path, img2_path, threshold=0.97):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    difference = cv2.absdiff(img1, img2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, diff = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    score = 1 - (cv2.countNonZero(diff) / diff.size)
    return score >= threshold
