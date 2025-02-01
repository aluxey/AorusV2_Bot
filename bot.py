import discord
import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv
from config import DISCORD_TOKEN

load_dotenv()
# Définition des intents
intents = discord.Intents.default()
intents.message_content = True

# Création du bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} est en ligne !')

async def load_modules():
    await bot.load_extension("modules.twitch")

@bot.command()
async def hello(ctx):
    """Commande qui répond avec un message de bienvenue"""
    await ctx.send("👋 Salut, je suis ton bot !")

async def main():
    await load_modules()
    await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())