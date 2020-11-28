import requests
from pathlib import Path
from additional_functions import download_an_img, get_file_extension


def fetch_hubble_pics(image_id):
    response = requests.get(f'http://hubblesite.org/api/v3/image/{image_id}')
    response.raise_for_status()

    image_files = response.json()['image_files']
    image_url = image_files[-1]['file_url']

    return f'https:{image_url}'


def fetch_hubble_collection(collection_name):
    response = requests.get(f'http://hubblesite.org/api/v3/images/{collection_name}')
    response.raise_for_status()
    images = response.json()

    for image_number, image in enumerate(images):

        image_url = fetch_hubble_pics(image['id'])
        image_extension = get_file_extension(image_url)

        download_an_img(image_url, f'Hubble_{image_number}{image_extension}')


if __name__ == '__main__':
    Path('images').mkdir(parents=True, exist_ok=True)
    fetch_hubble_collection('starships')