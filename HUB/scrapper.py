from Liters import *
from HUB.fonalli_final import fonalli_final, get_code
from HUB.cookie_feeder import cookie_feeder
from HUB.pre_user_app import pre_user_app
from HUB.ph_value import ph_value
from HUB.user_app_maker import user_app_maker


def scrap(update: Update, _: CallbackContext):
    update.message.reply_text(
    """âðâ¢â¢Ã·[ HVÃ¥Ã¾Ã¯ÃÃ°â   ]Ã·â¢â¢ðâ
                              
ðºðð¨ð° ð¬ðð§ð ð¦ð ð²ð¨ð®ð« ð©ð¡ð¨ð§ð ð§ð®ð¦ððð« ð°ð¢ð­ð¡ ðð¨ð«ð«ððð­ ðð¨ð®ð§ð­ð«ð² ðð¨ððð»
        
 ð¦DÎ£V MÎ£ÐÆ¬IÓ¨Ð:
ð» @Krakinz | @KrakinzBot 
""")
    return range(2)
def receiver(update: Update, _: CallbackContext):
    user = update.message.from_user
    current_user_creds = GLOBAL_USERS_DICTIONARY.get(user.id)
    if user.id in GLOBAL_USERS_DICTIONARY:
        del GLOBAL_USERS_DICTIONARY[user.id]
    seeders = update.message.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",
    """âðâ¢â¢Ã·[ HVÃ¥Ã¾Ã¯ÃÃ°â   ]Ã·â¢â¢ðâ
           
Êá´á´Éªá´á´ á´á´ á´á´á´á´.....
á´á´á´ÉªÉ´É¢ Éªá´ á´Êá´á´á´Ê á´É´á´ Êá´á´á´É´ Êá´á´á´á´ÊÊá´

 ð¦DÎ£V MÎ£ÐÆ¬IÓ¨Ð:
ð» @Krakinz | @KrakinzBot 
    
""")
    
    provided_code = get_code(update.message)
    if provided_code is None:
        seeders.delete()
        seeders.reply_photo(
            "https://telegra.ph/file/d80887fc658949a5a674c.jpg",
            "âðâ¢â¢Ã·[ HVÃ¥Ã¾Ã¯ÃÃ°â   ]Ã·â¢â¢ðâ\nê±á´ÊÊÊ, Êá´á´ á´Êá´ ÉªÉ´á´á´á´ á´á´á´ê± É´á´á´ ê±á´á´á´ á´á´ Êá´ á´ á´ á´ÊÉªá´ á´á´Êá´É¢Êá´á´ á´¡á´Ê-Êá´É¢ÉªÉ´ á´á´á´á´\n\n\n\n ð¦DÎ£V MÎ£ÐÆ¬IÓ¨Ð:\nð» @Krakinz | @KrakinzBot ",
            parse_mode=ParseMode.HTML
        )
        return range(2)
    status_r, cookie_v = cookie_feeder(
        current_user_creds.get("ph_value"),
        current_user_creds.get("random_hash"),
        provided_code
    )
    if status_r:
        status_t, response_dv = pre_user_app(cookie_v)
        if not status_t:
            user_app_maker(
                cookie_v,
                response_dv.get("tg_app_hash"),
                HYPE_BOT_NAME,
                HYPE_BOT_NAME,
                f"https://telegram.dog/{HYPE_BOT_NAME}",
                ["android","wp","desktop","web","other","ios","bb"])
        status_t, response_dv = pre_user_app(cookie_v)
        if status_t:
            fonalli = fonalli_final(
                current_user_creds.get("ph_value"),
                response_dv
            )
            fonalli += "\n"
            fonalli += "\n"
            seeders.reply_photo(
            "https://telegra.ph/file/d80887fc658949a5a674c.jpg",
            fonalli,
            parse_mode=ParseMode.HTML
            )
        else:
            HYPEEED.warning("âðâ¢â¢Ã·[ HVÃ¥Ã¾Ã¯ÃÃ°â   ]Ã·â¢â¢ðâ\ná´Êá´á´á´ÉªÉ´É¢ á´á´á´ Éªá´ á´á´á´ê±á´á´ á´ÊÊá´Ê %s", response_dv)
            seeders.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",
            "âðâ¢â¢Ã·[ HVÃ¥Ã¾Ã¯ÃÃ°â   ]Ã·â¢â¢ðâ\nê±á´á´á´á´ÊÉªÉ´É¢ á´¡Êá´É´É¢ÉªÉ´É¢ê±. ê°á´ÉªÊá´á´ á´á´ É¢á´á´ á´á´á´ Éªá´.\n\n\n\n ð¦DÎ£V MÎ£ÐÆ¬IÓ¨Ð:\nð» @Krakinz | @KrakinzBot "
            )
    else:
        seeders.reply_photo(
"https://telegra.ph/file/d80887fc658949a5a674c.jpg",cookie_v)
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("scrap", scrap)],
        states={range(2): [MessageHandler(
                Filters.text | Filters.contact,
                ph_value)],
            INPUT_TG_CODE: [MessageHandler(Filters.text, receiver)]},
        fallbacks=[CommandHandler('scrap', scrap)])


hypeVoid.add_handler(conv_handler)