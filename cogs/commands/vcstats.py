import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from util import TEST_SERVER_ID, get_mongo

class VCStats(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name='vcstats', guild_ids=[TEST_SERVER_ID])
    async def vcstats(self, interaction: Interaction):
        return


def setup(bot : commands.Bot):
    bot.add_cog(VCStats(bot))