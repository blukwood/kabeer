from config import PREFIX
from kabeer import LOGGER, app
from kabeer import app, CMD_HELP, StartTime

from pyrogram import Client, filters

@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def ammastar(kabeerstar):
    if kabeerstar.fwd_from:  
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    await eor(hellstar, "I am A Star")
    animation_chars = [
        "I Party like a rockstar",
        "I Look like a movie star",
        "I Play like an all star",
        "I Fuck like a pornstar",
        "Baby I'm a superstar",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        
        await hellstar.edit(animation_chars[i % 11])
    
