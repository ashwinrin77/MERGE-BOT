import os


class Config(object):
    API_HASH = os.environ.get("0b691c3e86603a7e34aae0b5927d725a")
    BOT_TOKEN = os.environ.get("7131780378:AAGLnkSYqVlksEGUR9oBnURwKZyOdlLEnrU")
    TELEGRAM_API = os.environ["25695562"]
    OWNER = os.environ.get("5088091585")
    OWNER_USERNAME = os.environ.get("@Fbrbhsvsc")
    PASSWORD = os.environ.get("boruto")
    DATABASE_URL = os.environ.get("mongodb+srv://haribotx:haribotx@cluster0.i3skil4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002001392004")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("14z9n5jPgc3mr-qv9leAfjXCkhU_vDM7t")
    USER_SESSION_STRING = os.environ.get("BABjxmKpuUjsTZywrQaUn9Dbv-K8S3vNsMBkFHtGD3iD5A33Ehyfh2jv_6Ui0yf_UAM6hmiFGpS805QPcYJwU5yCbKOhrPM6lUsAXeacmyqxlhtHRfP_rOGPQWQ_g9tc9RgdRq9L6Y1CJGC9tok0FXYbhbpcrqNX9lPPhaAoUAO-y2X_4kVqdBYvtW7VBuhBbqmf-yxulQRT4O2ZoYEZGKWisp7e4w_3iIHXQrnbe-cjipvUVW3Hk5DFzo1WPw3jrZyxiL00sIQIgycb15CemQI_HuoJCf6IN1OP3pZj89t05Ijh6V0yLH4h2-cs7j2c4dSMRKvRnJ_JJ3LpqBRXoVKkAAAAAS_eymEA", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
