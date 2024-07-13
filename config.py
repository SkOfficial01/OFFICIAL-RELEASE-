import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", ""))

OWNER_ID = int(getenv("OWNER_ID", "2107529793"))

BOT_USERNAME = getenv("BOT_USERNAME" , "Alone_Dil_bot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/stkeditz/AAROHIxMUSICv2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LUNACHATTERS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/lunaworld")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFa4q0AaXL5byrFr7AQhUj9Sp9w4vu0YDlrRe2dSy7Mf4-tg4vAOKKh3QpcmUZ3PMIHgh6VGrwB7Q8MHE8ck4JkGlnR6JZEry9Hn-ZuzSxhhxKur3w8-OR5lbAPgv2drOoTZO4hbBQMcE1AfJqFNNrO-oZPt9jZabQOLkWoNrGrAguDDFrdxdj-EGcKy_s2mSZ0wmrhmTUprlEJXFd-XvnqbYpe4665RROjgsMLdUZ0W7vXcei59CWKumojnDxMk1B8Z7PQCqxMNIt9WSNLBFcs0CBHyIbnkAWQOtDsOmo3wV9xUqM8KbINrHuiUSReP2MBdSsPiNt2M9X5kpIrhl_aVFGwAAAAGUbTqYAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/e04c3146efe41fc2ad6a0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/e04c3146efe41fc2ad6a0.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
STATS_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/f1d0bab61bcf5f94d5bc6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
