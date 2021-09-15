from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
from kabeer import app, CMD_HELP
import asyncio


@app.on_message(filters.command(['kickme'], PREFIX) & filters.me)
async def leave_chat(client: Client, message: Message):
    m = await message.edit('<code>Byy, See You all in hell</code>')
    await asyncio.sleep(3)
    await client.leave_chat(chat_id=message.chat.id)
    

CMD_HELP.update(
    {
        "kickme": """
**kickme**
  `kickme` -> Leave a chat
"""
    }
)
