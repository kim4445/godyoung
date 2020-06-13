import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("섹스")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("너 누구야"):
        await message.channel.send("저는 김한영박사님의 노예입니다")
    if message.content.startswith("느금마"):
        await message.channel.send("제 엄마이자 아버지는 김한영박사님이에요")
    if message.content.startswith("몇살이야"):
        await message.channel.send("저는 0.51246946548218752132살 입니다")
    if message.content.startswith("섹"):
        await message.channel.send("스")
    if message.content.startswith("남미는?"):
        await message.channel.send("미국남부이다.")
    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))
    #채널메시지
    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)
    #가위 바위 보
    import random
    if message.content.startswith("/가위바위보"): 
        number = ['a','s','d']
        hand = (random.sample(number,1))
        sungbin = message.content[7:]
        if (hand == ['a']):
            await message.channel.send("가위")
            if (sungbin == '보'):
                await message.channel.send("패배")
            if (sungbin == '바위'):
                await message.channel.send("승리")
            if (sungbin == '가위'):
                await message.channel.send("무승부")
        if (hand == ['s']):
            await message.channel.send("바위")
            if (sungbin == '보'):
                await message.channel.send("승리")
            if (sungbin == '바위'):
                await message.channel.send("무승부")
            if (sungbin == '가위'):
                await message.channel.send("패배")
        if (hand == ['d']):
            await message.channel.send("보")
            if (sungbin == '보'):
                await message.channel.send("무승부")
            if (sungbin == '바위'):
                await message.channel.send("패배")
            if (sungbin == '가위'):
                await message.channel.send("승리")
    



client.run("NzIwMTcxNDg0MTQ4MTM4MDA0.XuOFhA.0YpJh5Fo2daZ40IQ8wmpFmAbsW4")