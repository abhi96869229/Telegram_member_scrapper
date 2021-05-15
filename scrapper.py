import os
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync
from telethon.sessions import StringSession
from telethon import functions,types
from telethon.sync import TelegramClient
from telethon import functions, types

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
owner = os.environ.get("USER_ID")
owner = int(owner)
string_session = os.environ.get("STRING_SESSION")
chan = os.environ.get("GROUP1")
chann = os.environ.get("GROUP2")
client = TelegramClient(StringSession(string_session), api_id, api_hash)
client.start()
usersscraped = list()

for user in client.iter_participants(chan):
    try:
        userinfo = client(functions.users.GetFullUserRequest(
            id=user.username
        ))
        try:
            
            result = client(functions.contacts.AddContactRequest(
                id=user.username,
                first_name=userinfo.user.first_name,
                last_name=userinfo.user.last_name,
                phone = "+91 ",
                add_phone_privacy_exception=False
            ))
            try:
                scrap = client(functions.channels.InviteToChannelRequest(
                    channel=chann,
                    users=[user.username]
                ))
                usersscraped.append(user.username)
                print("useradded")
            except:
                 pass
        except:
            pass
    except:
        pass
    

