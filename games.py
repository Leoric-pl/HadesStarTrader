import random
import discord
mod0=[]
mod1=[]
mod2=[]
mod3=[]
mod4=[]
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
primnum=[2,3,5,7,11]

async def games(message):

  #game 1

  if message.content.lower()[2:4]=='1g':
    mod0.clear()
    for i in primnum:
      mod0.append(random.randint(0,i-1))
    await message.channel.send('New number in game 1  generated')
    reply=''
    for i in primnum:
      reply=reply+(str)(mod0[primnum.index(i)])
    print(reply)
  elif message.content.lower()[2:4]=='1i':
    reply='Your challange is to guess number, that is random. You get tip every time(**T**) every time when given number modulo 2,3,5, 7 or 11 is equal to basic number... find number and win!'
    await message.channel.send(reply)
  elif message.content.lower()[2:4]=='1:':
    givenN=(int)(message.content.lower()[4:])
    reply='N:'
    for i in primnum:
      if givenN % i==mod0[primnum.index(i)]:
        reply=reply+' **T** '
      else:reply=reply+' F '
    await message.channel.send(reply)
    if reply=='N: **T**  **T**  **T**  **T**  **T** ':
      await message.channel.send('congratz, U found it!')
      mod0.clear()
      for i in primnum:
        mod0.append(random.randint(0,i-1))
      await message.channel.send('New number in game 1  generated')
      reply=''
      for i in primnum:
        reply=reply+(str)(mod0[primnum.index(i)])
      print(reply)

      #game 2

  elif message.content.lower()[2:4]=='2g':
    mod1.clear()
    for i in primnum:
      mod1.append(random.randint(0,i-1))
    await message.channel.send('New number in game 2  generated')
    reply=''
    for i in primnum:
      reply=reply+(mod1[primnum.index(i)])
    print(reply)
  elif message.content.lower()[2:4]=='2i':
    reply='Your challange is to guess number, that is random. You get tip every time every time when given number modulo 2,3,5, 7 or 11 is equal to basic number... this tme You do not know wchich number gives good answer, just number of correct pointers'
    await message.channel.send(reply)
  elif message.content.lower()[2:4]=='2:':
    correctPointer=0
    givenN=(int)(message.content.lower()[4:])
    reply='Correct:'
    for i in primnum:
      if givenN % i==mod1[primnum.index(i)]:
        correctPointer+=1
      reply=reply+(str)(correctPointer)
    await message.channel.send(reply)
    if correctPointer==5:
      await message.channel.send('congratz, U found it!')
      mod1.clear()
      for i in primnum:
        mod1.append(random.randint(0,i-1))
      await message.channel.send('New number in game 2  generated')
      reply=''
      for i in primnum:
        reply=reply+(str)(mod1[primnum.index(i)])
      print(reply)

      #game 3

  elif message.content.lower()[2:4]=='3g':
    mod2.clear()
    for i in primnum:
      mod2.append(random.randint(0,i-1))
    reply=''
    for i in primnum:
      reply=reply+(str)(mod2[primnum.index(i)])
    print(reply)
    reply=''
    for i in range (11):
      correctPointer2=0
      for k in primnum:
        if i%k==mod2[primnum.index(k)]:
          correctPointer2+=1
      reply+=(str)(correctPointer2)
    await message.channel.send('Generated: '+ reply)
  elif message.content.lower()[2:4]=='3i':
      reply='Your challange is to guess number, that is random. You get sequence of SUM and You need to write modulo to each number of (2,3,5,7,11) as one number. SUM in each position is increased if it has same modulo (2,3,5,7,11) as generated number'
      await message.channel.send(reply)
  elif message.content.lower()[2:4]=='3:':
    correctPointer2=0
    givenN2=(int)(message.content.lower()[4:5])
    givenN3=(int)(message.content.lower()[5:6])
    givenN5=(int)(message.content.lower()[6:7])
    givenN7=(int)(message.content.lower()[7:8])
    givenN11=(int)(message.content.lower()[8:])
    reply='Correct:'
    if (givenN2 ==mod2[primnum.index(2)]) and (givenN3 ==mod2[primnum.index(3)]) and (givenN5 ==mod2[primnum.index(5)]) and (givenN7 ==mod2[primnum.index(7)]) and (givenN11 ==mod2[primnum.index(11)]):
      await message.channel.send('congratz, U found it!')
      mod1.clear()
    else: await message.channel.send('Wrong!')

    #game 4

  elif message.content.lower()[2:4]=='4g':
    mod3.clear()
    for i in range(2, 8):
      mod3.append(random.randint(0,i-1))
    reply=''
    for i in range(2, 8):
      reply=reply+(str)(mod3[i-2])
    print(reply)
    reply=''
    for i in range (11):
      correctPointer3=0
      for k in range(2, 8):
        if i%k==mod3[k-2]:
          correctPointer3+=1
      reply+=(str)(correctPointer3)
    await message.channel.send('Generated: '+ reply)
  elif message.content.lower()[2:4]=='4i':
    reply='Your challange is to guess number, that is random. You get sequence of SUM and You need to write modulo to each number of (2,3,4,5,6,7) as one number. SUM in each position is increased if it has same modulo (2,3,4,5,6,7) as generated number'
    await message.channel.send(reply)
  elif message.content.lower()[2:4]=='4:':
    correctPointer3=0
    givenN2=(int)(message.content.lower()[4:5])
    givenN3=(int)(message.content.lower()[5:6])
    givenN4=(int)(message.content.lower()[6:7])
    givenN5=(int)(message.content.lower()[7:8])
    givenN6=(int)(message.content.lower()[8:9])
    givenN7=(int)(message.content.lower()[9:10])
    reply='Correct:'
    if (givenN2==mod3[0]) and (givenN3==mod3[1]) and (givenN4==mod3[2]) and (givenN5==mod3[3]) and (givenN6==mod3[4]) and (givenN7==mod3[5]):
      await message.channel.send('congratz, U found it!')
      mod1.clear()
    else: await message.channel.send('Wrong!')

    #game 5

  elif message.content.lower()[2:4]=='5g':
    mod4.clear()
    for i in range(5):
      mod4.append(random.sample(letters,1))
    reply=''
    await message.channel.send('Generated: '+ reply)
  elif message.content.lower()[2:4]=='5i':
    reply='Rules like in mastermind, but instead of colours are letters(a-z), 5 signs to get'
    await message.channel.send(reply)
  elif message.content.lower()[2:4]=='5:':
    correctPointer=0
    givenN=message.content.lower()[4:9]
    givenT=[]
    correctPointer4a=0
    correctPointer4b=0
    for i in range(5):
      givenT=givenN[i]
      if givenT[i]==mod4[i]:
        correctPointer4a+=1
      else: 
        for a in range(5):
          if givenT[i]==mod4[a] and mod4[a] != givenT[a]:
            correctPointer4b+=1
    reply='Correct places: '+correctPointer4a+', correct signs: '+correctPointer4b
    await message.channel.send(reply)
    reply='Correct:'
    if correctPointer4a==5:
      await message.channel.send('congratz, U found it!')
      mod4.clear()
    else: await message.channel.send('Wrong!')

  elif message.content.lower()[2:3]=='?' or message.content.lower()[2:3]=='i':
    reply='to start game just write **:g[number]g**, for now there are 4 games(egzample:**:g1g**)\n'+                 'to read instructions to game write **:g[number]i** (egzample:**:g1i**)\n'+                                         'to check number in game write **:g[number]:[TriedNumber]** (egzample:**:g1:10**)'
    await message.channel.send(reply)
