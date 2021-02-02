import asyncio
from discord.ext import commands
from Log.infoLog import logger as log
from Game.game_engine import GameEngine


class GameBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = GameEngine()

    @commands.command()
    async def game(self, ctx, name, *args):
        """
        게임
        1. 홀짝 게임
        """
        try:
            if name == "홀짝":
                text = self.engine.odd_even(args)
            else:
                text = "해당 게임이 존재하지 않습니다."

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")


