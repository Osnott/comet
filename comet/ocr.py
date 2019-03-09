import cv2
import pytesseract

def recognize():
    # Read image path from command line
    imPath = "test/test-images/WordSearchPuzzle.jpg"

    # Uncomment the line below to provide path to tesseract manually
    # pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR'

    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    #  --psm 6
    config = ('-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --oem 1')

    # Read image from disk
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(
        im, config='-l eng --oem 0 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return text