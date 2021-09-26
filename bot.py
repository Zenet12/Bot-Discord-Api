import discord  # Don't touch this line
import requests # Don't touch this line
import json # Don't touch this line
from discord.ext import commands # Don't touch this line

bot = commands.Bot(command_prefix='!')  # Where ! change to your tag or leave it like that

@bot.command()
async def fact(ctx):
    r = requests.get("https://some-random-api.ml/facts/dog")    # The link from which the api request is taken
    api = json.loads(r .text)
    get = api['fact']
    await ctx.send(get) # This function is responsible for sending a message

@bot.command()  # If you want your text to be used before the text from the api, then use this request option
async def facttext(ctx):
    r = requests.get("https://some-random-api.ml/facts/dog")    # The link from which the api request is taken
    api = json.loads(r .text)
    get = api['fact']
    await ctx.send(f"fact: {get}") # This function is responsible for sending a message

bot.run('token')