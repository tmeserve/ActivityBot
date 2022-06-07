import util

DATABASE = util.get_secrets()['database']['database']
EXP_COLLECTION = util.get_secrets()['database']['experience_collection']
LOG_COLLECTION = util.get_secrets()['database']['log_collection']