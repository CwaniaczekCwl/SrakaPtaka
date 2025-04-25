import discord
import os
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.members = True  
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

async def change_role_color():
    await client.wait_until_ready()
    guild_id = int(os.getenv("GUILD_ID"))
    role_id = int(os.getenv("ROLE_ID"))

    guild = client.get_guild(guild_id)
    role = guild.get_role(role_id)

    if not guild or not role:
        print("❌ Nie znaleziono roli! Sprawdź ROLE_ID i czy bot ma dostęp.")
        return

    i = 0
    while not client.is_closed():
        try:
            color = colors[i % len(colors)]
            print(f"🔁 Próba zmiany koloru na: #{hex(color)[2:].zfill(6)}")
            await role.edit(colour=discord.Colour(color), reason="Rainbow effect")
            print(f"✅ Zmieniono kolor!")
            i += 1
        except discord.errors.HTTPException as e:
            print(f"⚠️ Rate limit lub błąd HTTP: {e}")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"❌ Inny błąd: {e}")
            await asyncio.sleep(3)
        await asyncio.sleep(1.2)  

async def restart_loop_every(minutes):
    while not client.is_closed():
        await change_role_color()
        print(f"🔄 Restart pętli po {minutes} minutach...")
        await asyncio.sleep(minutes * 60)

@client.event
async def on_ready():
    print(f"✅ Zalogowano jako {client.user}")
    client.loop.create_task(restart_loop_every(10))  

client.run(os.getenv("TOKEN"))
