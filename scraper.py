import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import cv2
import pytesseract
# from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from google import genai
from google.genai import types



def scrape():

    url = 'https://www.macchiato.com.au/pages/view-menus'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # menuTag = soup.find('img')
    # menuSrc = menuTag.get('src',None)
    menuSrc = '//www.macchiato.com.au/cdn/shop/files/Breakfast_Menu.png?v=1772054800&width=2400'
    # print(menuTag)
    # print(menuSrc)
    # print(url)

    if menuSrc:
        bong = requests.compat.urljoin(url,menuSrc)
        print(f"Opening image from: {bong}")

        menuBong = requests.get(bong)
        image = Image.open(BytesIO(menuBong.content))
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=["Give me a list of all pastas and their prices",image]
        )
        # extractedText = pytesseract.image_to_string(image)
        # print(extractedText)
        # print(response)

        # image.show()
    else:
        print('BONG')

if __name__ == '__main__':
    scrape()
    # print(__name__)
    

