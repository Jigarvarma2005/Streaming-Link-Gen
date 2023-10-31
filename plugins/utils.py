# (c) Jigarvarma2005

from helper_funcs.bot_utils import *
from config import Config
import time
from bot import botStartTime
import pyrogram
import shutil, psutil
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper_funcs.fsub import handle_force_sub

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["stats","status"]))
async def stats(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    currentTime = readable_time((time.time() - botStartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>Total disk space:</b> {total}\n' \
            f'<b>Used:</b> {used}  ' \
            f'<b>Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>Upload:</b> {sent}\n' \
            f'<b>Down:</b> {recv}\n\n' \
            f'<b>CPU:</b> {cpuUsage}% ' \
            f'<b>RAM:</b> {memory}% ' \
            f'<b>Disk:</b> {disk}%'
    await update.reply_text(botstats)

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["brightcove"]))
async def brightcove(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me BrightCove video id"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/brightcove?id={uri}"
    await update.reply_text(text="Use the below url to stream in website",
                            reply_markup=InlineKeyboardMarkup(
                                    [[
                                        InlineKeyboardButton("Stream", url=uri)
                                        ]]
                                        ))

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["jw"]))
async def jwplayer_(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me JW Player video id"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/jw?id={uri}"
    await update.reply_text(text="Use the below url to stream in website",
                            reply_markup=InlineKeyboardMarkup(
                                    [[
                                        InlineKeyboardButton("Stream", url=uri)
                                        ]]
                                        ))

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["yt"]))
async def yt__(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me YouTube video id or URL"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/yt?id={uri}"
    await update.reply_text(text="Use the below url to stream in website",
                            reply_markup=InlineKeyboardMarkup(
                                    [[
                                        InlineKeyboardButton("Stream", url=uri)
                                        ]]
                                        ))

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["m3u8"]))
async def m3u8_(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me m3u8 URL"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/m3u8?id={uri}"
    await update.reply_text(text="Use the below url to stream in website",
                            reply_markup=InlineKeyboardMarkup(
                                    [[
                                        InlineKeyboardButton("Stream", url=uri)
                                        ]]
                                        ))

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["mpd"]))
async def mpd_(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me mpd URL"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/mpd?id={uri}"
    await update.reply_text(text="Use the below url to stream in website",
                            reply_markup=InlineKeyboardMarkup(
                                    [[
                                        InlineKeyboardButton("Stream", url=uri)
                                        ]]
                                        ))

@app.on_message(pyrogram.filters.private & pyrogram.filters.command(["play"]))
async def direct_player_(bot, update):
    back = await handle_force_sub(bot, update)
    if back == 400:
        return
    msg = "Now send me Direct Video URL"
    uri = await input_str(bot, update,msg)
    if uri == 404:
        return
    uri = f"https://{Config.VIDEO_PLAYER_URL}/play?id={uri}"
    await update.reply_text(text="Use the below url to stream in website",
                            reply_markup=InlineKeyboardMarkup(
                                    [[
                                        InlineKeyboardButton("Stream", url=uri)
                                        ]]
                                        ))
