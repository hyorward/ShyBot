# bot.py
import asyncio
import os
import random
from datetime import datetime
import pytz
import discord
import requests
from discord import Intents
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv

VOL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 - reconnect_streamed 1 - reconnect_delay_max 5', 'options': '-vn'
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PRAYER_API_URL = 'http://api.aladhan.com/v1/timingsByCity'

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print('hui')

# async def get_prayer_times(city, country):
#     params = {
#         'city': city,
#         'country': country,
#         'method': 2
#     }
#     response = requests.get(PRAYER_API_URL, params=params)
#     data = response.json()
#     timings = data['data']['timings']
#     return timings
#
#
#
#
#
#
# @tasks.loop(minutes=1)
# async def check_prayer_times(self, ctx: commands.Context):
#     now = datetime.now(pytz.timezone('Europe/Moscow'))
#     current_time = now.strftime('%H:%M')
#     target_time = '19:13'
#     print(current_time)
#     if target_time == current_time:
#         voice_channel = ctx.author.voice.channel
#         vc = await voice_channel.connect()
#         vc.play(discord.FFmpegPCMAudio('azan.mp3'))
#         await ctx.send('Listening..')
#         while vc.is_playing():
#             await asyncio.sleep(1)
#         await vc.disconnect()
#         await ctx.send('Done')

    # timings = await get_prayer_times('Makhachkala', 'Russia')
    # for prayer, time in timings.items():
    #     if current_time == time[:-3]:
    #         for vc in bot.voice_clients:
    #             if vc.is_connected():
    #                 vc.play(discord.FFmpegPCMAudio('azan.mp3'))
    #                 while vc.is_playing():
    #                     asyncio.sleep(1)
    #                 await vc.disconnect()



@bot.hybrid_command(name='chort', description='Who is chort?')
@app_commands.describe(names='Names to choose from')
@app_commands.choices(names=[
    discord.app_commands.Choice(name='Abdulmalik', value=1),
    discord.app_commands.Choice(name='Abdurashid', value=2),
    discord.app_commands.Choice(name='Arthur', value=3),
    discord.app_commands.Choice(name='Burgers', value=4),
    discord.app_commands.Choice(name='Ibrahim', value=5),
    discord.app_commands.Choice(name='Ibrahim Chort', value=14),
    discord.app_commands.Choice(name='Maga Abdal', value=6),
    discord.app_commands.Choice(name='Maga Chort', value=7),
    discord.app_commands.Choice(name='Maga Shlang', value=8),
    discord.app_commands.Choice(name='Magashka', value=9),
    discord.app_commands.Choice(name='Murad', value=10),
    discord.app_commands.Choice(name='Muslim', value=11),
    discord.app_commands.Choice(name='Pelin', value=12),
    discord.app_commands.Choice(name='Yura', value=13)
])
async def play_random(ctx, names: discord.app_commands.Choice[int]):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(f'{names.value}.mp3'))
    await ctx.send('Playing..')
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    await ctx.send('Done')



