# (c) Jigarvarma2005

from translation import Translation
from pyrogram import filters, Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper_funcs.fsub import handle_force_sub

@app.on_message(filters.private & filters.command(["help", "about"]))
async def help_user(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    HELP = Translation.HELP_USER.format(update.from_user.first_name, update.from_user.id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=HELP,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🚨Updates Channel🚨", url="https://t.me/Universal_Projects"),
                    InlineKeyboardButton("👷Support Group👷", url="https://t.me/JV_Community")
                ],
                [
                    InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/Jigarvarma2005")
                ]
            ]
        ),
        parse_mode="markdown",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )



@app.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    START = Translation.START_TEXT.format(update.from_user.first_name, update.from_user.id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=START,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🚨Updates Channel🚨", url="https://t.me/Universal_Projects"),
                    InlineKeyboardButton("👷Support Group👷", url="https://t.me/JV_Community")
                ],
                [
                    InlineKeyboardButton("🧑‍💻Devloper🧑‍💻", url="https://t.me/Jigarvarma2005")
                ]
            ]
        ),
        parse_mode="markdown",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
    )


