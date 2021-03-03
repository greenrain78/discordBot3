import asyncio
from discord.ext import commands
from Log.infoLog import logger as log
from Point.point_engine import PointEngine
from Settings import superuser


class PointBot(commands.Cog):
    """
    포인트 봇
    디스코드 포인트 조회및 출석채크 기능을 담당하는 봇이다.
    """

    def __init__(self, bot):
        self.bot = bot
        self.engine = PointEngine()

    @commands.command()
    async def point(self, ctx):
        """
        디코 포인트 이벤트 정보 확인
        디스코드 포인트 이벤트에 대한 정보를 확인한다.
        """
        try:
            em = self.engine.eventInfo()

            msg = await ctx.send(embed=em)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")

    @commands.command()
    async def mypoint(self, ctx):
        """
        내 점수 확인
        현재 내가 보유중인 디스코드 포인트를 확인한다.
        """
        try:
            user = ctx.author.name
            text = self.engine.getPoint(user)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제

        except Exception as e:
            log.exception("command botState error")

    @commands.command()
    async def mylist(self, ctx):
        """
        내 점수 리스트 확인
        최근 포인트 획득 리스트를 확인한다.
        """
        try:
            user = ctx.author.name
            text = self.engine.getPointList(user)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제

        except Exception as e:
            log.exception("command botState error")

    @commands.command()
    async def userpoint(self, ctx, name):
        """
        해당 사용자의 현재 포인트를 확인
        입력한 사용자의 디스코드 포인트를 확인한다.
        """
        try:
            text = self.engine.getPoint(name)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")

    @commands.command()
    async def givepoint(self, ctx, user, point):
        """
        해당 사용자의 포인트를 갱신한다.
        주어진 포인트 만큼 사용자의 포인트를 감소하거나 증가시킨다.
        """
        try:
            name = ctx.message.author.name
            if name == superuser:
                pt = int(point)
                text = self.engine.givePoint(user, pt)

                msg = await ctx.send(text)
                await asyncio.sleep(60)

                await ctx.message.delete()  # 입력된 명령 제거
                await msg.delete()  # 메세지 삭제
            else:
                text = '허용되지 않은 사용자 입니다.'
                msg = await ctx.send(text)
                await asyncio.sleep(60)

                await ctx.message.delete()  # 입력된 명령 제거
                await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")

    async def dailyCheck(self, message):
        try:
            name = message.author.name
            text = self.engine.dailyCheck(name)
            if text is not None and name != 'testbot':
                msg = await message.channel.send(text)
                await asyncio.sleep(10)
                await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")
