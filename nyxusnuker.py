import discord
import os
import aiohttp
import requests
import random
import json
import io
import asyncio
from PIL import Image
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from colorama import init, Fore
from datetime import datetime, timedelta

token = 'MTI3ODQ1MzcyNzAzMTg1NzIwNA.GCNfZf.GCVc8rVMpKrLjfIlzngzztkblOOnmenpxxI9eU' # https://discord.com/oauth2/authorize?client_id=1278453727031857204&permissions=8&integration_type=0&scope=bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} connected')

@bot.tree.command(name="nuke", description="Delete all channels, voice channels, categories, and roles in the server, Basically launch a nuke.")
async def nuke(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("error: not in server", ephemeral=True)
            return
        await interaction.response.send_message("Nuke has been launched", ephemeral=True)
        for channel in guild.channels:
            await channel.delete(reason="Nuke was launched")
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete(reason="Nuke was launched")
                except Exception as e:
                    print(f"Cant delete role cuz its probably above the bots role {role.name}: {e}")

        await interaction.followup.send("Nuke has evaporated the server.", ephemeral=True)
    else:
        await interaction.response.send_message("No perms", ephemeral=True)

bot.run(token)
