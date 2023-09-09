import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '9301845'))
API_HASH = environ.get('API_HASH', '563e9fd30b529442b705c7230f766b83')
BOT_TOKEN = environ.get('BOT_TOKEN', "5003449601:AAHRnchyfFt0IjF8qbwEEcSq1IKrlr21asw")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/b6f42af4d20b757b46d73.jpg https://telegra.ph/file/f514edecba0f6c1ef3418.jpg https://telegra.ph//file/797fcafb53479875e2bc7.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/b6f42af4d20b757b46d73.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://tma.tmanetwork.workers.dev/0:/video_2023-08-20_20-06-16_7269498453388052480.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1952992043 5673274527 5348874903 617075060').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '1239432287 995893511 5776009452 800256280 5889499190 1888929837 271569446 2022298525 2133390498 895948033 670243821 1357785245 1029159777 1832414870 770434548 1051274938 1969904986 885441870 840784430 951188986 191699151 2068711372 425971654 1080354939 1148289533 759066469 361025362 758994240 949146503 452975673 805218386 513259287 454529841 787702381 1111889913 1766379598 823907478 872384896 397788965 897585133 805904251 861532284 1281665016 630327024 677722239 1284849502 1952992043 1284849502 629614747 683838230 1780890768 1695649654 1111794097 5658459031 1122452634 1341707984  5392730845 5577950386 1473031828 1496159462 1016448192 1129787761 5403721494 1797231578 1430152534 1167592173 777060241 1098459627 186015909 1647618072 1016448192    1187879249 971038761 789897244 863038066 5165713044 1667890440 2099634127 1364514753 1077601779 635860712 784926990 5166592278 1798281049 1172432790 1358036061 1842919669 780027745 231781988 983081204 798490955 5116561187 1370045189 1642921138 5118756794 962503518 1247470001 5186250277 1786964891 1647618072 5070805488 667602671 6016684290 833358769 519063192 1072045954 669730261 958289313 939586485 1054149700 1056774644 889894743 6622540918 840003023 1915835968 1020798320 1211986540 983081204 1167592173 1152975395 850604359 1250293277 1037770894 1701324217 6039029551 673528576 1836861578 191364114 2093499319 933179043 2053446522 617075060 969099516 6387811014 6133756637 671673389 271569446 807639598 797008174 1374152533 1679299779 1369853499 1340976633 1175740484 705069924 685774810 388370120 469754915 693779352').split()]
auth_channel = environ.get('AUTH_CHANNEL','')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001541584194')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001568999811')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://tmaadda:tmaadda@cluster0.8vqs89z.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Tmamoviesbottt")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#stream feature - @TeamHMT_Bots
STREAM_BIN = environ.get("STREAM_BIN", "-1001870465424") #Log channel/Bin Channel id -100xxxxxxx
STREAM_URL = environ.get("STREAM_URL", "https://tmawebwattch-c1a90dbae517.herokuapp.com/") # https://example.com/ (Your Stream Url)
IS_STREAM = bool(STREAM_BIN and STREAM_URL)
#Use this feature, if you have deployed file to link bot. paste the app url with stream url and add filter bot as admin in bin channel and add id in stream bin

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'gyanilinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '928f016f7d48c35adb6673be0c4f45ff86c10d19')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+Iu9yr6xAiI05OGI1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Tmaadda')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/how_to_use_tmafilesbot/9')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001694472922'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '+Iu9yr6xAiI05OGI1')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
