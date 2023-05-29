import os
from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
from dotenv import load_dotenv

load_dotenv()

r_api = str(os.environ.get('TEST_API'))
r_hash = str(os.environ.get('TEST_HASH'))

url = 't.me/Parsinger_Telethon_Test'

lst = [5125814085, 5423813689, 5395359919, 5330282124, 5451738743, 5319101536,
       5599808192, 5552200609, 5560704798, 5421516684,
       5530400713, 5595171770, 5373895551, 5582701295, 5401839698, 5443556002,
       5445202221, 5394891665, 5486227453, 5342098799, 5486370067, 5576022537,
       5539803054, 5523594628, 5449816597, 5235694206, 5596049016, 5313438049,]

res = []

with TelegramClient('my', r_api, r_hash) as client:
    users = client.iter_participants('url')
    for user in users:
        user_full_about = client(GetFullUserRequest(user))
        if user_full_about.user.id in lst:
            res.append(int(user_full_about.about))
print(sum(res))