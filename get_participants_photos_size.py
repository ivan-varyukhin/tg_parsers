import os
from telethon import TelegramClient, events, sync, connection
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'

with TelegramClient('my', r_api, r_hash) as client:
    participants = client.get_participants(url)
    size = 0
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f'img/{i}')
        size += os.path.getsize(f'{i}.jpg')
print(size)