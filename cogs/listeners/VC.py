import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from util import TEST_SERVER_ID, get_mongo


class VC(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.client = get_mongo()
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member : nextcord.Member, before : nextcord.VoiceState, after  : nextcord.VoiceState):
        if before.channel is None and after.channel is not None:
            print('joined vc')
        elif before.channel is not None and after.channel is None:
            print('left vc')
        

def setup(bot : commands.Bot):
    bot.add_cog(VC(bot))