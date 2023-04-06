# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(17983098)
    API_HASH = str("ee28199396e0925f1f44d945ac174f64")
    BOT_TOKEN = str("5848326557:AAFWQc5chBlpdqNvjJHyUTTOksahsV7zMVg")
    SESSION_NAME = str(getenv('SESSION_NAME', 'Moksh_b658'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(-1001230414925)
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('https://8080-cs-3b90c593-edc4-48ef-9fa4-60ca78365fe3.cs-europe-west1-xedi.cloudshell.dev/', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '797848243'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split()))
