from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("- ابـدا بأستخراج كـود .", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Kembali", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("- السورس .", url="https://t.me/TOPTETO")],
        [
            InlineKeyboardButton("المساعده", callback_data="help"),
            InlineKeyboardButton("- حول البوت .", callback_data="about")
        ],
        [InlineKeyboardButton("- المطور .", url="https://t.me/Usern4meDoesNotExist404")],
    ]

    START = """
📟 ¦ اهلا بـك عزيـزي {0}\n🖱 ¦ يـمكنك استـخـراج الـتـالـي 📥\n📟 ¦ تيرمـكـس تليثون للحسـابـات 🥷\n📡 ¦ تيرمـكـس تليثون للبوتــات 🎭\n🎸 ¦ بايـروجـرام مـيوزك للحسابات 🥷\n🔮 ¦ بايـروجـرام مـيوزك للبوتات 🎭\n🔗 ¦ بايـروجـرام مـيوزك احدث اصدار 📀\n\n- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت\n\nبواسطـة : [₍ ƚ ᥱ ƚ ᥆ || تـيـ ٖ ـتـو ⁾ ↺](tg://user?id=6352598131) 
    """

    HELP = """
**↢ للحصول علي مساعده** 

/about - معلومات البوت
/help - للمساعده
/start - لبدا البوت 
"""

    ABOUT = """
**معلومات البوت الاستخراج** 

بوت لاستخراج سلسلة الجلسات Pyrogram و Telethon.

Developer : [Teto](https://t.me/ToPTeTo)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)
    """
  

