***get_participants_list1.py***

    Получить список всех участников группы https://t.me/Parsinger_Telethon_Test
    Извлечь у каждого подписчика first_name и last_name.

***get_participants_list2.py***

    Получить данные участников группы https://t.me/Parsinger_Telethon_Test
    id, first_name, last_name, phone

***get_participants_photos_size.py***

    Скачать полноразмерные аватарки всех участников группы https://t.me/Parsinger_Telethon_Test
    Получить общий размер всех аватарок (в байтах).

***get_participants_all_photos_size.py***

    Скачать полноразмерные аватарки всех участников группы https://t.me/Parsinger_Telethon_Test 
	включая все сохранённые аватарки.
    Получить общий размер всех аватарок (число должно быть в байтах, в числе должны отсутствовать пробелы).

***sum_participants_about_info1.py***

    Есть список lst=[] в котором хранятся ID участников группы https://t.me/Parsinger_Telethon_Test
    Собрать числа из поля "О Себе" или "About" пользователя, если его ID имеется в списке,
	затем суммировать все добытые числа.
	
    lst = [332703068, 5914813738, 5710963988, 5799970696, 5843185336, 
	       5899028303, 5799846345, 5988909155, 5765618528, 5744269105,
		   5811870581, 5749394385, 5821321049, 5831778721, 5908359516,
		   5807015533, 5877375636, 5748959968, 5852187682, 5642780248,
		   5633717169, 5989940172]

***sum_participants_about_info2.py***

    Есть список lst=[] в котором хранятся username участников группы;
    Собрать числа из поля "О Себе" или "About" пользователя из списка lst=[], 
	затем суммировать все добытые числа.

    lst = ['Anthony_Hills', 'Craig_Moody', 'Kathleen_Browns', 'Vicki_Baileys',
	       'Jorge_Garrett', 'Larry_Summers', 'Tommy_Sullivan', 'Edward_Murrray',
		   'Nicholas_Gonzales', 'Virgina_Garcia','Denise_Barker', 'Jessie_Wright',
		   'Mary_Baileyn', 'Claytons_Riley', 'Joshuan_Chandler', 'Jameson_Powell',
		   'Harry_Valdes', 'Chriss_Yong', 'Sarah_Wilis', 'Frances_Ross', 'Joseph_Anderson']

***sum_nums_in_messages.py***

    Получить числовые значения из сообщений в группе https://t.me/Parsinger_Telethon_Test
    Суммировать полученные числа и вставить результат в поле для ответа.

***find_user-id_of_pinned_message.py***

    В группе https://t.me/Parsinger_Telethon_Test есть закреплённое сообщение.
    Получить user_id пользователя чьё сообщение закреплено.

***sum_messages_of_user-id.py***

    В группе https://t.me/Parsinger_Telethon_Test пользователь с user_id=5807015533
	оставил несколько цифровых сообщений.
    Определить участника с указанным user_id и получить его сообщения и суммировать их.

***collect_usernames_with_messages.py***

    Собрать username всех пользователей, которые отправили числовое сообщение в группу 
	https://t.me/Parsinger_Telethon_Test и создать список из этих username.

***get_group_all_photos_size.py***

    Скачать все изображения из группы https://t.me/Parsinger_Telethon_Test и определить их общий размер
    (число должно быть в байтах, в числе должны отсутствовать пробелы).