from discord.ext import commands

from Chat.chat_bot import ChatBot
from ERBS.erbs_bot import ERBSBot
# from Music.music_bot import MusicBot
from Game.game_bot import GameBot
from Point.point_bot import PointBot
from Basic.basic_bot import BasicBot
from Log.infoLog import logger as log
from Settings import debug


class MyBot(commands.Bot):

    def __init__(self):
        if not debug:
            prefix = commands.when_mentioned_or("$")
        else:
            prefix = commands.when_mentioned_or("!")

        desc = 'GreenRain discord bot 3'
        super(MyBot, self).__init__(command_prefix=prefix, description=desc)

        # create bot
        self.pointBot = PointBot(self)
        self.erbsBot = ERBSBot(self)
        self.basicBot = BasicBot(self, pointBot=self.pointBot, erbsBot=self.erbsBot)
        self.gameBot = GameBot(self)
        self.chatBot = ChatBot(self)

        # add bot
        self.add_cog(self.pointBot)
        self.add_cog(self.erbsBot)
        self.add_cog(self.basicBot)
        self.add_cog(self.gameBot)
        self.add_cog(self.chatBot)

    async def on_message(self, message):
        log.info('{0.author}: {0.content}'.format(message))
        await self.chatBot.checkBlock(message)

        await super(MyBot, self).on_message(message)
        await self.pointBot.dailyCheck(message)
