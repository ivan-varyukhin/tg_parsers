import os
from telethon import TelegramClient, events, sync, connection
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

size = 0

url = 't.me/Parsinger_Telethon_Test'

with TelegramClient('my', r_api, r_hash) as client:
    all_user_group = client.get_participants(url)
    for i, user in enumerate(all_user_group):
        for iter_photo in client.iter_profile_photos(user):
            client.download_media(iter_photo, file='img/{i}')
            size += os.path.getsize(f'img/{i}.jpg')
print(size)