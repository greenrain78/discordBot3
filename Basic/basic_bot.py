import asyncio
from discord.ext import commands
from Log.infoLog import logger as log
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
        try:
            name = ctx.message.author.name
            if name == '김대원':
                text = self.engine.getState()
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

    @commands.command()
    async def github(self, ctx):
        """
        디코 봇 깃허브 링크
        """
        try:
            text = 'https://github.com/greenrain78/discordBot3'
            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command github error")
