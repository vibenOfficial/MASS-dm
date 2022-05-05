#dependencies
import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import asyncio

#config
token = "token" #change this to ur token, https://discord.com/developers/applications
prefix = "." #change this to prefix

#edit this if u know what ur doing
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"Logged in as {client.user.name}")

#command
@client.command(name="send")
async def send(ctx, arg1='', *, arg2=''):
 if ctx.channel.id == 123456789: #change this to ur channel ID
  member_count = 0
  for member in ctx.guild.members:
   member_count += 1
  await ctx.send(f":white_check_mark: MASS-DM Started. Total Members: `{member_count}` Members.")
  for member in ctx.guild.members:
   if member == client.user or member.bot == True:
    member_count -= 1
    pass
   else:
    try:
	    await member.send(f"**{arg2}**\n<#{arg1}>\n<@{member.id}>")
	    await asyncio.sleep(int("1")) #might crash if less than one
    except discord.errors.Forbidden:
	    member_count -= 1
	    pass
    except commands.CommandInvokeError:
	    member_count -= 1
	    pass
        
  await ctx.send(f":white_check_mark: MASS-DM Finished. Total DMed: `{member_count}` Members.")
  return
 else:
  await ctx.send(":x: You do not have permissions to use this.")

client.run(token) # login with token
