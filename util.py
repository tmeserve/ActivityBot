import os, discord, json
from pymongo import MongoClient

def load_secrets():
    f = open('secrets.json')

    file = json.load(f)

    return file


TEST_SERVER_ID = 983197438959571014

mongoClient : MongoClient

def set_mongo(mongo):
    mongoClient = mongo

def get_mongo():
    return mongoClient