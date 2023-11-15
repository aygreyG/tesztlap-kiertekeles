import cv2
import pytesseract

# path to tesseract executable
# install from: https://github.com/tesseract-ocr/tesseract#installing-tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# gives back an array of tuples (image, text) where text is the text in the image
def get_regions(img_path):
    img = cv2.imread(img_path)
    # resize image
    w = 1080
    height, width, _ = img.shape
    ratio = width / height
    img = cv2.resize(img, (int(w * ratio), w))

    # convert to grayscale, blur and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 35, 30)

    # dilate to connect text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilation = cv2.dilate(thresh, kernel, iterations=5)

    # find contours
    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    img_copy = thresh.copy()

    ROI_num = 0
    regions = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 15000:
            x, y, w, h = cv2.boundingRect(contour)
            cropped = img_copy[y:y + h, x:x + w]
            cv2.imwrite('rois/ROI_{}.png'.format(ROI_num), cropped)
            ROI_num += 1
            text = pytesseract.image_to_string(cropped, lang='hun')
            if text != '':  
              regions.append((img, text))

    return regions
