from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
from kabeer import app, CMD_HELP
from kabeer.helpers.utils import requirements_list

import wikipedia


@app.on_message(filters.command('wiki', PREFIX) & filters.me)
async def wiki(client: Client, message: Message):
    lang = message.command[1]
    user_request = ' '.join(message.command[2:])
    if user_request == '':
        wikipedia.set_lang("ru")
        user_request = ' '.join(message.command[1:])
    try:
        if lang == 'en':
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f'''<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{result}</code>''')

    except Exception as exc:
        await message.edit(f'''<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>''')


CMD_HELP.update(
    {
        "wikipedia": """
**wikipedia**
  `wikipedia` -> wikipedia
"""
    }
)

requirements_list.append('wikipedia')
