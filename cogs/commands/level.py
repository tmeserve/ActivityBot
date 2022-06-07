import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from util import TEST_SERVER_ID


class Level(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot

def setup(bot : commands.Bot):
    bot.add_cog(Level(bot))