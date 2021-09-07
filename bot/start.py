from time import time
from datetime import datetime
from helpers.filters import command
from helpers.decorators import sudo_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery
from config import BOT_USERNAME


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


@Client.on_message(filters.command("vstart"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"👋**Hello there, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** ",
                    reply_markup=InlineKeyboardMarkup(
    [
        InlineKeyboardButton(
            text="🧰 HOW TO USE THIS BOT 🛠 ", callback_data="cbguide"),
    ],
    [
        InlineKeyboardButton(text="🛠 Command List", callback_data="cblist"),
        InlineKeyboardButton(
            text="Repo 📦", url=f"https://youtu.be/cLRdwUskzWU"
        ),
    ],
    [
        InlineKeyboardButton(text="💬 support group", url="https://t.me/slbotzone"),
        InlineKeyboardButton(
            text="📢 Bot updates ", url="https://t.me/sl_bot_zone"
        ),
    ],
    [
        InlineKeyboardButton(text="⚡️Developer ", url="https://t.me/supunmabot"),
    ],
                    ))
   else:
      await m.reply("**I am alive now in your group ✅**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🧰 HOW TO USE THIS BOT 🛠 ", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🔎 Search Youtube", switch_inline_query='s ')
                       ],[
                          InlineKeyboardButton(
                             "🛠 Command List", callback_data="cblist")
                       ]]
                    )
      )


@Client.on_message(command(["vhelp", f"vhelp@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""🏃‍♂️**bot is running in your group ✅**\n<b>🤗**uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🧰 HOW TO USE THIS BOT 🛠 ", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🔎 Search Youtube",  switch_inline_query_current_chat="")
                       ],[
                          InlineKeyboardButton(
                             "🛠 Command List", callback_data="cblist")
                       ]]
                    )
      )


@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🤷‍♂️ bot status:\n"
        f"🙋‍♀️ `PONG!!`\n"
        f"✮✮ **Now online**`{delta_ping * 1000:.3f} ms`\n"
        f"✮✮ **Time Taken:** `{uptime}`\n"
        f"✮✮ **Service uptime:** `{START_TIME_ISO}`",
        reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🧰 HOW TO USE THIS BOT 🛠 ", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🔎 Search Youtube",  switch_inline_query_current_chat="")
                       ],[
                          InlineKeyboardButton(
                             "🛠 Command List", callback_data="cblist")
                       ]]
                    )
    )
