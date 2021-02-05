import discord
import vimhelp
import load_token


def discord_action():
    # setting Intents
    client = discord.Client()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith(':h') or message.content.startswith(':help'):
            print(message.content)
            help_word = message.content.split()[1]
            vimhelp_result = vimhelp.vimhelp(help_word)[0]
            if len(vimhelp_result) < 2000:
                await message.channel.send("```\n"+vimhelp_result+"```")
    client.run(load_token.load_token())
