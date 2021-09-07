from time import time
from datetime import datetime
from helpers.filters import command
from helpers.decorators import sudo_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


##### edited by dihanofficial

from config import ASSISTANT_NAME, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❓ Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton("💾 Source Code", url=f"https://github.com/dihanofficial/VideoPlayerBot"),
                 InlineKeyboardButton("👨‍🔧About Me", callback_data="about"),
            ],
            [
                InlineKeyboardButton("🙋‍♂️ Updates Channel", url=f"https://t.me/dihanofficial"),
                InlineKeyboardButton("🙋‍♀️ Support Group", url=f"https://t.me/dihan_official"),
            ],
            [
               InlineKeyboardButton("➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply(f"**@{ASSISTANT_NAME} is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Back", callback_data="start"),
                InlineKeyboardButton ("🙋‍♀️ Support Group", url=f"https://t.me/dihan_official"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("Back", callback_data="start"),
                InlineKeyboardButton ("🙋‍♀️ Support Group", url=f"https://t.me/dihan_official"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    
    elif query.data=="start":
        buttons = [
           [
                InlineKeyboardButton("❓ Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton("💾 Source Code", url=f"https://github.com/dihanofficial/VideoPlayerBot"),
                 InlineKeyboardButton("👨‍🔧About Me", callback_data="about"),
            ],
            [
                InlineKeyboardButton("🙋‍♂️ Updates Channel", url=f"https://t.me/dihanofficial"),
                InlineKeyboardButton("🙋‍♀️ Support Group", url=f"https://t.me/dihan_official"),
            ],
            [
               InlineKeyboardButton("➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
