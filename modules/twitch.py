import discord
from discord.ext import commands
from utils.twitch_api import get_followed_streamers

class Twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="follows")
    async def list_followed_streamers(self, ctx):
        """Shows a list of streamers you follow on Twitch"""
        streamers = get_followed_streamers()

        print(f"🔍 DEBUG: Fetched streamers -> {streamers}")

        if isinstance(streamers, str):  # Error message
            await ctx.send(streamers)
            return
        
        if not streamers:
            await ctx.send("❌ You are not following any streamers.")
            return
        
        # Chunk the message if it's too long (Discord limits messages to 2000 characters)
        message = "**🎮 Streamers you follow:**\n"
        for streamer in streamers:
            message += f"- {streamer}\n"

        # If the message is too long, split it
        if len(message) > 2000:
            parts = [message[i : i + 2000] for i in range(0, len(message), 2000)]
            for part in parts:
                await ctx.send(part)
        else:
            await ctx.send(message)
        

async def setup(bot):
    await bot.add_cog(Twitch(bot))
