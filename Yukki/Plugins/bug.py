from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
)

from Yukki import (
    BOT_USERNAME, 
    SUDOERS, 
    app, 
)
from config import SUP_GROUP

def get_text(message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


OWNER_NAME = "kyouka"
OWNER_USERNAME = "BukanYesus"


@app.on_message(filters.command(["bomsag", f"bug@{BOT_USERNAME}"]) & filters.group)
async def bug(_, message):
    report = get_text(message)
    if message.chat.username:
        chatusername = f"[{message.chat.title}](t.me/{message.chat.username})"
    else:
        chatusername = f"{message.chat.title}"
    if not report:
        await message.reply(
            "Contoh menggunakan fitur ini\n`/bug assisten ga turun`",
        )
        return
    await app.send_message(
        SUP_GROUP,
        f"""
**✅ [{OWNER_NAME}](t.me/{OWNER_USERNAME}) Ada Laporan Baru
🧑‍💼 Pengguna: {message.from_user.mention}
💡 Group: {chatusername}
🆔 Id: `{message.chat.id}`
💬 Pesan: {report}**
""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"• {message.from_user.first_name} •",
                        url=f"{message.link}",
                    )
                ]
            ]
        ),
    )
    await message.reply(
        f"**🙏🏻 Terimakasih {message.from_user.mention} laporan anda sedang di proses oleh admin**"
    )


@app.on_message(filters.command(["send", f"send@{BOT_USERNAME}"]) & filters.user(SUDOERS))
async def send(_, message):
    text = get_text(message)
    texting = message.reply_to_message
    await app.send_message(text, texting.text)


@app.on_message(filters.command(["rsend", f"rsend@{BOT_USERNAME}"]) & filters.user(SUDOERS))
async def rsend(_, message):
    text = get_text(message)
    stickers = message.reply_to_message
    await app.send_sticker(text, stickers.sticker.file_id)
