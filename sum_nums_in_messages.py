import os
from telethon import TelegramClient, events, sync, connection
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'

res = []
with TelegramClient('my', r_api, r_hash) as client:
    all_message = client.iter_messages(url)
    for message in all_message:
        if message.message:
            res.append(int(message.message))
print(sum(res))