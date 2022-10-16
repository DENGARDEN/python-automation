import pytesseract
from pdf2image import convert_from_path
import cv2
import matplotlib.pyplot as plt

from pathlib import Path
import os


PATH = "/home/dengarden/Documents/temp/bigdata/"

pdfs = os.listdir(PATH)
pdfs = sorted(list(map(lambda x: PATH + x, pdfs)))

pdfs = [pdf for pdf in pdfs if os.path.isfile(pdf) and pdf.endswith(".pdf")]
print(pdfs)

for pdf in pdfs:
    name = Path(pdf).stem
    pages = convert_from_path(pdf, 350)

    images = []
    i = 1
    for page in pages:
        image_name = f"{name}_" + "Page_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")

        images.append(image_name)
        i = i + 1

    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Akash.Chauhan1\AppData\Local\Tesseract-OCR\tesseract.exe'

    # load the original image
    # image = cv2.imread(images[0])

    # # get co-ordinates to crop the image
    # # c = line_items_coordinates[1]

    # # cropping image img = image[y0:y1, x0:x1]
    # img = image
    # # img = image[c[0][1]:c[1][1], c[0][0]:c[1][0]]

    # plt.figure(figsize=(10,10))
    # plt.imshow(img)

    # # convert the image to black and white for better OCR
    # ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

    # # pytesseract image to string to get results
    # text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))

    full_text = ""
    for image in images:
        full_text += pytesseract.image_to_string(image, config="--psm 6")
        print(full_text)

    with open(f"./result/{name}.txt", "w") as f:
        f.write(full_text)

    while len(images) > 0:
        os.remove(images.pop())
