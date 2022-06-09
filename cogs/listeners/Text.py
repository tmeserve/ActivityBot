import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from datetime import datetime

from util import TEST_SERVER_ID, get_users


class Text(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        print('Loaded Text Cog')

    @commands.Cog.listener()
    async def on_message(self, message : nextcord.Message):
        users = get_users()
        if users.has_messages(message.author.id):
            txt = users.get_text_messages(message.author.id)
            txt.add_message(message, datetime.now())
            # users.update_text_messages(message.author.id, txt)
        else:
            users.add_user(message.author)
            users.get_text_messages(message.author.id).add_message(message, datetime.now())
            

def setup(bot : commands.Bot):
    bot.add_cog(Text(bot))