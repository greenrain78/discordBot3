import asyncio
from discord.ext import commands
from Log.infoLog import logger as log
from Stock.stock_engine import StockEngine


class StockBot(commands.Cog):
    """
    주식 봇
    디스코드 포인트 주식을 매수 매도할 수 있는 봇
    """

    def __init__(self, bot):
        self.bot = bot
        self.engine = StockEngine()

    @commands.command()
    async def mystock(self, ctx):
        """
        현재 내가 보유한 주식을 보여준다.
        """
        try:
            user = ctx.author.name
            text = self.engine.getStock(user)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제

        except Exception as e:
                log.exception("command botState error")

    @commands.command()
    async def findstock(self, ctx, code):
        """
        해당 주식코드의 주식 정보를 보여준다.
        """
        try:

            text = self.engine.findStock(code)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제

        except Exception as e:
            log.exception("command botState error")

    @commands.command()
    async def searchstock(self, ctx, name):
        """
        주식 종목 코드를 검색한다.
        """
        try:

            text = self.engine.searchstock(name)

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제

        except Exception as e:
            log.exception("command botState error")



