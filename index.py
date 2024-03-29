import os
import discord
from discord.ext import commands
from utils import default
from utils.data import Bot, HelpFormat

config = default.get("config.json")
print("Logging in...")

bot = Bot(
    command_prefix=config.prefix, prefix=config.prefix,
    owner_ids=config.owners, command_attrs=dict(hidden=True),
    help_command=HelpFormat(),
    intents=discord.Intents(
        guilds=True, members=True, messages=True, reactions=True
    )
)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

try:
    bot.run(config.token)
except Exception as e:
    print(f'Error when logging in: {e}')
