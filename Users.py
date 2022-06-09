import nextcord
from nextcord.ext import commands
from User import User

import util

class Users():

    def __init__(self, bot : commands.Bot):

        self.users = {}
        self.bot = bot

    def add_user(self, member : nextcord.Member):

        self.users[member.id] = User(self.bot)

    def get_text_messages(self, id):
        return self.users[id]

    def update_text_messages(self, id, txt):
        self.users[id] = txt

    def has_messages(self, id):
        return id in self.users