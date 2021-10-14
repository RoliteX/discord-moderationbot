import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix='-')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='-help'))
    print("I'm Ready!")

@Bot.command()
# @commands.has_role("Admin") --> Only 'Admin' Use this command
async def kick(ctx, member:discord.Member, *args, reason="X"):
    await member.kick(reason=reason)
    await ctx.send(f'Consider it done!')

@Bot.command()
# @commands.has_role("Admin") --> Only 'Admin' Use this command
async def ban(ctx, member:discord.Member, *args, reason="X"):
    await member.ban(reason=reason)
    await ctx.send(f'Consider it done!')

@Bot.command()
# @commands.has_role("Admin") --> Only 'Admin' Use this command
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'You are forgiven this time {user.mention}')
            return

Bot.run() # Bot.run(Discord Bot Token)