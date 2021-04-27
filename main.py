import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("goodmorning"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await message.channel.send(m)

@client.event
async def on_message(message):
    if message.content.startswith("おやすみ"):
        if client.user != message.author:
            m = "おやすみなさい" + message.author.name + "さん！"
            await message.channel.send(m)
            
            
            
client.run("000000000000")
