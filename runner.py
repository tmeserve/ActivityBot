import util, os, logger
import sys

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from pymongo import MongoClient

secrets = util.load_secrets()
db_secrets = secrets['database']
IP = db_secrets['IP']
username = db_secrets['username']
password = db_secrets['password']
# db_string = f'mongodb+srv://{username}:{password}@{IP}'
db_string = f'mongodb://{username}:{password}@{IP}'

client = MongoClient(db_string)
util.set_mongo(client)

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('ready')

initial_extensions = []

def load_cogs(dir):
    for filename in os.listdir(f'{dir}'):
        if os.path.isdir(f'./{dir}/{filename}'):
            load_cogs(dir + f'/{filename}')
        if filename.endswith('py'):
            initial_extensions.append(f'cogs.{filename[:-3]}')\


if __name__ == '__main__':
    load_cogs('./cogs')
    for extension in initial_extensions:
        print(extension)
        bot.load_extension(extension)

    bot.run(secrets['discord']['token'])
