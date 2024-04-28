from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("📟 ¦ اهلا بـك عزيـزي {msg.from_user.mention}\n🖱 ¦ يـمكنك استـخـراج الـتـالـي 📥\n📟 ¦ تيرمـكـس تليثون للحسـابـات 🥷\n📡 ¦ تيرمـكـس تليثون للبوتــات 🎭\n🎸 ¦ بايـروجـرام مـيوزك للحسابات 🥷\n🔮 ¦ بايـروجـرام مـيوزك للبوتات 🎭\n🔗 ¦ بايـروجـرام مـيوزك احدث اصدار 📀\n\n- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت\n\nبواسطـة : [₍ ƚ ᥱ ƚ ᥆ || تـيـ ٖ ـتـو ⁾ ↺](tg://user?id=6352598131) ", callback_data="generate")]

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
Hallo {}
nama saya adalah [{}](https://mallucampaign.in/images/img_1703290706.jpg)
jika Anda tidak mempercayai bot ini!
──────────────────────
1) berhenti membaca pesan ini
2) hapus obrolan ini dan blokir bot
──────────────────────
kamu dapat menggunakan saya untuk menghasilkan sesi string Pyrogram dan Telethon. gunakan tombol di bawah ini untuk memulai!
    """

    HELP = """
**📝 Semua Printah** 

/about - Tentang Bot
/help - Bantuan
/start - Mulai Bot
/generate - Ambil Session 
/cancel - Batalkan Proses
/restart - Mulai Ulang Bot
"""

    ABOUT = """
**📝 Info Tentang Bot** 

Telegram Bot untuk mengambil session string Pyrogram dan Telethon.

Developer : [Klik Disini](https://t.me/Usern4meDoesNotExist404)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)
    """
  
  
