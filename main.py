import discord
import os
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)

colors = [
    0xff0000, 0xff1a00, 0xff3300, 0xff4d00, 0xff6600, 0xff8000, 0xff9900,
    0xffb200, 0xffcc00, 0xffe500, 0xffff00, 0xe5ff00, 0xccff00, 0xb2ff00,
    0x99ff00, 0x80ff00, 0x66ff00, 0x4dff00, 0x33ff00, 0x1aff00, 0x00ff00,
    0x00ff1a, 0x00ff33, 0x00ff4d, 0x00ff66, 0x00ff80, 0x00ff99, 0x00ffb2,
    0x00ffcc, 0x00ffe5, 0x00ffff, 0x00e5ff, 0x00ccff, 0x00b2ff, 0x0099ff,
    0x0080ff, 0x0066ff, 0x004dff, 0x0033ff, 0x001aff, 0x0000ff, 0x1a00ff,
    0x3300ff, 0x4d00ff, 0x6600ff, 0x8000ff, 0x9900ff, 0xb200ff, 0xcc00ff,
    0xe500ff, 0xff00ff, 0xff00e5, 0xff00cc, 0xff00b2, 0xff0099, 0xff0080,
    0xff0066, 0xff004d, 0xff0033, 0xff001a
]

running = True

async def change_role_color():
    await client.wait_until_ready()
    guild_id = int(os.getenv("GUILD_ID"))
    role_id = int(os.getenv("ROLE_ID"))

    guild = client.get_guild(guild_id)
    role = guild.get_role(role_id)

    if not role:
        print("❌ Nie znaleziono roli! Sprawdź ROLE_ID i czy bot ma dostęp.")
        return

    print(f"🎨 Zmieniam kolory roli: {role.name} co 0.7s")

    i = 0
    while running:
        try:
            color = colors[i % len(colors)]
            await role.edit(colour=discord.Colour(color))
            print(f"✅ Zmieniono kolor na: #{hex(color)[2:].zfill(6)}")
            i += 1
            await asyncio.sleep(0.7)
        except Exception as e:
            print(f"❌ Błąd: {e}")
            await asyncio.sleep(2)

@client.event
async def on_ready():
    print(f"🚀 Zalogowano jako {client.user}")
    client.loop.create_task(change_role_color())

client.run(os.getenv("TOKEN"))
