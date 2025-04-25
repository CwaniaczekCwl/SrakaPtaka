import discord
import os
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)

colors = [
    0xff0000, 0xff3300, 0xff6600, 0xff9900, 0xffcc00,
    0xffff00, 0xccff00, 0x99ff00, 0x66ff00, 0x33ff00,
    0x00ff00, 0x00ff33, 0x00ff66, 0x00ff99, 0x00ffcc,
    0x00ffff, 0x00ccff, 0x0099ff, 0x0066ff, 0x0033ff,
    0x0000ff, 0x3300ff, 0x6600ff, 0x9900ff, 0xcc00ff,
    0xff00ff, 0xff00cc, 0xff0099, 0xff0066, 0xff0033
]

running = True

async def change_role_color():
    await client.wait_until_ready()
    guild_id = int(os.getenv("GUILD_ID"))
    role_id = int(os.getenv("ROLE_ID"))

    guild = client.get_guild(guild_id)
    role = guild.get_role(role_id)

    i = 0
    while running:
        color = colors[i % len(colors)]
        await role.edit(colour=discord.Colour(color))
        i += 1
        await asyncio.sleep(4.0)  

@client.event
async def on_ready():
    print(f"✅ Zalogowano jako {client.user}")
    client.loop.create_task(change_role_color())

client.run(os.getenv("TOKEN"))
