import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Définition des intents
intents = discord.Intents.default()
intents.message_content = True

# Création du bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} est en ligne !')

@bot.command()
async def hello(ctx):
    """Commande qui répond avec un message de bienvenue"""
    await ctx.send("👋 Salut, je suis ton bot !")

# Lancer le bot
bot.run(TOKEN)
