import asyncio

from discord.ext import commands

from Point.point_engine import PointEngine


class PointBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = PointEngine()

    @commands.command()
    async def point(self, ctx):
        """
        디코 포인트 이벤트 정보 확인
        디스코드 포인트 이벤트에 대한 정보를 확인한다.
        """
        em = self.engine.eventInfo()
        msg = await ctx.send(embed=em)
        await ctx.message.delete()  # 입력된 명령 제거
        await asyncio.sleep(60)
        await msg.delete()  # 메세지 삭제

    @commands.command()
    async def mypoint(self, ctx):
        """
        내 점수 확인
        현재 내가 보유중인 디스코드 포인트를 확인한다.
        """
        user = ctx.author.name
        text = self.engine.getPoint(user)
        await ctx.send(text)
        await ctx.message.delete()  # 입력된 명령 제거

    @commands.command()
    async def userpoint(self, ctx, name):
        """
        해당 사용자의 현재 포인트를 확인
        입력한 사용자의 디스코드 포인트를 확인한다.
        """
        text = self.engine.getPoint(name)
        await ctx.send(text)
        await ctx.message.delete()  # 입력된 명령 제거

    async def dailyCheck(self, message):
        name = message.author.name
        text = self.engine.dailyCheck(name)
        if text is not None and name != 'testbot':
            msg = await message.channel.send(text)
            await asyncio.sleep(10)
            await msg.delete()  # 메세지 삭제
