import requests
import os
from pathlib import Path
from additional_functions import download_an_img


def fetch_hubble_pics(image_id):
    response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}')
    response.raise_for_status()
    
    image_files = response.json()['image_files'][-1]['file_url']
    image_url = f'https:{image_files}'
    
    image_extension = os.path.splitext(image_url)
    download_an_img(image_url, f'Hubble_{image_id}{image_extension[1]}')


def fetch_hubble_collection(collection_name):
    response = requests.get(f'http://hubblesite.org/api/v3/images/{collection_name}')
    response.raise_for_status()
    images = response.json()

    for image in images:
        fetch_hubble_pics(image['id'])