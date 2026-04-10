from dotenv import load_dotenv
import os
import discord
# Con esto cargamos al sistema los .env y con os lo agarramos
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
cliente = discord.Client(intents=intents)

@cliente.event
async def on_ready():
    print(f'We have logged as {cliente.user}')

@cliente.event
async def on_message(message):
    if message.author == cliente.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@cliente.event
async def on_message(message):
    if message.author == cliente.user:
        return

    member = message.author

    if (member.activity):
        await message.channel.send(f'{member.display_name} está jugando a: {member.activity.name}')
    else:
        await message.channel.send(f'{member.display_name} no parece estar jugando a nada ahora.')



@cliente.event
async def on_typing(channel, user, _):
    await channel.send(f'doxeadisimo broder {user.name}')


cliente.run(TOKEN)
