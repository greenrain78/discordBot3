from discordBot import MyBot
from discordBot_token import discord_token

token = discord_token

if __name__ == '__main__':
    client = MyBot()

    @client.event
    async def on_ready():
        print('Logged in as {0} ({0.id})'.format(client.user))
        print('-------------------------------------------')

    client.run(discord_token)
