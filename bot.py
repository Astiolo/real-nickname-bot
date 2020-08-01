import discord
import os
from discord.ext import commands

TOKEN = os.environ.get('TOKEN','000')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command(
	name='rename', 
	description = "Change the nickname of another user", 
	aliases = ['nick','name'],
	pass_context = True)	
async def rename(ctx, user : discord.Member = None, newName = ""):
	#member = get_member(user)
	if user is None:
		await ctx.send("You need to specify a user")
	elif newName == "":
		await ctx.send("You need to specify a nickname")
	elif ctx.message.author.id == user.id:
		await ctx.send("You can't set your own nickname. That's not how nicknames really work!")
	else:
		await user.edit(nick=newName)
		await ctx.send(ctx.message.author.mention + " changed " + str(user.name) + "'s name to " + newName)
		
@bot.command(
	name='pin',
	description = "Pin a message by ID",
	pass_context = True)
async def pin(ctx, id):
	message = await bot.get_message(ctx.message.channel, id)
	await message.pin()
	await ctx.send(ctx.message.author.mention + " pinned a message by " + message.author.mention + ":\n" + message.content)
	
@bot.command(
name='unpin',
description = "Unpin a message by ID",
pass_context = True)
async def unpin(ctx, id):
	message = await bot.get_message(ctx.message.channel, id)
	await message.unpin();
	name = ctx.message.author.name
	await ctx.send(ctx.message.author.mention + " unpinned a message by " + message.author.mention + ":\n" + message.content)

bot.run(TOKEN)
