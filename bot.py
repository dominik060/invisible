import discord
from discord.ext import commands
import random
import math
from math import pi, sin, acos, e, erf, exp, log, asin, atan, inf, tau, ceil, comb, cos, cosh, dist, erfc, \
    fabs, fmod, fsum, gcd, log2, modf, nan, perm, sinh, sqrt, __spec__, tan, tanh, acosh, asinh, atan2, atanh, expm1, \
    floor, frexp, gamma, hypot, isinf, isnan, isqrt, __loader__, ldexp, log1p, log10, trunc, lgamma, copysign, degrees, \
    factorial, isclose, isfinite, radians, remainder
import time
import requests
from discord.ext.commands import Bot
import asyncio
import self
import os
bot: Bot = commands.Bot(command_prefix='xd ')
bot.remove_command('help')


# ----------------------------------------------------------------------------------------------------------------------
#   Events
@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print('Bot is ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='xd help'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.channel.send("That command wasn't found! Try xd help")


# ----------------------------------------------------------------------------------------------------------------------
#   Commands
@bot.command()
async def help(ctx):
    em = discord.Embed(color=discord.Color.green())
    em.title = 'Invisible bot commands'
    em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    em.description = 'Vytvořil D0M1'
    em.add_field(name="prefix", value="xd ", inline=False)
    em.add_field(name="info", value="zobrazím informace o sobě", inline=False)
    em.add_field(name="ping", value="zobrazím svoji odezvu", inline=False)
    em.add_field(name="clear (číslo)", value="vymažu počet zpráv", inline=False)
    em.add_field(name="8b (otázka)", value="odpovím na otázku", inline=False)
    em.add_field(name="help", value="zobrazí ti tadytu zprávu", inline=False)
    em.add_field(name="cat", value="ukážu ti náhodný obrázek kočky", inline=False)
    em.add_field(name="say (co)", value="napíšu to co ty", inline=False)
    em.add_field(name="xd", value="napíšu xdddddddddd", inline=False)
    em.add_field(name="math (příklad)", value="vypočtu ti matematický příklad", inline=False)
    em.add_field(name="pytlik", value="nech se překvapit", inline=False)
    em.add_field(name="dedavlese", value="nech se překvapit", inline=False)
    em.add_field(name="qp (otázka)", value="quick pool(ano, ne)", inline=False)
    em.add_field(name="pool (otázka)", value="stajný jak qp, ale lépe vypadá", inline=False)
    em.add_field(name="spam (co)", value="prostě budu spamit dokud mě nevypneš", inline=False)
    em.add_field(name="stop", value="zrusi spam", inline=False)
    em.add_field(name="ban (jméno, důvod)", value="prostě ban", inline=False)
    em.add_field(name="unban (jméno)", value="prostě unban", inline=False)
    em.add_field(name="help", value="zobrazím tadytu zprávu", inline=False)
    await ctx.channel.send(embed=em)


@bot.command(pass_context=True)
async def info(ctx):
    em = discord.Embed(color=discord.Color.green())
    em.title = 'Invisible bot Info'
    em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    em.description = 'Vytvořen D0M1.'
    em.add_field(name="Servery", value=len(bot.guilds))
    em.add_field(name="Online Uživatelé",
                 value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})))
    em.add_field(name='Kanály', value=f"{sum(1 for g in bot.guilds for _ in g.channels)}")
    em.set_footer(text="Invisible bot | D0M1")
    await ctx.channel.send(embed=em)


@bot.command()
async def ping(ctx):
    em = discord.Embed(color=discord.Color.blue())
    em.add_field(name=f"Pong 🏓!", value=f"{round(bot.latency * 1000)}ms")
    await ctx.channel.send(embed=em)


@bot.command(aliases=['8b'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
    em = discord.Embed()
    em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    em.add_field(name=f"Question: ", value=f"{question}", inline=True)
    em.add_field(name="Answer: ", value=f"{random.choice(responses)}", inline=False)
    await ctx.send(embed=em)

@bot.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.channel.send(data['file'])


@bot.command()
async def math(ctx, *, expression: str):
    calculation = eval(expression)
    await ctx.send('Math: {}\nAnswer: {}'.format(expression, calculation))


@bot.command()
async def pool(ctx,  *, question):
    await ctx.channel.purge(limit=1)
    em = discord.Embed(color=discord.Color.blue())
    em.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    em.add_field(name=f"{question}", value="✅ yes    ❎ no")
    await ctx.channel.send(embed=em)
    message = await ctx.channel.send("᲼᲼᲼᲼᲼᲼")
    await message.add_reaction(emoji="✅")
    await message.add_reaction(emoji="❎")

@bot.command()
async def qp(ctx,  *, question):
    await ctx.channel.purge(limit=1)
    name=ctx.message.author.name
    message = await ctx.send(f'{name}: {question}')
    await message.add_reaction('✅')
    await message.add_reaction('❎')

@bot.command()
async def invites(ctx, author):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"{author} invited {totalInvites} member{'' if totalInvites == 1 or 0 else 's'} to the server!")


global a
a = 0


@bot.command()
async def spam(ctx, *args):
    global a
    a = 0
    response = ""
    for arg in args:
        response = response + " " + arg
    while True:
        if a == 1:
            break
        elif a == 0:
            await ctx.send(response)
            time.sleep(1)
        else:
            break


@bot.command()
async def stop(ctx):
    global a
    a = 1
    await ctx.send("stopped")


@bot.command()
async def dedavlese(ctx):
    response = """
Běží děda po lese
všechno na něm třese se
přehání to s projímadlem
třese mu to s jeho sádlem
máš to marný staříku nedoběhneš k hajzlíku!!!!
                """
    await ctx.channel.send(response)


@bot.command()
async def pytlik(ctx):
    response = """
Dnes ráno na záchodě,
strašlivě jsem vykřik.
Pod prkýnko od hajzlíku,
přiskřip jsem si pytlík.
"""
    await ctx.channel.send(response)


bot.run(os.environ['TOKEN'])
