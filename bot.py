import discord
import os

bot = discord.bot()


@bot.event
async def on_ready():
    print("Bot is ready!")


bot.run(os.environ['TOKEN'])