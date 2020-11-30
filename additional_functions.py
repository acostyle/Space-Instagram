import argparse
import os
import requests

from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser(description='Download SpaceX and Hubble photos into your folder')

    parser.add_argument('-si', '--spacex_id', help='Choose launch id and download photos from SpaceX API', type=int)
    parser.add_argument('-hi', '--hubble_id', help='Choose id and download photos from Hubble API', type=int)
    parser.add_argument('-hc', '--hubble_collection', help='Change Hubble Collection and download photos from Hubble API', type=str)
    parser.add_argument('-i', '--instagram', action='store_true', help='Post downloaded photos to Instagram')

    return parser


def download_an_img(url, filename):
    download_path = os.getenv('DOWNLOAD_PATH')

    Path(download_path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(Path.cwd().joinpath(download_path).joinpath(f'{filename}'), 'wb') as image:
       image.write(response.content)