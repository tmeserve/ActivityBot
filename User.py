import nextcord
from nextcord.ext import commands

class User():

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.messages = []
        # only tracks the last 20 messages
        # {
        #     'uuid': [['msg', 'time']]
        # }

    
    def add_message(self, msg : nextcord.Message, time):
        self.messages.append([msg, time])
        if len(self.messages) > 20:
            self.messages.pop()
