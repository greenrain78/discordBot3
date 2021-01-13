import asyncio

import discord
from discord.ext import commands

from Basic.basic_engine import BasicEngine


class BasicBot(commands.Cog):
    def __init__(self, para_bot, pointBot, erbsBot):
        self.bot = para_bot
        self.engine = BasicEngine(pointBot, erbsBot)

    @commands.command()
    async def botState(self, ctx):
        """
        디코 봇 상태 확인
        """
        name = ctx.message.author.name
        if name == '김대원':
            text = self.engine.getState()
            await ctx.send(text)
            await asyncio.sleep(60)
            await ctx.message.delete()  # 입력된 명령 제거
