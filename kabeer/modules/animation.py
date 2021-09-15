from config import PREFIX
from kabeer import LOGGER, app
from kabeer import app, CMD_HELP, StartTime
import asyncio
from collections import deque
from pyrogram import Client, filters

@app.on_message(filters.command("istar", PREFIX) & filters.me)
async def kabeerstar(_, message: Message):
    if kabeerstar.fwd_from:  
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    await message.edit(kabeerstar, "I am A Star")
    animation_chars = [
        "I Party like a rockstar",
        "I Look like a movie star",
        "I Play like an all star",
        "I Fuck like a pornstar",
        "Baby I'm a superstar",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        
        await message.edit(animation_chars[i % 11])
    
