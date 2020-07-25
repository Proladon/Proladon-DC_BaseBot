import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio

# load settings
with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

bot = commands.Bot(command_prefix=jdata['Prefix'], owner_id=jdata['Owner_id'])

@bot.event
async def on_ready():
	print(">> Bot is online <<")

# load all extensions
for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(jdata['TOKEN'])
	