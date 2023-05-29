import os
from telethon import TelegramClient, events, sync, connection
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'

client = TelegramClient('session_name2', r_api, r_hash)
client.start()
participants = client.get_participants(url)

res = []
for item in participants:
    res.append(f'{item.first_name} {item.last_name}')
print(res)