import requests
import os
from pathlib import Path
from additional_functions import download_an_img


def fetch_spacex_launch(id):
    response = requests.get(f'https://api.spacexdata.com/v3/launches/{id}')
    response.raise_for_status()
    image_url = response.json()['links']['flickr_images']

    for image_number, image in enumerate(image_url):
        image_extension = os.path.splitext(image)
        download_an_img(image, f'SpaceX_{image_number}{image_extension[1]}')