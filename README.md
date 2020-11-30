# Space Instagram
 This is the app automatically posting photos to your instagram account from the last SpaceX launch and also from Hubble website by specified category.

### How to install

You should create four environment variables with your instagram username, instagram password, download path and converted images path
```
INSTAGRAM_USERNAME='your_username'
INSTAGRAM_PASSWORD='your_password'
DOWNLOAD_PATH='your_download_path'
CONVERT_PATH='your_converted_images_path'
```

You can put them into `.env` file in the same folder with `main.py`

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to run a script

For help, type `python main.py -h` or `python main.py --help`

__If you want to download pictures from SpaceX launch, you should to choose launch ID (from on 0 to 110 on 30.11.20):__
`python main.py -si SPACEX_ID` or `python main.py --spacex_id SPACEX_ID`

__If you want to download pictures from Hubble:__
- To download by ID: `python main.py -hi HUBBLE_ID` or `python main.py --hubble_id HUBBLE_ID`
- To download by collection: `python main.py -hc HUBBLE_COLLECTION` or `python main.py --hubble_collection HUBBLE_COLLECTION`

__If you want to post photos on your Instagram:__
`python main.py -i` or `python main.py --instagram`
