import discord
import asyncio

token = ""
client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print("dont let skids get money for gc spamming u")
    print(f"GroupChannel leaver is now activating on {client.user} ...")
    await asyncio.sleep(5)
    for gc in client.private_channels:
        if isinstance(gc, discord.GroupChannel):
            try:
                await gc.leave()
                print(f'Successfull: {gc.name}')
            except:
                print(f'Failed: {gc.name}')
    print(f"GroupChannel leaver has finished! Thanks you're master Tacs!")
    print(f"just close this now < 3")

client.run(token, bot=False)
