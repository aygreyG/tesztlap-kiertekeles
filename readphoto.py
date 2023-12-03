import cv2
import pytesseract

# path to tesseract executable
# install from: https://github.com/tesseract-ocr/tesseract#installing-tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# gives back an array of (text, cropped image, coordinates) where text is the text in the image
def get_regions(img_path):
    img = cv2.imread(img_path)
    # resize image
    w = 1080
    height, width, _ = img.shape
    ratio = width / height
    img = cv2.resize(img, (int(w * ratio), w))

    # convert to grayscale, blur and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 27, 30)

    # dilate to connect text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
    dilation = cv2.dilate(thresh, kernel, iterations=3)

    # find contours
    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    img_copy = thresh.copy()

    ROI_num = 0
    regions = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cropped = img_copy[y:y + h, x:x + w]
            cv2.imwrite('rois/ROI_{}.png'.format(ROI_num), cropped)
            ROI_num += 1
            text = pytesseract.image_to_string(cropped, lang='eng', config='--psm 6')
            text = text.replace('\n', '')
            cropped_color = img[y:y + h, x:x + w]
            if text != '':
                regions.append((text, cropped_color, (x, y, w, h)))

    regions.reverse()
    return regions
