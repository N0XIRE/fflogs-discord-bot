import discord
import asyncio
import json
from discord.ext import tasks, commands
from discord.ext.commands import Bot


class fetcher(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.id = 0
        self.log_watcher.start()

    def cog_unload(self):
        self.log_watcher.cancel()

    @tasks.loop(seconds=15.0)
    async def log_watcher(self):
        print(self.id)
        self.id += 1

    @log_watcher.before_loop
    async def before_log_watcher(self):
        print('Waiting for bot init...')
        await self.client.wait_until_ready()
        print('Launching log_watcher')


def setup(client):
    client.add_cog(fetcher(client))
