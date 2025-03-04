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
API_ID = int(environ.get('API_ID', '8497750'))
API_HASH = environ.get('API_HASH', '91ed92493d470bc610781f12e74a8b0a')
BOT_TOKEN = environ.get('BOT_TOKEN', "5086970136:AAFZry63z3JQVUnECgEO94NDJyk60osF9KQ")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/Dom-12-06-10')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/Dom-12-06-10")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/50e572f32c8cce1aa5fd2.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/Dom-12-06-10")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1952992043 904059063 969099516').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001739510487 -1002130401863').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '1239432287 995893511 5776009452 800256280 5889499190 1888929837 271569446 2022298525 2133390498 895948033 670243821 1357785245 1029159777 1832414870 770434548 1051274938 1969904986 885441870 840784430 951188986 191699151 2068711372 425971654 1080354939 1148289533 759066469 361025362 758994240 949146503 452975673 805218386 513259287 454529841 787702381 1111889913 1766379598 823907478 872384896 397788965 897585133 805904251 861532284 1281665016 630327024 677722239 1284849502 1952992043 1284849502 629614747 683838230 1780890768 1111794097 1122452634 1167592173 1098459627 186015909 1077601779 5070805488 1020798320 1167592173 1152975395 850604359 1250293277 1037770894 1701324217 6039029551 673528576 1836861578 191364114 2093499319 933179043 2053446522 617075060 969099516 671673389 271569446 807639598 1374152533 1679299779 1369853499 1340976633 685774810 469754915 693779352 731875409 460363082 1111794097 811185412 1292413064 1662278949 1206857311 658045819 1893730690 523900329 773970993 900317068 879298863 1148039926 1498152183 648297350 1020207355 1763090891 5673274527 1645981537 6114293827 1825323355 1364514753 1247470001 797008174 1341707984 1271729010 1333593831 642262354 667602671 1496159462 5186250277 5624727031 705069924 5131474018 1682583134 1798281049 5116561187 1627235645 950219823 1535290325 1430152534 840152088 5392730845 816843856 789897244 1187879249 5821582517 1126886042 1060410878 1049950296 5246975098 863038066 6046206694 1172432790 6133756637 949657126 1129787761 798490955 1219040239 1112312657').split()]
auth_channel = environ.get('AUTH_CHANNEL','-1001533657627')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001533657627 ')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002104064120')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
VRFIED_IMG = environ.get("VRFIED_IMG", "https://graph.org/file/9cea98695ef1343e4f627.jpg")
VRFY_IMG = environ.get("VRFY_IMG", "https://graph.org/file/10f9dac6eab3247e35831.jpg")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Manohartech:Manohartech@cluster0.lwo8q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Manohartech")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#stream feature - @TeamHMT_Bots
STREAM_BIN = environ.get("STREAM_BIN", "") #Log channel/Bin Channel id -100xxxxxxx
STREAM_URL = environ.get("STREAM_URL", "") # https://example.com/ (Your Stream Url)
IS_STREAM = bool(STREAM_BIN and STREAM_URL)
#Use this feature, if you have deployed file to link bot. paste the app url with stream url and add filter bot as admin in bin channel and add id in stream bin

# Others
VERIFY = bool(environ.get('VERIFY', False))
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/how_to_use_tmafilesbot')
SPRT_CHNL = environ.get('SPRT_CHNL', 'https://t.me/nenmemeravthaa')
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'gyanilinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '6aa57b9cf2e0491b7c8509e11f0acf57bcb16844')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+nMvXvoVF-wUwYzE1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/nenmemeravthaa')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_To_Solve_Nma')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001794031076'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'nmadiscussion')
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
