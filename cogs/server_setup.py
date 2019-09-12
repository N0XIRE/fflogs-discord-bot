import discord
import asyncio
import json
import os.path
import shutil
from discord.ext import commands
from discord.ext.commands import Bot

#with open('help.json', 'r') as f:
    #help = json.load(f)


class server_setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['config'])
    async def setup(self, ctx):
        id = ctx.author.guild.id

        if os.path.exists(f'servers/{id}.json'):
            with open(f'servers/{id}.json', 'r') as f:
                guild_config = json.load(f)

            embed = discord.Embed(title="Setup FFLogs Bot", description=f"-logs {guild_config['logs_channel']}\n-guild {guild_config['guild_name']}\n-world {guild_config['guild_world']}\n-region {guild_config['guild_region']}", color=0x589BFF)

        else:
            embed = discord.Embed(title="Setup FFLogs Bot", description="-logs <#channel>\n-guild <\"fflogs guild\">\n-world <guild world>\n-region <guild region>", color=0x589BFF)
        message = await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def logs(self, ctx, string = None):
        id = ctx.author.guild.id

        if string is not None:
            if not os.path.exists(f'servers/{id}.json'):
                shutil.copyfile('servers/guild_template.json', f'servers/{id}.json')

            with open(f'servers/{id}.json', 'r+') as f:
                guild_config = json.load(f)
                guild_config['logs_channel'] = string
                print(guild_config['logs_channel'])
                f.seek(0)
                json.dump(guild_config, f)
                f.truncate()

            embed = discord.Embed(title="Success", description="_ _", color=0x00FF00)
        else:
            embed = discord.Embed(title="Failure, please provide a log channel.", description="_ _", color=0xFF0000)

        message = await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def guild(self, ctx, string = None):
        id = ctx.author.guild.id

        if string is not None:
            if not os.path.exists(f'servers/{id}.json'):
                shutil.copyfile('servers/guild_template.json', f'servers/{id}.json')

            with open(f'servers/{id}.json', 'r+') as f:
                guild_config = json.load(f)
                guild_config['guild_name'] = string
                print(guild_config['guild_name'])
                f.seek(0)
                json.dump(guild_config, f)
                f.truncate()

            embed = discord.Embed(title="Success", description="_ _", color=0x00FF00)
        else:
            embed = discord.Embed(title="Failure, please provide a log channel.", description="_ _", color=0xFF0000)

        message = await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def world(self, ctx, string = None):
        id = ctx.author.guild.id

        if string is not None:
            if not os.path.exists(f'servers/{id}.json'):
                shutil.copyfile('servers/guild_template.json', f'servers/{id}.json')

            with open(f'servers/{id}.json', 'r+') as f:
                guild_config = json.load(f)
                guild_config['guild_world'] = string
                print(guild_config['guild_world'])
                f.seek(0)
                json.dump(guild_config, f)
                f.truncate()

            embed = discord.Embed(title="Success", description="_ _", color=0x00FF00)
        else:
            embed = discord.Embed(title="Failure, please provide a log channel.", description="_ _", color=0xFF0000)

        message = await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def region(self, ctx, string = None):
        id = ctx.author.guild.id

        if string is not None:
            if not os.path.exists(f'servers/{id}.json'):
                shutil.copyfile('servers/guild_template.json', f'servers/{id}.json')

            with open(f'servers/{id}.json', 'r+') as f:
                guild_config = json.load(f)
                guild_config['guild_region'] = string
                print(guild_config['guild_region'])
                f.seek(0)
                json.dump(guild_config, f)
                f.truncate()

            embed = discord.Embed(title="Success", description="_ _", color=0x00FF00)
        else:
            embed = discord.Embed(title="Failure, please provide a log channel.", description="_ _", color=0xFF0000)

        message = await ctx.message.channel.send(embed=embed)


def setup(client):
    client.add_cog(server_setup(client))
