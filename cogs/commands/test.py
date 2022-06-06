from cgi import test
from code import interact
import nextcord
from nextcord.ext import commands
from nextcord import Interaction


test_server_id = 983197438959571014

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

        
        print('loaded')

    @nextcord.slash_command(name='testing', description='test commands', guild_ids=[test_server_id])
    async def testing(self, interaction : Interaction):
        await interaction.response.send_message('Test')


def setup(client):
    client.add_cog(Test(client))