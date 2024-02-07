# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

chill_first_member, working_first_member = None, None

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_voice_state_update(member, before, after):
    global chill_first_member
    global working_first_member

    # Check if joining the chilling voice channel
    if after.channel and after.channel.id == 1201624719523336295:
        # If no one was in the channel before and this is the first member
        if not before.channel and not chill_first_member:
            chill_first_member = member
            # Get general channel object (replace with channel ID)
            general_channel = client.get_channel(1201624719523336294)
            await general_channel.send(f"{member.name} is chilling in CLP! Join him")
        else:
            # Reset chill_first_member if someone else joins later
            chill_first_member = None
    
    # Check if joining the working voice channel
    if after.channel and after.channel.id == 1201625376825278605:
        # If no one was in the channel before and this is the first member
        if not before.channel and not working_first_member:
            working_first_member = member
            # Get general channel object (replace with channel ID)
            general_channel = client.get_channel(1201624719523336294)
            await general_channel.send(f"{member.name} is working in CLP! Join him.")
        else:
            # Reset working_first_member if someone else joins later
            working_first_member = None


    if before.channel and not after.channel:
        print(f'{member} has left the vc')

client.run(TOKEN)