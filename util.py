import os, discord, json
from pymongo import MongoClient

secrets, config, roles = None, None, None

def load_secrets():
    global secrets
    secrets = json.load(open('./configs/secrets.json'))

    return secrets

def load_config():
    global config
    config = json.load(open('./configs/config.json'))

    return config

def load_roles():
    global roles
    roles = json.load(open('./configs/roles.json'))

    return roles

def get_secrets():
    return secrets

def get_config():
    return config

def get_roles():
    return roles

TEST_SERVER_ID = 983197438959571014

mongoClient : MongoClient

def set_mongo(mongo):
    global mongoClient
    mongoClient = mongo

def get_mongo():
    return mongoClient