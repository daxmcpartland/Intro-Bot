import discord
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = "{token}"
GUILD = "{guild}"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.id == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_voice_state_update(member, before, after):
    if client.voice_clients:
        return
    
    if before.channel is None and after.channel is not None:
        vc = await after.channel.connect()
        match member.name:
            case "nitwit0824":
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/still-a.mp3"))
            case "mazdraith":
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/cena-theme.mp3"))
            case "cj.canadaa":
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/ali-a-intro.mp3"))
            case "ninnybobinny":
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/swmg.mp3"))
            case "johnnym_":
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/taco-bell-bong.mp3"))
            case "SnazzerJazzer":
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/rizz.mp3"))
            case "snewpdogg":
                 vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/rizz.mp3"))
            case _:
                vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="./songs/swmg.mp3"))
        
        while vc.is_playing():
            await asyncio.sleep(.025)

        await vc.disconnect()


client.run(TOKEN)