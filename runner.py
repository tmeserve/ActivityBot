import util, os, logger
import sys
from Users import Users

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from pymongo import MongoClient
import certifi

secrets = util.load_secrets()
db_secrets = secrets['database']
IP = db_secrets['IP']
username = db_secrets['username']
password = db_secrets['password']
db_string = f'mongodb+srv://{username}:{password}@{IP}'


client = MongoClient(db_string, tlsCAFile=certifi.where())
util.set_mongo(client)

# config = util.load_config()
# roles = util.load_roles()

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('ready')
    util.set_users(Users(bot))

initial_extensions = []

def load_cogs(dir):
    for filename in os.listdir(f'{dir}'):
        if os.path.isdir(f'{dir}/{filename}'):
            # load_cogs(os.path.join(dir, f'/{filename}'))
            load_cogs(dir + f'/{filename}')
        if filename.endswith('py'):
            tmp = dir.replace('/', '.')
            initial_extensions.append(f'{tmp}.{filename[:-3]}')


if __name__ == '__main__':
    
    # load_cogs(os.path.join(f'{os.getcwd()}', 'cogs'))
    load_cogs('cogs')
    for extension in initial_extensions:
        bot.load_extension(extension)

    bot.run(secrets['discord']['token'])
