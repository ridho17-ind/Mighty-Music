from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJX5NgelpPxIp7TxBi31AWY0e6awyNoAACrwIAAiZaqFetusa6iC_gHx8E")
    await message.reply_text(
        f"""**┗┓| 👑SKYZO BOT MUSIK👑 |┏┛**

**Hallo kamu 🙋‍♂**
Nama saya adalah __[Skyzo Music Bot](https://t.me/Skyzo_Music_Bot)__
Saya bisa memutar musik di Voice Call Grup kamu
━━━━━━━━━━━━━━━━━━━━
Dikelola oleh **[Skyzo](https://t.me/SkyzoGanss)** 👨‍💻

❖ **Tambahkan __[Skyzo Music Assistant](https://t.me/SkyzooAsistens)__ **dan** __[Skyzo Music Bot](https://t.me/Skyzo_Music_Bot)__ __ke grup Anda, dan rasakan sensasi mendengar musik di VC Group anda!!**__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 Perintah 🎧", url="https://t.me/infoseputarbot/3")
                  ],[
                    InlineKeyboardButton(
                        "💭 Grup", url="https://t.me/skyzomusicbot"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Creator 👨‍💻", url="https://t.me/SkyzoGanss"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔉", url="https://t.me/infoseputarbot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Skyzo Bot Music Berhasil Diaktifkan ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💭 Group Support", url="https://t.me/skyzomusicbot")
                ]
            ]
        )
   )



