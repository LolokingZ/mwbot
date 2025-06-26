import cv2
import pytesseract

def extract_numbers_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]

    # OCR config
    config = '--psm 6 -c tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(thresh, config=config)

    # Filter angka valid
    numbers = [int(x) for x in text.split() if x.isdigit()]
    return numbers
