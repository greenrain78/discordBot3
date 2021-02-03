import asyncio

import discord
from discord.ext import commands
from Log.infoLog import logger as log

from ERBS.erbs_engine import ErbsEngine


class ERBSBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = ErbsEngine()

    @commands.command()
    async def recent(self, ctx, name):
        """
        블서 최근 전적 조회
        입력한 사용자의 가장 최근에 플래이한 블서 경기 내역을 보여준다.
        """
        try:
            text = await self.engine.recent(name)
            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")

    @commands.command()
    async def graph(self, ctx, kind, name):
        """
        블서 관련 데이터를 그래프로 그려서 보여준다.
        """
        try:
            if kind == "Top":
                text = await self.engine.topGraph(name)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")
