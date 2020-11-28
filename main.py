import os
import requests

from pathlib import Path
from dotenv import load_dotenv

from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_launch
from post_images import convert_image
from post_images import post_images
    

def main():
    load_dotenv()

    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')

    Path('images').mkdir(parents=True, exist_ok=True)
    Path('converted_images').mkdir(parents=True, exist_ok=True)

    fetch_spacex_launch()
    fetch_hubble_collection('printshop')

    convert_image('images')
    post_images(username, password)


if __name__ == '__main__':
    main()