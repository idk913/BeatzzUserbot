# modified for FRIDAY by @WhySooSerious
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from userbot.utils import admin_cmd


@borg.on(admin_cmd("deezer (.*)"))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    chat = "@DeezerMusicBot"
    await event.edit("```B.E.A.T.Z.Z is Getting Your Music```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`B.E.A.T.Z.Z is Downloading Music \nIt may take some time\n   So Stay Tuned.....`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
              await bot.send_message(chat, name)
              respond = await response
              respond2 = await response2
          except YouBlockedUserError:
              await event.reply("```Please unblock @DeezerMusicBot and try again```")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)
          await bot.forward_messages(event.chat_id, respond2.message)