@bot.hybrid_command(name='soundpad', description='Different sounds from memes')
@app_commands.describe(names='Names to choose from')
@app_commands.choices(names=[
    discord.app_commands.Choice(name='Down syndrome', value=15),
    discord.app_commands.Choice(name='Blin, na..', value=16),
    discord.app_commands.Choice(name='Bruh', value=17),
    discord.app_commands.Choice(name='Kazakhstan bomb', value=18),
    discord.app_commands.Choice(name="I'm a muslim", value=19),
    discord.app_commands.Choice(name='To be continued..', value=20),
    discord.app_commands.Choice(name="No", value=22),
    discord.app_commands.Choice(name="Let's go..", value=23),
    discord.app_commands.Choice(name="Good night", value=24),
    discord.app_commands.Choice(name="KurbanHaji", value=25),
    discord.app_commands.Choice(name="I'm a Dagestan", value=26),
    discord.app_commands.Choice(name="The earth is round", value=27),
    discord.app_commands.Choice(name="Do the tining", value=28),
    discord.app_commands.Choice(name="I'm a georgian", value=29),
    discord.app_commands.Choice(name="Avaretc...!", value=32),
    discord.app_commands.Choice(name="Sheep came home", value=33),
    discord.app_commands.Choice(name="Autumn", value=35),
    discord.app_commands.Choice(name="Don't write here anymore", value=36),
    discord.app_commands.Choice(name="Once you live...", value=37),
    discord.app_commands.Choice(name="Working!", value=39),
    discord.app_commands.Choice(name="What a luxury!", value=40),
    discord.app_commands.Choice(name="Hello", value=42),
    discord.app_commands.Choice(name="How do you tell with me?", value=43),
    discord.app_commands.Choice(name="Assalamu Aleykum", value=44),
    discord.app_commands.Choice(name="Laugh", value=45)
])
async def play_random(ctx, names: discord.app_commands.Choice[int]):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(f'{names.value}.mp3'))
    await ctx.send('Playing..')
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    await ctx.send('Done')


