import discord, os
import customWords
from discord import app_commands as commands
from messageGenerator import generateMessage


if not os.path.isdir("ServerWordLists"):
    os.mkdir("ServerWordLists")

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
@commands.describe(amount="The number of Classpects to generate. (Max = 16)",
                    mode="Determines how the classpects are generated.",
                    farragofiction="Determines whether or not Farragofiction classes and aspects are considered canon. (Has no effect on Chaos Mode)",
                    minimum="Determines the minimum size of each word.",
                    maximum="Determines the maximum size of each word.",
                    custom="Determines whether the words from the server's custom words list is used.",
                    explicit="Determines whether explicit words are used.")
@commands.choices(
        mode=[
        commands.Choice(name="Chaos", value=0),
        commands.Choice(name="Swap", value=1),
        commands.Choice(name="Semi-Canon", value=2),
        commands.Choice(name="Semi-Canon (Class)", value=4),
        commands.Choice(name="Semi-Canon (Aspect)", value=5),
        commands.Choice(name="Canon", value=3),
        ],
        farragofiction=[
        commands.Choice(name="True", value=1),
        commands.Choice(name="False", value=0),],
        custom=[
        commands.Choice(name="Both", value=2),
        commands.Choice(name="Custom only", value=1),
        commands.Choice(name="Main only", value=0),],
        explicit=[
        commands.Choice(name="True", value=1),
        commands.Choice(name="False", value=0),],
        )

async def ClasspectsCommand(interaction, amount:int=4, mode:int=1,farragofiction:int=0, minimum:int=3, maximum:int=50, custom:int=2, explicit:int=1):
    message = generateMessage(interaction,amount,mode,farragofiction,minimum,maximum,custom,explicit)
    await interaction.response.send_message(message)

#@tree.command(name = "addcustomwords", description = "Add words to the server's custom words list.", guild=discord.Object(id=SERVERID))
#@commands.describe(amount="The words to add to the list. Seperate each word with a comma and preface words with a ~tilde to mark them as explicit.",)
#async def ClasspectsCommand(interaction, words:str=""):
#    pass

@client.event
async def on_ready():
    print("bot online")
    await tree.sync(guild=discord.Object(id=SERVERID))
    print(client.user)



client.run(token)