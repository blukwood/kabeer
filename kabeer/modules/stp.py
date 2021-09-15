from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
from kabeer import app, CMD_HELP
import os
import asyncio


CMD_HELP.update(
    {
        "stp": """
**stp**
  `stp` -> Reply to stiker
"""
    }
)


@app.on_message(filters.command(['stick2png', 'stp'], PREFIX) & filters.me)
async def stick2png(client: Client, message: Message):
    if message.reply_to_message:
        reply = message.reply_to_message
        if reply.sticker:
            if not reply.sticker.is_animated:
                await message.edit('<code>Picture processing...</code>')
                file = await client.download_media(message.reply_to_message, 'out.png')
                await client.send_photo(message.chat.id, 'downloads/out.png', reply_to_message_id=message.reply_to_message.message_id)
                await message.delete()
                os.remove('downloads/out.png')
            else:
                msg = await message.edit('<b>Stiker is animated!</b>')
                await asyncio.sleep(3)
                await msg.delete()
        else:
            msg = await message.edit('<b>Reply to stiker!</b>')
            await asyncio.sleep(3)
            await msg.delete()
