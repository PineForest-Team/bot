import token_name
import discord
client = discord.Client()

@client.event
async def on_ready():
    print("Logged: {0.user}".format(client))

@client.event
async def on_message():
    if message.aughtor == client.user:
        return
    if message.content.startswitch('q'):
        await message.channel.send('w')

client.run(token_name.token_name)