import json
import discord
privileged_names=['Leoric-pl','Brathoss','Kubaaa','PenZel','Myszak', 'Sawyer','micmen']

class User():
      name=""
      score=0
      flights=0
      def __init__(self,new_name):
        self.name=new_name
      def in_flight(self,points):
        self.score+=points
        self.flights+=1
class Stats():
    rs_score=[0,0,0,0,0,0,0,0,0,0,0]
    users=[]
    rs_company=[[],[],[],[],[],[],[],[],[],[],[]]

async def show_rs_stats(message):
  res="rs stats:\n"
  for i in range(Stats.rs_score.__len__()):
    res=res+str(i+1)+' '+str(Stats.rs_score[i])+'\n'
  await message.channel.send(res)
async def show_user_stats(message):
  res='user stats:'
  for i in Stats.users:  
    tab=[str(i.name),str(i.score),str(i.flights)]
    res+=' '.join(tab)+'\n'
  await message.channel.send(res)

async def show_all_stats(message):
  await show_user_stats(message)
  await show_rs_stats(message)
async def is_user(username):
  for i in Stats.users:
    if i.name==username:return True
  Stats.users.append(User(username))
  return True

async def flight(rslevel,points,usernames):
  usernum=usernames.__len__()
  Stats.rs_score[rslevel-1]+=points
  for i in usernames:
    await is_user(i)
  for k in usernames:
    for i in Stats.users:
      if i.name==k:i.in_flight(points/usernum)
async def reset_stats():
  for i in range(Stats.rs_score.__len__()):
    Stats.rs_score[i]=0
    Stats.users.clear()

async def count_stats():
  file=open('stats.txt', "r")
  for line in file:
    part2=line.split()
    rs=int(part2[0])
    score=int(part2[1])
    part2=part2[2:]
    await flight(rs,score,part2)
    
async def decide(message):
  if message.content.lower()[0:5]=='rs_e+' and message.author.name in privileged_names:
    toW=message.content.lower()[5:]
    work=open('stats.txt','a')
    work.write('\n')
    work.write(toW)
    work.close()
    await reset_stats()
    await count_stats()
    await show_all_stats(message)
  elif message.content.lower()[0:6]=='rs_e_s':
    await reset_stats()
    await count_stats()
    await show_all_stats(message)
  elif message.content.lower()[0:6]=='rs_e_c' and message.author.name in privileged_names:
    open('stats.txt', 'w').close()
    await reset_stats()
    await message.channel.send('all stats have been cleared')
  elif message.content.lower()[0:3]=='rs+':
    part2=message.content.lower()[3:].split()
    rs=int(part2[0])-1
    Stats.rs_company[rs].append(message.author.mention)
    await message.channel.send('added to queue')
    if(len(Stats.rs_company[rs])==4):
      await message.channel.send(' '.join(Stats.rs_company[rs])+str(rs+1))
      Stats.rs_company[rs].clear()
  elif message.content.lower()[0:3]=='rs-':
    Stats.rs_company[rs].remove(message.author.mention)
    
