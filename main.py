from discordBot import MyBot
from discordBot_token import discord_token
from Log.infoLog import logger as log

token = discord_token

if __name__ == '__main__':
    client = MyBot()

    @client.event
    async def on_ready():
        log.info('Logged in as {0} ({0.id})'.format(client.user))
        log.debug('test11')

    client.run(discord_token)
