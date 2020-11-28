from pathlib import Path
from instabot import Bot
from PIL import Image
from dotenv import load_dotenv
import os


def convert_image(image_files):
    images_path = Path(image_files)

    for image in images_path.iterdir():
        image_file = Image.open(image)
        image_file.thumbnail((1080, 1080))

        rgb_image_file = image_file.convert('RGB')

        rgb_image_file_name = Path(image).stem
        rgb_image_file.save(Path.cwd().joinpath('converted_images').joinpath(f"{rgb_image_file_name}.jpg"), format='JPEG')


def post_images(username, password):
    bot = Bot()
    bot.login(username=username, password=password)

    converted_images = Path.cwd().joinpath('converted_images')

    for image in converted_images.iterdir():
        pic_name = image.stem
        print(f'Uploading: {pic_name}')

        bot.upload_photo(image, caption=pic_name)


if __name__ == '__main__':
    Path('converted_images').mkdir(parents=True, exist_ok=True)