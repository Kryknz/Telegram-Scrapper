from Liters import *

def start(update: Update, context: CallbackContext):
    args = context.args
    if update.effective_chat.type == "private":
        update.message.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",
"""โ๐โขโขรท[ HVรฅรพรฏรรฐโ   ]รทโขโข๐โ

    ๐ป ๐ช๐ต๐ฎ๐ ๐๐ฎ๐ป ๐๐ผ๐ ๐๐ผ???
โ๏ธ๐๐ฆ๐ญ๐ฆ๐จ๐ณ๐ข๐ฎ ๐ฃ๐ฐ๐ต ๐ต๐ฐ ๐ค๐ณ๐ฆ๐ข๐ต๐ฆ ๐ถ๐ด๐ฆ๐ณ ๐๐๐ ๐ข๐ฏ๐ฅ ๐ด๐ฆ๐ฏ๐ฅ ๐ต๐ฉ๐ฆ๐ช๐ณ ๐๐๐_๐๐ ๐ข๐ฏ๐ฅ ๐๐๐_๐๐๐๐ 


/scrap แดแด แดษดส ๊ฑแดแดษขแด แดแด สแด-แดษดแดแดส สแดแดส แดแดแดแดษชส๊ฑ

 ๐ฆDฮฃV MฮฃะฦฌIำจะ:\n๐ป @Krakinz | @KrakinzBot  
""",
    parse_mode=ParseMode.HTML
    )
start_handler = CommandHandler("start", start, run_async=True)
hypeVoid.add_handler(start_handler)