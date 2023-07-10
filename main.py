import discord, os
from discord import app_commands as commands
from messageGenerator import generateMessage

SERVERID=1127644789203013782 #Add the guild ids in which the slash command will appear. If it should be in all, remove all arguments named "guild" from this code, but note that it will take some time (up to an hour) to register the command if it's for all guilds.

TOKEN = ""
CURRENT_DIR = os.path.dirname(__file__).replace('\\','/')
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))

with open(PARENT_DIR+"/token.txt") as file:
    token = file.readlines()[0]

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = commands.CommandTree(client)

@tree.command(name = "generateclasspects", description = "Generate a list of up to 16 bogus Classpects.", guild=discord.Object(id=SERVERID))
@commands.describe(amount="The number of Classpects to generate.",
                   mode="Determines how the classpects are generated.",
                   farragofiction="Determines whether or not Farragofiction classes and aspects are considered canon. (Has no effect on Chaos Mode)")
@commands.choices(
        mode=[
        commands.Choice(name="Chaos", value=0),
        commands.Choice(name="Swap", value=1),
        commands.Choice(name="Semi-Canon", value=2),
        commands.Choice(name="Canon", value=3),
        ],
        farragofiction=[
        commands.Choice(name="True", value=1),
        commands.Choice(name="False", value=0),]
        )
async def ClasspectsCommand(interaction, amount:int=4, mode:int=0,farragofiction:int=0):
    message = generateMessage(amount,mode,farragofiction)
    await interaction.response.send_message(message)

@client.event
async def on_ready():
    print("bot online")
    await tree.sync(guild=discord.Object(id=SERVERID))
    print(client.user)



client.run(token)