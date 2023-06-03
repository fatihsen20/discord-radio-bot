import sys
import discord
from discord.ext import commands

token = sys.argv[1]
radio_url = sys.argv[2]
heart = "🫶"
goodbye = "👋"
slight_smile = "🙂"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def hi(ctx):
    await ctx.send("Hello "+ slight_smile + " " + ctx.author.mention)

@bot.command(commands="radio", help="Play the Radio.")
async def radio(ctx):
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()
    voice_client.play(discord.FFmpegPCMAudio(radio_url))
    await ctx.send("I'm Loser, I'm Coming! " + heart + " " + ctx.author.mention)

@bot.command(commands="bye", help="Stop the Radio.")
async def bye(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.stop()
    await voice_client.disconnect()
    await ctx.send("I'm Loser, I'm Leaving! " + goodbye + " " + ctx.author.mention)

bot.run(token)
