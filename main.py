import asyncio

from random import randint

import config
import asyncpraw
from aiogram import Bot, types


API_TOKEN=config.settings['TOKEN']

channel1=config.channels['SELF_CHANNEL']
channel2=config.channels['GROUP_1_CHANNEL']

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)

reddit = asyncpraw.Reddit(client_id=config.settings['CLIENT_ID'],
                          client_secret=config.settings['SECRET_CODE'],
                          user_agent='PepegaMemBot')

memory=[]
TIMEOUT = 5
limit=1
start_number=1
end_number=4


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id,text)

async def posting():
    while True:
        await asyncio.sleep(TIMEOUT)
        subreddit_number=randint(start_number,end_number)
        if subreddit_number==1:
            SUBREDDIT_NAME = config.subreddits_names['ed']
        if subreddit_number==2:
            SUBREDDIT_NAME = config.subreddits_names['mems']
        if subreddit_number==3:
            SUBREDDIT_NAME = config.subreddits_names['cats']
        if subreddit_number==4:
            SUBREDDIT_NAME = config.subreddits_names['lol']
        messages = await reddit.subreddit(SUBREDDIT_NAME)
        messages = messages.new(limit=limit)
        item = await messages.__anext__()
        if item.title not in memory:
            memory.append(item.title)
            await send_message(channel1, item.url)
            await send_message(channel2, item.url)

loop = asyncio.get_event_loop()
loop.run_until_complete(posting())