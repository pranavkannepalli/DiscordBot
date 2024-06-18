from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, app_commands, Interaction
import webserver
from responses import authwithtoken_response, gettodos_response, remove_todo, numtodos_response, add_todo

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

tree = app_commands.CommandTree(client)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = "hello there!"
        await message.author.send(response) if is_private else await message.channel.send(response)
    except BaseException as e:
        print(e)

@client.event
async def on_ready() -> None:
    await tree.sync()
    print(f'{client.user} is now running')

@tree.command(name = "authwithtoken", description="Starts your process by associating this channel with a unique token")
@app_commands.describe(token="Supply your user token or group name")
async def authwithtoken(interaction:Interaction, token: str) -> None:
    response = authwithtoken_response(interaction.guild_id, interaction.channel, token)
    await interaction.response.send_message(response)

@tree.command(name = "todos", description="Gets your todos from firebase")
async def todos(interaction:Interaction) -> None:
    response = gettodos_response(interaction.guild_id, interaction.channel)
    await interaction.response.send_message(response)

@tree.command(name = "removetodo", description="Starts your process by associating this channel with a unique token")
@app_commands.describe(id="The numeric id associated with the todo you are trying to delete")
async def removetodo(interaction:Interaction, id: int) -> None:
    response = remove_todo(interaction.guild_id, interaction.channel, id)
    await interaction.response.send_message(response)

@tree.command(name="numtodos", description="Gets the number of todos ever created in this group.")
async def numtodos(interaction:Interaction) -> None:
    response = numtodos_response(interaction.guild_id, interaction.channel)
    await interaction.response.send_message(response)

@tree.command(name="addtodo", description="Add a todo to the group.")
@app_commands.describe(description="The name of the todo that you are trying to add.")
async def addtodo(interaction: Interaction, description: str) -> None:
    response = add_todo(interaction.guild_id, interaction.channel, interaction.user.display_name, description)
    await interaction.response.send_message(response)

def main() -> None:
    client.run(token=TOKEN)

webserver.keep_alive()
main()
