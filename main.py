# bot.py
from distutils import command
import os
from webserver import keep_alive


from discord.ext import commands

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot_prefix=':hs:'
r=['reserach:']
rpath='r.txt'
spath='s.txt'
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
            work=open(rpath,'a')
            work.write('\n')
            work.write(currentMessage)
            work.close()
            await message.channel.send('added succesfully')
            print(r.count(currentMessage))
        elif curmessage[0:2]=='s+':
            s.append(currentMessage)
            work=open(spath,'a')
            work.write('\n')
            work.write(currentMessage)
            work.close()
            await message.channel.send('added succesfully')
        elif curmessage[0:2]=='r-':
            r.remove(currentMessage)
            work=open(rpath,'r')
            work1=open('new.txt','w')
            for line in work:
                if line !=currentMessage:
                    work1.write(line)
                    print(line+'12')
                    print(currentMessage+'12')
            work.close()
            work1.close()
            work=open(rpath,'w')
            work1=open('new.txt','r')
            for line in work1:
                work.write(line)
            work.close()
            work1.close()
            await message.channel.send('removed succesfully')
        elif curmessage[0:2]=='s-':
            s.remove(currentMessage)
            work=open(spath,'r')
            work1=open('new.txt','w')
            for line in work:
                if line !=(currentMessage):
                    work1.write(line)
                    print(line+'11')
                    print(currentMessage+'11')
            work.close()
            work1.close()
            work=open(spath,'w')
            work1=open('new1.txt','r')
            for line in work1:
                work.write(line)
            work.close()
            work1.close()
            await message.channel.send('removed succesfully')
        elif curmessage[0:4]=='show':
            work=open('r.txt','r')
            for line in work: 
                await message.channel.send(line)
            work.close()
            work=open('s.txt','r')
            for line in work: 
                await message.channel.send(line)
            work.close()
        else: await message.channel.send('something went wrong...')

keep_alive()
client.run(TOKEN)
