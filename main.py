import discord
import os
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

client = discord.Client(intents=intents)

colors = [
    0xFF0000,  # czerwony
    0xFF7F00,  # pomarańczowy
    0xFFFF00,  # żółty
    0x00FF00,  # zielony
    0x0000FF,  # niebieski
    0x4B0082,  # indygo
    0x8B00FF   # fioletowy
]

running = True

async def change_role_color():
    await client.wait_until_ready()
    guild_id = int(os.getenv("GUILD_ID"))
    role_id = int(os.getenv("ROLE_ID"))

    guild = client.get_guild(guild_id)
    role = guild.get_role(role_id)

    while running:
        color = random.choice(colors)
        await role.edit(colour=discord.Colour(color))
        await asyncio.sleep(5)  # zmiana koloru co 5 sekund

@client.event
async def on_ready():
    print(f"✅ Zalogowano jako {client.user}")
    client.loop.create_task(change_role_color())

client.run(os.getenv("TOKEN"))