@bot.hybrid_command(name='blessyou', description='Bless you!')
async def bless_random(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    audio_files = ['blessyou', 'blessyou1']
    random_audio = random.choice(audio_files)
    vc.play(discord.FFmpegPCMAudio(random_audio + '.mp3'))
    await ctx.send('Blessing..')
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    await ctx.send('Done')


@bot.hybrid_command(name='goodmorning', description='Good Morning!')
async def bless_random(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio('dobr.mp3'))
    await ctx.send('Listening..')
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    await ctx.send('Done')


@bot.hybrid_command(name='podkol', description='Kirkorov meme')
async def podkol_kirk(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await  voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio('podkol.mp3'))
    await ctx.send('Listening to Kirkorov..')
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    await ctx.send('Done')

@bot.hybrid_command(name='azan', description='Listen to the azan')
async def azan_islam(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio('azan.mp3'))
    await ctx.send('Listening..')
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()
    await ctx.send('Done')


@bot.hybrid_command(name='eblan', description='Who is eblan?')
async def eblan(ctx: commands.Context):
    eblans = {
        'Abdulmalik': 'https://sun9-38.userapi.com/impg/aMkwKLPU4OBUNm99rBvg_GW6TgYLU5SBWLWMgw/dhl67wT6U7k.jpg?size=1280x720&quality=96&sign=d899cacf324dc6fde4e058b3c0e534e6&type=album',
        'IbraGYM': 'https://sun9-14.userapi.com/impg/ES-LTLaUoTHBDh4TRItcwnOeFGKQgVb0F0HzzQ/kGyDSdYEybE.jpg?size=1280x960&quality=96&sign=5293f6de1df6c2367abeba2cef601915&type=album',
        'IbraYoung': 'https://sun9-40.userapi.com/impg/T42rHghBi86bcTyB24zierWlmekd9GLmjOXUhA/XoWAMnYrNgc.jpg?size=719x1280&quality=96&sign=aaf866d4b81f0f15070245a8d6672979&type=album',
        'Ibra)))': 'https://sun9-79.userapi.com/impg/VUoHVCT0z8do7qJwXFnEJr-fXouz25U2TwR2Cg/_XjtypyRSII.jpg?size=591x1280&quality=96&sign=680dba7e1fcb82f2913a600c1de9ed81&type=album',
        'Arthur': 'https://sun9-25.userapi.com/impg/or5g_QubRNay50hZNa-ObbvGXv6QIX1m9ghlsw/_QbYNgw2V9c.jpg?size=720x1280&quality=96&sign=29d21721b4d7abc526d22af6a835e61e&type=album',
        'IbraDamn': 'https://sun9-3.userapi.com/impg/LwTArYkntlf4sgGB1WAONloOck8eUWfp4g5vyw/78VP9mzIbaM.jpg?size=962x1280&quality=96&sign=7cea7f301f8ef95b13df133cecae7533&type=album',
        'AbdurashidBoxer': 'https://sun9-70.userapi.com/impg/5an2tuhS6urYSMUiKAuwYHcg-R9K6fUVAcRCaw/13RS4aAsuMg.jpg?size=959x1280&quality=96&sign=68745495aeebb98b340150694b4c2582&type=album',
        'Austrian_painter': 'https://sun9-6.userapi.com/impg/QcTbGpPnOq1A0eokG3LveHPpVYwweW4tAe_HuQ/gtHeFxncclg.jpg?size=960x1280&quality=96&sign=c816d38571d19d4d64691e7c408981ff&type=album',
        'Ibra': 'https://sun9-59.userapi.com/impg/B8A05ocajCcCXrl2w8EQSiOxPGNbpNZ-NzLT3g/ITxrnm4mabY.jpg?size=720x1280&quality=96&sign=9896a19ced1465b2e071fc652b5a463c&type=album',
        'MuradMewing': 'https://sun9-26.userapi.com/impg/L1EuCF7UpixAD-wrHxkN0OdQURegP43iKux06A/RUI5mQp0IjI.jpg?size=960x1280&quality=96&sign=4ecdf1dfa1f4e6e9e85518e0aded5244&type=album',
        'ShamilKaspiysky': 'https://sun9-73.userapi.com/impg/9ySZzhuTLuJkKO8YsHl5fNElCSvEfFbMUOw0Bg/SFQ4Sw8Nb-U.jpg?size=640x640&quality=96&sign=6fa3af09fad17d070c0d5b20714365cc&type=album',
        'Miguel': 'https://sun9-54.userapi.com/impg/Vwiw5p2Cl9imGIg9BYL-Ae2PDUHDEhXDJfxgcg/AMH2bO53dcs.jpg?size=961x1280&quality=96&sign=cce920539f6c670bd9e905195337fc60&type=album',
        'Muslim': 'https://sun9-13.userapi.com/impg/iC7aVyilZK4nLbSQUEwlvcXk80r_Vf4tiKknyA/XJkKcIn2ppY.jpg?size=634x960&quality=95&sign=7fdca33dd205595fc7ea9079260da94a&type=album',
        'Yura': 'https://sun9-76.userapi.com/impg/0xZFvyo3tMhBuyJNz6aEYRlK0OEsbCVFNt77YQ/m-sr1cZ-qc8.jpg?size=367x578&quality=96&sign=9a0c24eb9629f2df3c10a1ae2bd673a6&type=album'
    }
    (key, val) = random.choice(list(eblans.items()))
    e = discord.Embed(
        title=key,
        colour=discord.Colour.from_rgb(38, 38, 38)
    )
    e.set_image(url=val)
    await ctx.send(embed=e)




@bot.hybrid_command(name='online', description='Langcraft online')
async def langcraft_online(ctx: commands.Context):
    response = requests.get('https://backend.langcraft.site/api/v1/server-info/')
    online = response.json()['players_count']
    await ctx.send(f'**Langcraft online: {online}**')

@bot.hybrid_command(name='nation', description='Langcraft nation')
async def langcraft_nation(ctx: commands.Context):
    response = requests.get('https://backend.langcraft.site/api/v1/nations/')
    nation_ids = [item['id'] for item in response.json()]
    id = random.choice(nation_ids)
    response = requests.get(f'https://backend.langcraft.site/api/v1/nations/{id}')
    name = response.json()['name']
    desc = response.json()['description']
    flag = response.json()['flag']
    e = discord.Embed(
        title=name,
        description=desc,
        colour=discord.Colour.from_rgb(38, 38, 38)
    )
    e.set_image(url=flag)
    await ctx.send(embed=e)

bot.run(TOKEN)

