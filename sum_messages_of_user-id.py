import os
from telethon import TelegramClient, events, sync, connection
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'
from_user_id=5339026159

total = 0
with TelegramClient('my', r_api, r_hash) as client:
    all_message = client.iter_messages(url)
    for message in all_message:
        user_id = message.from_id
        if user_id and user_id.user_id == from_user_id:
            message = message.text
            if message.isdigit():
                total += int(message)
print(total)