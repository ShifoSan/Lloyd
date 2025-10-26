# lloyd.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='quote', help='Responds with a random quote.')
async def quote(ctx):
    quotes = [
        'The only thing we have to fear is fear itself.',
        'Be yourself; everyone else is already taken.',
        'Two things are infinite: the universe and human stupidity; and I\'m not sure about the universe.',
    ]

    response = random.choice(quotes)
    await ctx.send(response)

bot.run(TOKEN)
