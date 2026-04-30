import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot online!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(f"👋 Bem-vindo {member.mention}!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

bot.run("MTQ5OTMxMDkwODUyNTI1Mjc3OA.GCH5Mc.LMiLMjuPO9qw1Jq7tBUboC58cNYrLdGvppkHcM")
