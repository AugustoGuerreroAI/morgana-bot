from discord.ext import commands
import discord

class Normales(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Todos los comandos normales acá
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int):
        # Código limpiar mensajes
        pass

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("Hello!")

    @commands.command()
    async def status(self, ctx: commands.Context, user: discord.Member = None):
        objetivo = user or ctx.author
        try:
            actividades_total = objetivo.activities

            reporte = f'reportando que carajos tiene {objetivo.display_name} \n'
            reporte += f'- {objetivo.status} \n'
            reporte += f'{len(actividades_total)}'

            print(reporte)

            nombre_juego = objetivo.activity.name
            await ctx.send(f' {objetivo.name} se encuentra jugando a: {nombre_juego}')
        except AttributeError:
            await ctx.send(f'💤 {objetivo.name} no está jugando a nada (o Discord me lo ocultan no se porque lrpm).')

        

    @commands.command()
    async def avatar(self, ctx: commands.Context, user: discord.Member = None):
        if (user != None):
            await ctx.send(f'{user.avatar}')
        else:
            member = ctx.author
            await ctx.send(f'{member.avatar}')

        

    

async def setup(bot):
    await bot.add_cog(Normales(bot))
