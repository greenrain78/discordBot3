import asyncio
from discord.ext import commands
from Log.infoLog import logger as log
from Game import game_engine as engine
from Point import user_DB


class GameBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def game(self, ctx, point, game_name, *args):
        """
        게임
        1. 홀짝 게임
        0~99사이의 랜덤한 숫자가 생기는데 해당 숫자가 홀인지 짝인지 맞추는 게임
        2. 동전 게임
        동전을 던지는데 동전이 앞면인지 뒷면인지 맞추는 게임
        """
        try:
            user = ctx.author.name
            try:
                pt = int(point)
                mypoint = user_DB.get_point(user)
                if pt < 0 or mypoint < pt:
                    text = f"{user}님 보유 포인트가 부족합니다.\n" \
                           f"입력하신 포인트: {pt}, 보유 포인트: {mypoint}"

                elif game_name == "홀짝":
                    text = engine.odd_even(user, pt, args)
                    user_DB.update_user_game_count(user)
                elif game_name == "동전":
                    text = engine.coin(user, pt, args)
                    user_DB.update_user_game_count(user)
                else:
                    text = "해당 게임이 존재하지 않습니다."

            except ValueError:
                text = f'{point}는 숫자가 아닙니다.'

            msg = await ctx.send(text)
            await asyncio.sleep(60)

            await ctx.message.delete()  # 입력된 명령 제거
            await msg.delete()  # 메세지 삭제
        except Exception as e:
            log.exception("command botState error")
