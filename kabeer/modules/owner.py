import asyncio
import time
import os

from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from kabeer import app, CMD_HELP
from config import Config

# Help
CMD_HELP.update(
    {
        "Owner Tools": f"""
**Owner Stuff,**

   `block` - To Block a User
   `unblock` - To Unblock a Blocked User
   `kickme` - To Leave From a Chat
   `chats` - To Count your Chats (Unstable due to Floodwait Limits)
"""
    }
)


# To Block a user
@app.on_message(filters.command("block", PREFIX) & filters.me)
async def block_dumb(_, message: Message):
  shit_id = message.chat.id
  r_msg = message.reply_to_message
  try:
    if r_msg:
      await app.block_user(r_msg.from_user.id)
      await message.edit("`Successfully Blocked This User`")
    else:
      await app.block_user(shit_id)
      await message.edit("`Successfully Blocked This User`")
  except Exception as lol:
    await message.edit(f"**Error:** `{lol}`")

# To Unblock User That Already Blocked
@app.on_message(filters.command("unblock", PREFIX) & filters.me)
async def unblock_boi(_, message: Message):
  good_bro = int(message.command[1])
  try:
    await app.unblock_user(good_bro)
    await message.edit(f"`Successfully Unblocked The User` \n**User ID:** `{good_bro}`")
  except Exception as lol:
    await message.edit(f"**Error:** `{lol}`")

# Leave From a Chat
@app.on_message(filters.command("kickme", PREFIX) & filters.me)
async def ubkickme(_, message: Message):
  try:
    await app.leave_chat(message.chat.id)
    await message.edit("`Successfully Leaved This Chat!`")
  except Exception as lol:
    await message.edit(f"**Error:** `{lol}`")

# To Get How Many Chats that you are in (PM's also counted)
@app.on_message(filters.command("chats", PREFIX) & filters.me)
async def ubgetchats(_, message: Message):
  total=0
  async for dialog in app.iter_dialogs():
    try:
      await app.get_dialogs_count()
      total = total+1
      await message.edit(f"**Total Chats Counted:** `{total}`")
    except FloodWait as e:
      await time.sleep(e.x)