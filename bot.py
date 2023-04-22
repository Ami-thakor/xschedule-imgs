import requests
import os
import time
from pyrogram import Client, filters

# Initialize your Pyrogram client
BOT_TOKEN = os.environ.get('BOT_TOKEN',
                           '5696074673:AAFSjLPwlYT6usWNs4e5XGFqe94PSq9PK98')

plugins = dict(root="plugins")
API_ID = 16514976
API_HASH = '40bd8634b3836468bb2fb7eafe39d81a'

CHAT_ID = int(os.environ.get('CHAT_ID',
                             '-1002'))

client = Client("my_bot", api_id=API_ID,
                api_hash=API_HASH, bot_token=BOT_TOKEN)

directory_path = 'imgs'
if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
def download_image(url, file_name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return file_name
    except requests.exceptions.HTTPError as e:
        return None
    except:
        return None


with open('images.txt', 'r') as file:
    photos = file.readlines()

# Define a handler for the /send command
@client.on_message(filters.private & filters.command("start"))
def start_command_handler(_, message):
   return message.reply_text("Already Started")
  
      
    
    
run = 0


# Define a handler for the /send command
@client.on_message(filters.private & filters.command("send"))
def send_command_handler(_, message):
    global run
    if run != 0:
        return message.reply_text("Already Started")
    count = 1
    run = 1
    for i in photos:

        file = f'imgs/{count}.jpg'
        
        res = download_image(i, file)
        photos.remove(i)
    
        if res:
            try:
                client.send_photo(CHAT_ID, res, disable_notification=True)
                time.sleep(3000)
            except:
                pass


client.run()
