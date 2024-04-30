# bot.py
import asyncio
import http
import requests
import os
import random
import ffmpeg

import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

VOL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 - reconnect_streamed 1 - reconnect_delay_max 5', 'options': '-vn'
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print('hui')


@bot.hybrid_command(name='chort', description='Who is chort?')
async def play_random(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    audio_files = ['abdulmalik', 'arthur', 'adik', 'magaabdal', 'magachert', 'murad', 'muslim', 'pelinchert', 'yura', 'magahochu', 'magashka', 'rodinu', 'ibra']
    random_audio = random.choice(audio_files)
    vc.play(discord.FFmpegPCMAudio(random_audio + '.mp3'))
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
        'Muslim': 'https://sun9-13.userapi.com/impg/iC7aVyilZK4nLbSQUEwlvcXk80r_Vf4tiKknyA/XJkKcIn2ppY.jpg?size=634x960&quality=95&sign=7fdca33dd205595fc7ea9079260da94a&type=album'
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

