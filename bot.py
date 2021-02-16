import discord, json, pyfiglet, random
import string
import random
import sys
from pyfiglet import Figlet
from discord.ext import commands, tasks
import asyncio
import json
import time
import traceback
from os import system
from random import randint
import re
from colorama import Fore, init
import platform
from time import sleep
import aiohttp
from discord import Member
from itertools import cycle
import asyncio, discord, time, sys, os, random, traceback, json
from discord import errors

bot = commands.Bot(description="dave-chan", command_prefix=".")
bot.remove_command('help')

status = cycle(['Dave-chan', '.help for help commands'])

@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user} IS ONLINE!!! WOOO')


@tasks.loop(seconds=25)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def ascii(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'```{text}```')

@bot.command()
async def request(ctx):
    r = request.get('https://google.com')
    print(r.status_code)

@bot.command()
async def doh(ctx, *, args):
    await ctx.message.delete()
    result = pyfiglet.figlet_format(args, font = "doh" ) 
    await ctx.send(f'```{result}```')

@bot.command()
async def digital(ctx, *, args):
    await ctx.message.delete()
    digit = pyfiglet.figlet_format(args, font = "digital" ) 
    await ctx.send(f'```{digit}```')

@bot.command()
async def bubble(ctx, *, args):
    await ctx.message.delete()
    bubble = pyfiglet.figlet_format(args, font = "bubble" )
    await ctx.send(f'```{bubble}```')

@bot.command(aliases=['dotma'])
async def dotmatrix(ctx, *, args):
    await ctx.message.delete()
    dot = pyfiglet.figlet_format(args, font = "dotmatrix" )
    await ctx.send(f'```{dot}```')

@bot.command(aliases=['iso'])
async def isometric(ctx, *, args):
    await ctx.message.delete()
    iso = pyfiglet.figlet_format(args, font = "isometric1" ) 
    await ctx.send(f'```{iso}```')

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not to let you know.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 "Nah never will happen.",
                 'Even I think not.',
                 'God doesnt agree with this..',
                 'no',
                 'Try simping for cat girls instead.']
    await ctx.send(f'`Question:` {question}\n`Response:` {random.choice(responses)}')


@bot.command()
async def embed(ctx, title, *, desc):
    embedVar = discord.Embed(title=title, description=desc, color=0x9400D3)
    await ctx.message.channel.send(embed=embedVar)

@bot.command(aliases=['insults'])
async def insult(ctx):
    insults = ["You're not pog.",
                 'haha poor.',
                 'smelly mick smellington.',
                 'lol trash',
                 'I bet you have a prebuilt pc.',
                 'I could eat a bowl of alphabet soup and poop out a better statement than that.',
                 'smol brain.',
                 'Here is a tissue for all the bullshit on your lip.',
                 'Your birth certifcate is an apology letter from the condom factory.',
                 'If only closed minds came with closed mouths.',
                 'You should use gluestick instead of chapstick.',
                 'You are about as useful as a knitted condom.',
                 'You are so ugly you make blind kids cry.',
                 'You sir are the reason god created the middle finger.',
                 "Your mother should've swallowed you.",
                 "It's better to let someone think you are an idiot than to open your mouth and prove it.",
                 'If you ran like your mouth you would be in good shape.',
                 'I do not know what is worse, your IQ or your hairline.',
                 'Im not saying I hate you\nbut I would unplug your life support to charge my phone.',
                 'My hairstraightener is hotter than you.',
                 "My hair is straighter than you.",
                 'I think not.',
                 'No need for insults, your face is one all by itself.',
                 'There is no vaccine against stupidity.',
                 'Somewhere out there a tree is tirelessly producing oxygen for you. I think you owe it an apology.',
                 'You must have been born on a highway because that is accidents happen.',
                 'shut ur dumdumbubblegum looking ass.']
    await ctx.send(f'{random.choice(insults)}')

@bot.command(name="kill")
async def kill(ctx, user: discord.User):
    insults = [f'<@{ctx.author.id}> killed <@{user.id}>',
                 f'<@{user.id}> called <@{ctx.author.id}> poor so they shot them.',
                 f'<@{user.id}> slipped on a rock placed by <@{ctx.author.id}>, and died',
                 ]
    await ctx.send(f'{random.choice(insults)}')

