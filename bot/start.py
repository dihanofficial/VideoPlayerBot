
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import Sophia
from helpers.decorators import sudo_users_only
from helpers.filters import command

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


@Client.on_message(command(["start", f"start@{Sophia.BOT_USERNAME}"]))
async def start(_, m: Message):
    if m.chat.type == "private":
        await m.reply_text(
            f"✨ **Hello there, I am a telegram group video streaming bot.**\n\n💭 **I was created to stream videos in group "
            f"video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/{Sophia.BOT_USERNAME}?startgroup=true")
                ], [
                    InlineKeyboardButton(
                        "Source Code 💾", url=f"https://github.com/dihanofficial/videoplayerbot")
                ], [
                    InlineKeyboardButton(
                        "Follow Me ", url=f"https://github.com/dihanofficial/")
                ], [
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/SophiaSupport_Official"),
                    InlineKeyboardButton(
                        "📣 Updates Channel", url="https://t.me/SophiaUpdates")
                ], [
                    InlineKeyboardButton(
                        "👩 Developer", url="https://t.me/dihanofficial")
                ], [
                    InlineKeyboardButton(
                        "📚 All Command List", callback_data="cblist")
                ]]
            ))
    else:
        await m.reply_text("**Video Player Bot is Online now ✨**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton(
                                       "Support Group", url="https://t.me/SophiaSupport_Official")
                               ], [
                                   InlineKeyboardButton(
                                       "Updates Channel", url="https://t.me/SophiaUpdates")
                               ], [
                                   InlineKeyboardButton(
                                       "🌐 Search Youtube", switch_inline_query='')
                               ]]
                           )
                           )
