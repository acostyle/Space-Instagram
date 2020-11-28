import requests
from pathlib import Path
from additional_functions import download_an_img, get_file_extension


def fetch_spacex_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/101')
    response.raise_for_status()
    image_url = response.json()['links']['flickr_images']

    for image_number, image in enumerate(image_url):
        image_extension = get_file_extension(image)
        download_an_img(image, f'SpaceX_{image_number}{image_extension}')


if __name__ == '__main__':
    Path('images').mkdir(parents=True, exist_ok=True)
    fetch_spacex_launch()