from discordBot import MyBot

discord_token = "NzgxNTI0MjMwNTI0ODk1MjQy.X7-5KA.xA_8OfdbxwIWCzz8CS2IVRZpiqI"

if __name__ == '__main__':
    client = MyBot()

    @client.event
    async def on_ready():
        print('Logged in as {0} ({0.id})'.format(client.user))
        print('-------------------------------------------')

    client.run(discord_token)
