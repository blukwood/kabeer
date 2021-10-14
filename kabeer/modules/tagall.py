from config import PREFIX
import asyncio
from kabeer import LOGGER, app1, app2
from kabeer import CMD_HELP
from pyrogram import Client, filters
from pyrogram.types import Message


CMD_HELP.update(
    {
        "tagall": """
**Alive**
  `alive` -> For Checking Pyrogram Alive Status
  `ping` -> For Pinging Pyrogram
"""
    }
)


@app1.on_message(filters.command("tagall", PREFIX))
@app2.on_message(filters.command("tagall", PREFIX))
async def tagall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    icm = client.iter_chat_members(chat_id)
    async for member in icm:
        tag = member.user.username
        if limit <= 5:
            if tag != None:
                string += f"@{tag}\n"
            else:
                string += f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""
            await asyncio.sleep(2)