@bot.command() 
async def awp(ctx): 
    if ctx.message.author.id == 724703230130520095:
        async with ctx.channel.typing(): 
            async with aiohttp.ClientSession() as cs: 
                async with cs.get("https://evergene.io/api/animewp") as r: 
                    data = await r.json() 
                    embedca = discord.Embed(title="anIIIIIme") 
                    embedca.set_image(url=data['url']) 
                    embedca.set_footer(text="epik") 
                    await ctx.send(embed=embedca) 
    elif ctx.message.author.id == 672917108643987468:
        async with ctx.channel.typing(): 
            async with aiohttp.ClientSession() as cs: 
                async with cs.get("https://evergene.io/api/animewp") as r: 
                    data = await r.json() 
                    embedca = discord.Embed(title="anIIIIIme") 
                    embedca.set_image(url=data['url']) 
                    embedca.set_footer(text="epik") 
                    await ctx.send(embed=embedca) 

@bot.command() 
async def tickle(ctx): 
    async with ctx.channel.typing(): 
        async with aiohttp.ClientSession() as cs: 
            async with cs.get("https://evergene.io/api/tickle") as r: 
                data = await r.json() 
                embedca = discord.Embed(title="TICKLE TICKLE") 
                embedca.set_image(url=data['url']) 
                embedca.set_footer(text="watch out uwu") 
                await ctx.send(embed=embedca) 

@bot.command() 
async def slap(ctx): 
    async with ctx.channel.typing(): 
        async with aiohttp.ClientSession() as cs: 
            async with cs.get("https://evergene.io/api/slap") as r: 
                data = await r.json() 
                embedca = discord.Embed(title="SLAP NERD") 
                embedca.set_image(url=data['url']) 
                embedca.set_footer(text="spank") 
                await ctx.send(embed=embedca) 

@bot.command() 
async def hug(ctx): 
    async with ctx.channel.typing(): 
        async with aiohttp.ClientSession() as cs: 
            async with cs.get("https://evergene.io/api/hug") as r: 
                data = await r.json() 
                embedca = discord.Embed(title="huggy") 
                embedca.set_image(url=data['url']) 
                embedca.set_footer(text="uwu") 
                await ctx.send(embed=embedca) 

@bot.command() 
async def yomama(ctx): 
    async with aiohttp.ClientSession() as cs: 
        async with cs.get("https://api.yomomma.info/") as r: 
            data = await r.json() 
            await ctx.send(data['joke'])
                # embedca.set_image(url=data['joke']) 

@bot.command()
async def help(ctx):
    if ctx.message.author.id == 724703230130520095:
        embed=discord.Embed(title="Help", description="Dave-chan Help menu", color=0x0f9ace)
        embed.add_field(name="Utility commands:", value="below this are utility commands.", inline=False)
        embed.add_field(name="ping", value="test ", inline=False)
        embed.add_field(name="Embed", value="Send a embed with your own text!", inline=False)
        embed.add_field(name="Fun commands:", value="below this are fun commands", inline=False)
        embed.add_field(name="insult", value="INSULT SOMEONE to the hardest potetional.", inline=False)
        embed.add_field(name="8ball", value="Ask the 8ball some magical questions!!", inline=False)
        embed.add_field(name="hug", value="Send a hug!", inline=False)
        embed.add_field(name="slap", value="Slap someone as hard as you can!", inline=False)
        embed.add_field(name="yomama", value="wow such original", inline=False)
        await ctx.send(embed=embed)
        me = await bot.fetch_user(724703230130520095)
        await me.send('You can do .awp for the animepic and .tickle for the tickle command!')
    else:
        embed=discord.Embed(title="Help", description="Dave-chan Help menu", color=0x0f9ace)
        embed.add_field(name="Utility commands:", value="below this are utility commands.", inline=False)
        embed.add_field(name="ping", value="test ", inline=False)
        embed.add_field(name="Embed", value="Send a embed with your own text!", inline=False)
        embed.add_field(name="Fun commands:", value="below this are fun commands", inline=False)
        embed.add_field(name="insult", value="INSULT SOMEONE to the hardest potetional.", inline=False)
        embed.add_field(name="8ball", value="Ask the 8ball some magical questions!!", inline=False)
        embed.add_field(name="hug", value="Send a hug!", inline=False)
        embed.add_field(name="slap", value="Slap someone as hard as you can!", inline=False)
        embed.add_field(name="yomama", value="wow such original", inline=False)
        await ctx.send(embed=embed)

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
bot.run(token)