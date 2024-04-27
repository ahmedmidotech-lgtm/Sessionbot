from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "📟 ¦ اهلا بـك عزيـزي في بوت الاستخراج\n🖱 ¦ يـمكنك استـخـراج الـتـالـي 📥\n📟 ¦ تيرمـكـس تليثون للحسـابـات 🥷\n📡 ¦ تيرمـكـس تليثون للبوتــات 🎭\n🎸 ¦ بايـروجـرام مـيوزك للحسابات 🥷\n🔮 ¦ بايـروجـرام مـيوزك للبوتات 🎭\n🔗 ¦ بايـروجـرام مـيوزك احدث اصدار 📀\n- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت\nبواسطـة : [₍ ƚ ᥱ ƚ ᥆ || تـيـ ٖ ـتـو ⁾ ↺](https://t.me/ToPTeTo)"
buttons_ques = [
    [
        InlineKeyboardButton("‹ بايروجرام ›", callback_data="pyrogram1"),
        InlineKeyboardButton("‹ بايروجرام V2 ›", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("‹ تيلثون ›", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("‹ بايروجرام بوت ›", callback_data="pyrogram_bot"),
        InlineKeyboardButton("‹ بوت تيلثون ›", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "‹ تيلثون ›"
    else:
        ty = "‹ بايروجرام V2 ›"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"↢ جاري بدا انشاء جلسه {ty} ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Tolong Kirim `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('🎮 حسنـا قم بأرسال الـ API_ID\n\nاضغط /skip عشان تكمل بالرقم بس.', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("⌔ يجب ان يكون ايبي ايدي عدداً صحيحاً \n⌔ يࢪجي المحـاولة مـࢪة أخـࢪى...", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» » 🎮حسنـا قم بأرسال الـ API_HASH", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        await msg.reply("Mengirim OTP...")
    else:
        await msg.reply("Masuk sebagai Pengguna Bot...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply('`API_ID` Dan `API_HASH` Kombinasi Tidak Valid/Salah, Mulai Ulang /start generating session.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply('`PHONE_NUMBER` Tidak Valid. Tolong Mulai Ulang /start generating session.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "Silahkan Periksa **OTP** Di Akun Telegram Resmi Kamu. Jika kamu mendapatkan kode OTP, kirim OTP ke sini setelah membaca format di bawah ini \nIf OTP is `12345`, **Tolong Kirim OTP sebagai Berikut Contoh!** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('Batas waktu mencapai 10 menit. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply('OTP tidak valid. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply('OTP sudah habis masa berlakunya. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, 'Akun kamu telah mengaktifkan verifikasi dua langkah. Harap berikan kata sandinya.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('Batas waktu mencapai 5 menit. Silakan mulai membuat sesi lagi.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply('Kata Sandi yang Diberikan Tidak Valid. Silakan mulai membuat sesi lagi.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} STRING SESSION** \n\n`{string_session}` \n\nGenerated by @SpotifyStreamMusic"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "Berhasil dibuat {} string session. \n\nSilakan periksa pesan yang Anda simpan! \n\nBy @Usern4meDoesNotExist404".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Membatalkan Proses!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Mulai ulang Bot!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Membatalkan proses session!", quote=True)
        return True
    else:
        return False
