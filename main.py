from discordBot import MyBot
from discordBot_token import discord_token
from Log.infoLog import logger as log

token = discord_token

if __name__ == '__main__':
    log.info('start programe')
    client = MyBot()

    @client.event
    async def on_ready():
        log.info('Logged in as {0} ({0.id})'.format(client.user))

    client.run(discord_token)
