from datetime import datetime

import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from util import TEST_SERVER_ID, get_mongo
import constants


class VC(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.client = get_mongo()
        self.db = self.client[constants.DATABASE]
        self.exp_collection = self.db[constants.EXP_COLLECTION]
        self.log_collection = self.db[constants.LOG_COLLECTION]

    def calculate_total_time_in_hours(self, time_in, time_out):
        dt_time_in = datetime.strptime(time_in)
        dt_time_out = datetime.strptime(time_out)


    def afk(self, member : nextcord.Member, before : nextcord.VoiceState or nextcord.StageChannel, after : nextcord.VoiceState or nextcord.StageChannel, time):
        if before.afk and not after.afk:
            self.begin_time(member, time)
            return True
        elif not before.afk and after.afk:
            self.end_time(member, time)
            return True
        elif not before.afk and not after.afk:
            return

    def begin_time(self, member : nextcord.Member, time):
        log_dict = {
            'uuid': member.id,
            'guild_uuid': member.guild.id,
            'time_in': time,
            'time_out': ''
        }
        res = self.log_collection.insert_one(log_dict)
        print(res.acknowledged)

        for record in self.log_collection.find():
            print(record)

    def end_time(self, member : nextcord.Member, time):
        query = {
            'uuid': member.id,
            'guild_uuid': member.guild.id
        }
        log_doc = self.log_collection.find_one(query)
        time_in = log_doc['time_in']

        dt_time_in = datetime.strptime(time_in, '%Y/%m/%d %H:%M:%S')
        dt_time_out = datetime.strptime(time, '%Y/%m/%d %H:%M:%S')

        dt_total_time = dt_time_out - dt_time_in

        print(dt_total_time)

        # total_time = dt_total_time.total_hours()
        # print(total_time, dt_time_in.total_seconds())
    

    @commands.Cog.listener()
    async def on_voice_state_update(self, member : nextcord.Member, before : nextcord.VoiceState or nextcord.StageChannel, after  : nextcord.VoiceState or nextcord.StageChannel):
        time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print('vc update')
        print(before.channel, 'before channe;')
        print('')
        if before.channel is None and after.channel is not None:
            print('joined vc')
            val = self.afk(member, before, after, time)
            if val is None:
                print('val is none')
                self.begin_time(member, time)
        elif before.channel is not None and after.channel is None:
            print('left vc')
            val = self.afk(member, before, after, time)
            if val is None:
                self.end_time(member, time)
        elif before.channel is not None and after.channel is not None:
            print('switched vc')
            val = self.afk(member, before, after, time)

def setup(bot : commands.Bot):
    bot.add_cog(VC(bot))