from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""◍¦ اهلا بـك عزيـزي  {msg.from_user.mention}
◍ فـي بـوت اسـتـخـراج الـجـلـسـات
◍ يمكنك استخراج الجلسات الـتالية
◍ بايروجرام للحسابات & بايروجرام للبوتات
◍ بـايـروجـرام مـيوزك احـدث إصـدار 
◍ تيرمـكـس للحسابات & تيرمـكـس للبوتات

◍¦ بواسطـة : [𒆜🇦🇱⃝⃤|『 𝗧𝗘𝗧𝗢 』تيـتو](tg://user?id=6133404544) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ابدء استخراج جلسه", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗧𝗢", url="https://t.me/WX_PM"),
                    InlineKeyboardButton("𒆜🇦🇱⃝⃤|『 𝗧𝗘𝗧𝗢 』تيـتو", user_id=6133404544)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
