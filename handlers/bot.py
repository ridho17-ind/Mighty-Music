from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJX5NgelpPxIp7TxBi31AWY0e6awyNoAACrwIAAiZaqFetusa6iC_gHx8E")
    await message.reply_sticker("CAACAgUAAxkBAAEJhiRghU-HBoDo2l62Hsreb8jG3YAHzwACZAIAAgZVKFSjwwmhSBUWsh8E")
    await message.reply_text(
        f"""**┗┓| MIGHTY BOT MUSIK | ┏┛**

**Hallo kamu 🙋‍♂**
Nama saya adalah __[Mighty Music Asssistant Bot](https://t.me/mightymusic_bot)__
Saya bisa memutar musik di Voice Call Grup kamu
━━━━━━━━━━━━━━━━━━━━
Dikelola oleh **[Yunus Zend](https://t.me/ZendYNS)** 👨‍💻

❖ **Tambahkan __[Mighty Music Assistant](https://t.me/mightymusic_assistant)__ **dan** __[Mighty Music Bot](https://t.me/mightymusic_bot)__ ke grup Anda, dan rasakan sensasi mendengar musik di VC Group anda!!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 Perintah 🎧", url="https://t.me/infoseputarbot/3")
                  ],[
                    InlineKeyboardButton(
                        "💭 Grup", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Creator 👨‍💻", url="https://t.me/ZendYNS"
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
      await message.reply_text("""**Mighty Bot Music Berhasil Diaktifkan ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💠 Group 💠", url="https://t.me/Cari_Teman_Online_Group")
                ]
            ]
        )
   )



