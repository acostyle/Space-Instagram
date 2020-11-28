# Space Instagram
 This is the app automatically posting photos to your instagram account from the last SpaceX launch and also from Hubble website by specified category.

### How to install

You should create two environment variables with your Instagram username and password
```
INSTAGRAM_USERNAME='your_username'
INSTAGRAM_PASSWORD='your_password'
```

You can put them into `.env` file in the same folder with `main.py`
Just run the python script main.py with the following console command:
```python
python main.py
```
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```