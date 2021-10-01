

import logging
import time
import sys
import asyncio
import glob
import importlib
from pathlib import Path
from pyrogram import Client, idle
from config import Sophia
from bot.videoplayer import app
from bot.videoplayer import call_py
from helpers.loggings import LOG
 
    
bot = Client(
    ":memory:",
    Sophia.API_ID,
    Sophia.API_HASH,
    bot_token=Sophia.BOT_TOKEN,
    plugins=dict(root="bot"),
)

StartTime = time.time()

loop = asyncio.get_event_loop()

_path = f"bot/*.py"
files = glob.glob(_path)

def load_plugins(plugin_name):
    path = Path(f"bot/{plugin_name}.py")
    name = "bot.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(load)
    sys.modules[f"bot." + plugin_name] = load
    print("Imported => " + plugin_name)

async def start():
    print('\n')
    print('------------------ Initalizing SOPHIA --------------------')
    if bot:
        await bot.start()
    await app.start()
    await call_py.start()
    print('------------------------ DONE --------------------------')
    print('------------------ Importing Modules -------------------')
    for name in files:
        with open(name) as a:
            path_ = Path(a.name)
            plugin_name = path_.stem
            load_plugins(plugin_name.replace(".py", ""))
    print('------------------- INITIATED SOPHIA ---------------------')
    print('     Logged in as User =>> {}'.format((await app.get_me()).first_name))
    if bot:
        print('     Logged in to Bots =>> {}'.format((await bot.get_me()).first_name))
    print('--------------------------------------------------------')
    await idle()
if __name__ == '__main__':
    is_bot = bool(Sophia.BOT_TOKEN)
    loop.run_until_complete(start())



