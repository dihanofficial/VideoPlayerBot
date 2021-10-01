import os
from config import Sophia

class Messages():
      START_MSG = """
**Hello 👋 [{}](tg://user?id={})!**
I am a telegram Group & Channel Video Streaming bot.
✅ Send me /help for more info.
"""
      
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to Sophia Video Player v2.0
⚪️ Sophia can play videos in your group's voice chat as well as channel voice chats
⚪️ Assistant name >> @{Sophia.ASSISTANT_NAME}
Click next for instructions**
""",

f"""
**Setting up**
1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /vplay [Reply to video Or Youtube link] for the first time by an admin
*) If userbot joined enjoy Video, If not add @{Sophia.ASSISTANT_NAME} to your group and retry
**For Channel Video Play**
1) Make me admin of your channel 
2) Send /vjoin in linked group
3) Now send commands in linked group
**Commands**
**=>> Video Playing 🎧**
- /vplay [Youtube link] : Play the given yt url
- /vplay [reply to video]: Play replied video
- /vstop  Stop player
""",
        
f"""
**=>> Channel Video Play 🛠**
⚪️ For linked group admins only:
- /cplay [yt link] - Play the given yt url
- /cstop - stop video play
- /vjoin - invite assistant to your chat
channel is also can be used instead of cplay
⚪️ If you donlt like to play in linked group:
1) Get your channel ID.
2) Create a group with tittle: Channel video: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{Sophia.ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> Commands for Sudo Users ⚔️**
 - /leaveall - remove assistant from all chats
 -/vleave - leave assistant from chat
*Sudo Users can execute any command in any groups
"""
      ]
