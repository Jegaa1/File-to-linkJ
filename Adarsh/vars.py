# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', "1923471"))
    API_HASH = str(getenv('API_HASH', "fcdc178451cd234e63faefd38895c991"))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "6513982809:AAEWCacRjj6Br4msVjdMBNePOFsOvuYeteA"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1001814192750"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "880087645").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "JAsuran2p0"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://video:video@cluster0.gp0rn.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'tnshort.net')
    SHORTLINK_API = getenv('SHORTLINK_API', '003db0d0a2e56943b93dc0abd80e1260a17166c8')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://telegram.me/demoshort')
