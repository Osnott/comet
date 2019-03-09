import cv2
import sys
import pytesseract

if __name__ == '__main__':

  if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)

  # Read image path from command line
  imPath = sys.argv[1]

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

  # Print recognized text
  print(text)
