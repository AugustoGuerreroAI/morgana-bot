import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv() #Cargo .env y lo mando a variables de entorno

def create_intents() -> discord.Intents:
    return discord.Intents.all()

def get_token() -> str:
    return os.getenv("DISCORD_TOKEN")

# Here I get the intents in order to make the Bot track messages and presences and that stuff
intents: discord.Intents = create_intents()
# Trying to get the token from the .env file
TOKEN = get_token()

class MorganaBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='!m ', intents=intents)

    async def setup_hook(self):
        # Con esta fucion me encargo de que busque todos los comandos
        await self.load_extension('comandos.normales')
        print('Modulos cargados correctamente')
    
    async def on_ready(self):
        print(f'{self.user} se encuentra en linea!!!')

bot = MorganaBot()
bot.run(TOKEN)


