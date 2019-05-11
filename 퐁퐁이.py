import discord
import requests
import asyncio
import os
from json import loads

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("괴롭힘 당함")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = ["yeoneochobap"]
    name = ["연이연어"]
    channel = client.get_channel(525342388181401610)
    a = 0
    while True:
        for i in range(0, len(twitch)):
            headers = {'Client-ID': 'vkaxfu7isfa6oobkyz9jrjal5de3pp'}
            response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch[i], headers=headers)
            try:
                if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                    await channel.send(name[0] + "님이 노략질을 위해 방송을 시작하셧습니다! [ https://www.twitch.tv/yeoneochobap ]")
                    a = 1
            except:
                a = 0
        await asyncio.sleep(5)
@client.event
async def on_message(message):
    if message.content.startswith('퐁하'):
        await message.channel.send("하이하이!")
    if message.content.startswith("퐁바"):
        await message.channel.send("바이바이!")

    if message.content.startswith('방송켜라'):
        await message.channel.send("지금 연님이 똥싸고있어서 다싸면 켜주신데요:/ ")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
