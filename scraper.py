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
from google.genai.types import Tool, GenerateContentConfig
import serpapi



def scrape():


    location = input("Enter location \n")
    client = serpapi.Client(api_key="a7441ad03a2e7d64d66d2e5521ae2658315e4c20ad70e22994ef062437618daf")

    

    results = client.search({
        "engine": "google_maps",
        "q": "pasta",
        "ll": "@-33.8688,151.2093,14z",
        "type": "search"
    })

    local_results = results["local_results"]


    # response = requests.get(url)

    # menuTag = soup.find('img')
    # menuSrc = menuTag.get('src',None)
    # print(menuTag)
    # print(menuSrc)
    # print(url)
    # tools = [
    #     {"url.context": {}},
    # ]

    websiteList = []
    for e in local_results:
        if "website" in e:
            websiteList.append(e["website"])

    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Give me a list of all pastas and their prices from this list of urls {websiteList}",
        # config=GenerateContentConfig(
        #     tools=tools
        # )
    )

    print(response)


if __name__ == '__main__':
    scrape()
    # print(__name__)
    

