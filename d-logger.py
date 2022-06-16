#Made on Manjaro Linux and made for use in linux terminals. 
#You may neeed to change some things if you are on windows as I have not tested it on windows. 
#I assume it will be the same, maybe without fancy colors. idk.

import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import datetime
import asyncio
import io


BOT_Prefix=("d.", "D.")
client = commands.Bot(command_prefix=BOT_Prefix)
client.remove_command("help")


@client.command()
async def help(ctx):
    author = ctx.message.author


    helpembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    helpembed.set_author(name="Help")
    helpembed.add_field(name="d.ping", value = "Standard ping pong command", inline=False)
    await ctx.send(embed=helpembed)


print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + " attempting to establish connection to the client")


@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://twitch.tv/Monstercat",
                                 name=f"d.help | in {len(client.guilds)} guilds!") #This is the bots status. You can edit what this says between the " " 
    await client.change_presence(status=discord.Status.online, activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established, logged in as: " + client.user.name)


@client.event
async def on_guild_join(guild):
    print(f"I was invited to and have joined {guild}!")


#Logging This is the meat and potatoes :)
image_types = ["png", "jpeg", "gif", "jpg", "mp4", "mov"] #You can add more attachments/formats here to be saved.
@client.event
async def on_message(message: discord.Message):
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            await attachment.save(f'attachments/{attachment.filename}') # 'attachments/{{attachment.filename}' is the PATH to where the attachmets/images will be saved. Example: home/you/Desktop/attachments/{{attachment.filename}
            print(Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + f'Attachment {attachment.filename} has been saved to directory/folder > attachments.')
    else:
        with io.open("logs.txt", "a", encoding="utf-8") as f: #if logs.txt doesn't exist, it will create it and write to it.
            f.write(
                f"[{message.guild}] | [{message.channel}] | [{message.author}] @ {message.created_at}: {message.content}\n")
            f.close()
    print(
        Fore.WHITE + "[" + Fore.LIGHTRED_EX + '+' + Fore.WHITE + "]" + Fore.LIGHTRED_EX + f"[{message.guild}] | [{message.channel}] | [{message.author}] @ {message.created_at}: {message.content}")
                
    await client.process_commands(message)



@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")


#https://discordapp.com/oauth2/authorize?client_id=BOT_ID_HERE&scope=bot&permissions=8" permissions=8 = Admin Permissions in servers. (this can be edited to just read and send messages.) Although you won't save text or images in staff channels/private channels that admins can access.
@client.command()
async def invite(ctx):
    author = ctx.message.author


    invembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    invembed.set_author(name="Add me")
    invembed.add_field(name="My Invite Link", value = "[Invite](https://discordapp.com/oauth2/authorize?client_id=BOT_ID_HERE&scope=bot&permissions=8)", inline=False)
    await ctx.send(embed=invembed)

client.run('BOT_TOKEN_HERE')
