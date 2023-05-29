import os
from telethon import TelegramClient, events, sync, connection
from telethon.tl.types import InputMessagesFilterPhotos
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'

total_size = 0
with TelegramClient('my', r_api, r_hash) as client:
    all_message = client.iter_messages(url, filter=InputMessagesFilterPhotos)
    for message in all_message:
        media = client.download_media(message, file='img/')
        stats = os.stat(media)
        total_size += stats.st_size

print(total_size)