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

import config



ask_ques = "📝 Silahkan Pilih Menu Yang Ada Dibawah, Sesi Mana Yang Kamu Ingin Ambil"
buttons_ques = [
    [
        InlineKeyboardButton("Pyrogram", callback_data="pyrogram1"),        
        InlineKeyboardButton("Pyrogram V2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("Telethon", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot"),
        InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="Mulai Generating Session", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"Start **{ty}** Session Generator...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "Kirim **API_ID**.\n\nKlik Di /skip Jika Tidak Ada Api Hash/Api Id,Dan Menggunakan Bot **API** Atau Menggunakan Nomor Telpon.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("Tidak Valid/Salah **API_ID*** (harus berupa bilangan bulat). Mulai Ulang /start generating session.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "Sekrang Kirim **API_HASH** Untuk Melanjutkan", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "Sekarang Kirim **PHONE_NUMBER** Beserta Kode Negaranya. \nExample : **+6298625717871**"
    else:
        t = "Sekarang Kirim **BOT_TOKEN** \nExample : **5656342352:AAFitoxkARAtBJlm-8cH_icrw6M975_IGia**"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("Mengirim **OTP** ...")
    else:
        await msg.reply("Masuk Sebagai Pengguna Bot...")
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
        await msg.reply("**API_ID** Dan **API_HASH** Kombinasi Tidak Valid/Salah, \n Mulai Ulang /start generating session.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("**PHONE_NUMBER** Tidak Valid. Tolong Mulai Ulang /start generating session.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "Silahkan Periksa **OTP** Di Akun Telegram Resmi Kamu. Jika kamu mendapatkan kode OTP, kirim OTP ke sini setelah membaca format di bawah ini. \nIf OTP is **12345**\n**Tolong Kirim OTP sebagai Berikut Contoh!** **1 2 3 4 5**.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("Batas waktu mencapai 10 menit.\n\nMulai buat sesi lagi.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("OTP adalah **Invalid**.\n\nMulai buat sesi lagi.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("OTP adalah **Expired**.\n\nMulai buat sesi lagi", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "Akun Anda telah diaktifkan **two-step verification** kata sandi. Berikan kata sandi untuk melanjutkan.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("Batas waktu mencapai 5 menit.\n\nMulai buat sesi lagi.", reply_markup=InlineKeyboardMarkup(gen_button))
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
                await two_step_msg.reply("Kata Sandi yang Diberikan Tidak Valid.\n\nMulai buat sesi lagi.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
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
    text = f"**{ty.upper()} STRING SESSION** \n\n`{string_session}` \n\n**GENERATET BY:** @StringSessionUbot_bot"
    try:
        if not is_bot:
            await client.send_message("me", text)
            await bot.send_message(msg.chat.id, text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "Berhasil membuat milik Anda **{}** string session.\n\nPeriksa pesan tersimpan Anda untuk mendapatkan !".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**Membatalkan Proses !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**Mulai ulang Bot !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**Membatalkan proses generating session !**", quote=True)
        return True
    else:
        return False
