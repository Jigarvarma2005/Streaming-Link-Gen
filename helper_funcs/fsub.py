# (c) Jigarvarma2005

import os
from config import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def handle_force_sub(bot, cmd):
    if not Config.UPDATES_CHANNEL:
        return 500
    invite_link = f"https://t.me/{Config.UPDATES_CHANNEL}"
    try:
        user = await bot.get_chat_member(Config.UPDATES_CHANNEL, cmd.from_user.id)
        if user.status != "kicked":
            return 500
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/JV_Community).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link)
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/JV_Community).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
