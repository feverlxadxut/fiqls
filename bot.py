import disnake
import os

from pathlib import Path
from configure import TOKEN, PREFIX #configure.example.py
from disnake.ext import commands

client = commands.Bot(
    command_prefix = PREFIX,
    intents = disnake.Intents.all()
)
cwd = Path(__file__).parents[0]
cwd = str(cwd)

@client.event
async def on_ready():
    print('Бот запущен')

def _load_Cogs(): # Подгрузка когов
    for filename in os.listdir(cwd + "/cogs"):
        if not filename.startswith("_"):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
            else:
                client.load_extension(f'cogs.{filename}')

if __name__ == "__main__":
    _load_Cogs()
    client.run(TOKEN)