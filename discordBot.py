from discord.ext import commands

from ERBS.erbs_bot import ERBSBot
# from Music.msuic_bot import MusicBot
from Point.point_bot import PointBot
from Basic.basic_bot import BasicBot


class MyBot(commands.Bot):

    def __init__(self):
        prefix = commands.when_mentioned_or("$")
        desc = 'GreenRain discord bot 3'
        super(MyBot, self).__init__(command_prefix=prefix, description=desc)

        # create bot
        self.pointBot = PointBot(self)
        self.erbsBot = ERBSBot(self)
        self.basicBot = BasicBot(self, pointBot=self.pointBot, erbsBot=self.erbsBot)

        # add bot
        self.add_cog(self.pointBot)
        self.add_cog(self.erbsBot)
        self.add_cog(self.basicBot)

    async def on_message(self, message):
        print('{0.author}: {0.content}'.format(message))
        await self.pointBot.dailyCheck(message)
        await super(MyBot, self).on_message(message)
