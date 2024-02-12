import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21215289))

    API_HASH = os.environ.get("API_HASH", "be3dc2d90973c1caebbdfd68d82792e6")
