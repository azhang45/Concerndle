import nextcord
from nextcord.ext import commands
import config
import methods
import linecache
import random

client = commands.Bot(command_prefix="$")
PREFIX = "$"
SOLVED = True
correctWord = ""


@client.event
async def on_ready():
    print("bot is awake")
    

@client.event
async def on_message(message):
    if message.author.bot:
            return
    
    if message.author.id == 723910433966260336 and ('print bot version' == message.content.lower() or 'pbv' == message.content.lower()):
            await message.channel.send('0.0.5')

    if message.content[0] == PREFIX:
        global SOLVED
        global correctWord
        if message.content[1:] == 'concerndle' and SOLVED:
            SOLVED = False
            correctWord = methods.chooseWord("wordle-answers-alphabetical.txt")
            await message.channel.send(correctWord)
            return
        elif len(message.content) == 6 and not SOLVED:
            await message.channel.send(methods.checkCorrect(message.content[1:], correctWord))
            return
            

    if message.content == 'test':
        await message.channel.send("<:white_large_square:959676720930258984>" + "<:yellow_square:959677336750534686>" + "<:green_square:959677336750534686>")


# @client.command()
# async def concerndle(ctx):
#     await ctx.send(chooseWord("wordle-answers-alphabetical.txt"))

client.run(config.TOKEN) 