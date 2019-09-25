import discord
import asyncio
import json
import requests
import datetime
from discord.ext import tasks, commands
from discord.ext.commands import Bot
import os
import ast

loop = asyncio.get_event_loop()


class fetcher(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.id = 0
        self.server = None
        self.logs_channel = None
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.api_key = config['fflogsAPI']
        self.log_watcher.start()

    def cog_unload(self):
        self.log_watcher.cancel()

    @tasks.loop(seconds=15.0)
    async def log_watcher(self):
        print(self.id)
        self.id += 1

        servers = os.listdir('/home/programming/fflogs-discord-bot/servers')
        servers = [x.replace('.json', '') for x in servers]
        servers.pop(0)

        for server in servers:
            self.server = server

            with open(f'servers/{server}.json', 'r') as f:
                guild_config = json.load(f)
                self.logs_channel = guild_config['logs_channel'][2:-1]
                guildName = guild_config['guild_name'].replace(' ', '%20')
                serverName = guild_config['guild_world']
                serverRegion = guild_config['guild_region']

            url = f'https://www.fflogs.com:443/v1/reports/guild/{guildName}/{serverName}/{serverRegion}?api_key={self.api_key}'
            r = requests.get(url)
            reports = r.json()

            if not guild_config['last_log']:
                await self.log_sender(reports[0])
                guild_config['last_log'] = reports[0]['id']
            else:
                for report in reports:
                    if report['id'] == guild_config['last_log']:
                        break
                    else:
                        await self.log_sender(report)
                guild_config['last_log'] = reports[0]['id']

            # with open(f'servers/{server}.json', 'w') as f:
                #json.dump(guild_config, f)

    async def log_sender(self, log=None):
        embed = discord.Embed(title=f"{log['owner']} has uploaded a new log", description="_ _", color=0xFF00FF)
        embed.add_field(name="Info", value=f"{log['title']}\nID: {log['id']} \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b\u200b \u200b \u200b \u200b \n", inline=True)
        embed.add_field(name="Links", value="[FFLogs](https://www.fflogs.com/reports/{log['id']})\n[XIVAnalysis](https://xivanalysis.com/find/{log['id']})", inline=True)
        embed.set_footer(text=f"Uploaded: {datetime.datetime.now().strftime('%m/%d/%Y %H:%M CT')}")
        channel = self.client.get_channel(603038874939293708)
        message = await channel.send(embed=embed)

    @log_watcher.before_loop
    async def before_log_watcher(self):
        print('Waiting for bot init...')
        await self.client.wait_until_ready()
        print('Launching log_watcher')


def setup(client):
    client.add_cog(fetcher(client))
