import discord
import asyncio
import json
from discord.ext import commands
from discord.ext.commands import Bot

with open('help.json', 'r') as f:
    help = json.load(f)


class info:
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(info(client))
