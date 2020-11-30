import argparse
import os
import requests

from instabot import Bot
from pathlib import Path
from dotenv import load_dotenv

from additional_functions import create_parser
from fetch_hubble import fetch_hubble_pics
from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_launch
from post_images import convert_image
from post_images import post_images


def main():
    load_dotenv()

    parser = create_parser()

    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    
    args = parser.parse_args()
    
    if args.spacex_id:
        fetch_spacex_launch(args.spacex_id)

    if args.hubble_id:
        fetch_hubble_pics(args.hubble_id)
    
    if args.hubble_collection:
        fetch_hubble_collection(args.hubble_collection)

    if args.instagram:
        convert_image()
        post_images(username, password)

    else:
        print('Error: Please, input at least 1 argument')


if __name__ == '__main__':
    main()