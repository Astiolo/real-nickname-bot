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
		await bot.say("You need to specify a user")
	elif newName == "":
		await bot.say("You need to specify a nickname")
	elif ctx.message.author.id == user.id:
		await bot.say("You can't set your own nickname. That's not how nicknames really work!")
	else:
		await bot.change_nickname(user, newName)
		name = ctx.message.author.name
		if ctx.message.author.nick != None:
			name = ctx.message.author.nick
		await bot.say(name + " changed " + str(user.name) + "'s name to " + newName)
		
@bot.command(
	name='pin',
	description = "Pin a message by ID",
	pass_context = True)
async def pin(ctx, id):
	message = await bot.get_message(ctx.message.channel, id)
	await bot.pin_message(message)
	name = ctx.message.author.name
	if ctx.message.author.nick != None:
		name = ctx.message.author.nick
	await bot.say(name + " pinned a message: " + message.content)
	
@bot.command(
name='unpin',
description = "Unpin a message by ID",
pass_context = True)
async def unpin(ctx, id):
	message = await bot.get_message(ctx.message.channel, id)
	await bot.unpin_message(message)
	name = ctx.message.author.name
	if ctx.message.author.nick != None:
		name = ctx.message.author.nick
	await bot.say(name + " unpinned a message: " + message.content)
	
@bot.command(
name='ezmark',
description = "Ask for Mark's credit card details")
async def ezmark():
	await bot.say("Hey Mark, I need your credit card details real quick. Type them in here!")

bot.run(TOKEN)