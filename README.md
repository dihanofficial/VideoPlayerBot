<h1> Telegram Video Player Bot 🎶 </h1>

 Telegram bot project for streaming video on telegram video chat, powered by [pytgcalls](https://github.com/pytgcalls/pytgcalls) and [pyrogram](https://github.com/pyrogram/pyrogram)

##  Deploy to Heroku  👨‍🔧
The easy way to host this bot

<a href="https://heroku.com/deploy?template=https://github.com/dihanofficial/VideoPlayerBot"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a>

❓ --**Setting Up**-- :
- 1.) first, add me to your group.
- 2.) then promote me as admin and give all permissions except anonymous admin.
- 3.) add @dihanofficialvcplayerbot to your group.
- 4.) turn on the voice chat first before start to stream video.
- 5.) type /vplay (reply to video) to start streaming.
- 6.) type /stop to end the video streaming.


## VPS Deployment
```
- sudo apt update && ugrade -y
- sudo apt install python3-pip -y virtualenv
- sudo apt install ffmpeg -y
- git clone https://github.com/dihanofficial/VideoPlayerBot  #Clone your repo.
- cd video-stream
- virtualenv env #Create Virtual Environment.
- source env/bin/activate #Activate Virtual Environment
- curl -sL https://deb.nodesource.com/setup_16.x | sudo bash - #update node to latest version
- sudo apt-get install -y nodejs
- pip3 install --upgrade pip
- pip3 install -U -r requirements.txt
- sudo nano config.py #Fill it with your variables value.
- python3 -m bot
```

# Credits ⚔ 

- [Laky-64](https://github.com/Laky-64) for [pytgcalls](https://github.com/pytgcalls/pytgcalls)
- [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
