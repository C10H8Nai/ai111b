from twitchAPI import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import asyncio
import chatGPT_API
import chatGPT_UI
import chatGPT_UI_support
import os

# set up KEY
dict_temp = {}
pyDir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(pyDir, "key.txt") , "r") as keyfile:
    for line in keyfile.readlines():
        line = line.strip()
        k = line.split(':')[0]
        v = line.split(':')[1]
        dict_temp[k] = v
APP_ID = dict_temp['APP_ID']
APP_SECRET = dict_temp['APP_SECRET']
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = dict_temp['TARGET_CHANNEL']


# this will be called when the event READY is triggered, which will be on bot start
async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channels')
    # join our target channel, if you want to join multiple, either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
    # you can do other bot initialization things in here
    await ready_event.chat.send_message(TARGET_CHANNEL, "BOT Ready")

# this will be called whenever a message in a channel was send by either the bot OR another user
async def on_message(msg: ChatMessage):
    print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')


# this will be called whenever someone subscribes to a channel
async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\\n'
          f'  Type: {sub.sub_plan}\\n'
          f'  Message: {sub.sub_message}')


# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('you did not tell me what to reply with')
    else:
        await cmd.reply(f'{cmd.user.name}: {cmd.parameter}')
        
async def Command_Hello(cmd: ChatCommand):
    await cmd.reply('Hello!')
    
async def Command_chatgpt(cmd: ChatCommand):
    if len(cmd.parameter) != 0:
        itemlist = cmd.parameter
        result = chatGPT_API.callGPT(itemlist)
        # print("ChatGPT回應:" , result)
        await cmd.reply(f'{cmd.user.name}，ChatGPT回應: {result}')
        chatGPT_UI_support._w1.message_user.configure(text= '使用者(' + cmd.user.name + '):' + cmd.parameter)
        chatGPT_UI_support._w1.message_gpt.configure(text="GPT回應:" + result)
    else:
        await cmd.reply('請輸入內容')


# this is where we set up the bot
async def run():
    # set up twitch api instance and add user authentication with some scopes
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)

    # register the handlers for the events you want

    # listen to when the bot is done starting up and ready to join channels
    chat.register_event(ChatEvent.READY, on_ready)
    
    # listen to chat messages
    chat.register_event(ChatEvent.MESSAGE, on_message)
    # listen to channel subscriptions
    chat.register_event(ChatEvent.SUB, on_sub)
    # there are more events, you can view them all in this documentation

    # you can directly register commands and their handlers, this will register the !reply command
    chat.register_command('reply', test_command)
    chat.register_command('Hello', Command_Hello)
    chat.register_command('chatgpt', Command_chatgpt)


    # we are done with our setup, lets start this bot up!
    chat.start()
    chatGPT_UI.start_up()

    # lets run till we press enter in the console
    try:
        input('press ENTER to stop \n')
    finally:
        # now we can close the chat bot and the twitch api client
        chat.stop()
        await twitch.close()


# lets run our setup
asyncio.run(run())