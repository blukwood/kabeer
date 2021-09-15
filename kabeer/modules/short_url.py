# Copyright (c) 2021 Itz-fork
# Part of: Nexa-Userbot

import requests
import os
from kabeer import app, CMD_HELP
from pyrogram import filters
from pyrogram.types import Message

from kabeer.helpers.pyrohelper import get_arg


# Help
CMD_HELP.update(
    {
        "short_url": f"""
**Short Url,**

  ✘ `short` - To short long url using is.gd's free api

**Example:**

  ✘ `short`,
   ⤷ Send command with url = `{Config.PREFIX}short https://google.com`
   ⤷ Reply to a url message = `{Config.PREFIX}short` (Reply to a message with url)
"""
    }
)


def paste_isgd(url):
    main_url = f"https://is.gd/create.php?format=json&url={url}"
    pasted_url = requests.post(main_url)
    json_data = pasted_url.json()
    short_url = json_data['shorturl']
    return short_url

@app.on_message(filters.command("short", PREFIX) & filters.me)
async def cutr_short(_, message: Message):
    replied_msg = message.reply_to_message
    if replied_msg:
        to_short = replied_msg.text
    elif not replied_msg:
        try:
            to_short = get_arg(message)
        except Exception as e:
            await message.edit(f"**Error:** `{e}`")
            return
    shoterned_url = paste_isgd(to_short)
    try:
        print(shoterned_url)
        await message.edit(f"**Successfully Shortened the Url** \n\n**Shortened Url:** {shoterned_url} \n**Original Url:** {to_short}", disable_web_page_preview=True)
    except Exception as e:
        await message.edit(f"**Error:** `{e}`")
