from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Ben **{bn}** !!
Grubunuzun sesli sohbetinde müzik çalmanıza izin 😉

Şu anda desteklediğim komutlar şunlardır:

✳️ /oynat  -  **Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.**
✳️ /durdur -  **Sesli Sohbet Müziğini Duraklat.**
✳️ /devam  -  **Sesli Sohbet Müziğine Devam Et.**
✳️ /atla   -  **Sesli Sohbette Çalan Geçerli Müziği Atlar.**
✳️ /bitir  -  **Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.**
✳️ /katil  -  **Müzik Botunun Asistanını Gruba Çağırır.**
✳️ /ayril  -  **Müzik Botunun Asistanını Gruptan Çıkartır.**
✳️ /bul    -  **Müziği bulup gruba gönderir. Örnek /bul ezhel geceler.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Grup 💬", url="https://t.me/zmonios"
                    ),
                    InlineKeyboardButton(
                        "Kanal 📣", url="https://t.me/zmoniosmusic"
                    )
                ]
            ]
        )
    )
