import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/4f70284cc53a3de49369d.png"
pm_caption = "`BEATZZ IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.8.5**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**USERBOT DEV** : {@BeatsToHell913}\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
