import discord
from rules import should_notify
from notifier import send_notification
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if should_notify(message.content):
        send_notification(
            message.content,
            message.author.name,
            message.channel.name
        )

client.run(os.getenv("DISCORD_TOKEN"))
