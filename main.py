# bot.py
from distutils import command
import os

from discord.ext import commands

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot_prefix=':hs:'
r=['reserach:']
s=['savage:']
client = discord.Client()
bot = commands.Bot(command_prefix=bot_prefix)
@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.content.lower()[0:4]==bot_prefix[0:4]:
        curmessage=message.content.lower()[4:]
        currentMessage=str(curmessage[2:]+'->'+message.author.name)
        print(currentMessage)
        if curmessage[0:2]=='r+':
            r.append(currentMessage)
            await message.channel.send('added succesfully')
            print(r.count(currentMessage))
        elif curmessage[0:2]=='s+':
            s.append(currentMessage)
            await message.channel.send('added succesfully')
        elif curmessage[0:2]=='r-':
            r.remove(currentMessage)
            await message.channel.send('removed succesfully')
        elif curmessage[0:2]=='s-':
            s.remove(currentMessage)
            await message.channel.send('removed succesfully')
        elif curmessage[0:4]=='show':
            for q in r: 
                await message.channel.send(str(q))
            for i in s:
                await message.channel.send(str(i))  
        else: await message.channel.send('something went wrong...')
client.run(TOKEN)
