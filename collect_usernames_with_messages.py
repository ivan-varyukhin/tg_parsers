import os
from telethon import TelegramClient, events, sync, connection
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'

users = []
with TelegramClient('my', r_api, r_hash) as client:
    all_message = client.iter_messages(url)
    for message in all_message:
        user_id = message.from_id
        if user_id and message.text.isdigit():
            user_names = client.get_entity(user_id).username
            if user_names not in users:
                users.append(user_names)
            
print(users)