from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import webserver

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably');
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        print(response)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except BaseException as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')
0000
@client.event
async def on_message(message: Message) -> None:
    if(message.author == client.user):
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    print('tried sending message')

def main() -> None:
    client.run(token=TOKEN)

webserver.keep_alive()
main()