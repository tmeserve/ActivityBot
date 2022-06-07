import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from util import TEST_SERVER_ID, get_mongo
import constants

# Handles creating and deleting members when they leave and join the server
class Handler(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.client = get_mongo()
        self.db = self.client[constants.DATABASE]
        self.exp_collection = self.db[constants.EXP_COLLECTION]
        self.log_collection = self.db[constants.LOG_COLLECTION]
    
    @commands.Cog.listener()
    async def on_member_join(self, member : nextcord.Member):
        new_member_dict = {
            'uuid': member.id,
            'guild_uuid': member.guild.id,
            'vc_lvl': 0,
            'vc_exp': 0,
            'txt_lvl': 0,
            'txt_exp': 0,
            'weekly_vc_lvl': 0,
            'weekly_vc_exp': 0,
            'weekly_txt_lvl': 0,
            'weekly_txt_exp': 0,
            'monthly_vc_lvl': 0,
            'monthly_vc_exp': 0,
            'monthly_txt_lvl': 0,
            'monthly_txt_exp': 0
        }
        self.exp_collection.insert_one(new_member_dict)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member: nextcord.Member):
        query = {'uuid': member.id, 'guild_uuid': member.guild.id}
        self.exp_collection.delete_one(query)


def setup(bot : commands.Bot):
    bot.add_cog(Handler(bot))