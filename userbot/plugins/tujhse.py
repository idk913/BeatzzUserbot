"""COMMAND : .tujhse"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="tujhse"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "tujhse":

    await event.edit("👁👁")

    animation_chars = [

            "👁👁\n  👄  =====> Tujhse",
            "👁👁\n  👅  =====> Kisine",    
            "👁👁\n  💋  =====> Pucha",
            "👁👁\n  👄  =====> Kya?",
            "👁👁\n  👅  =====> Mujhe maalum hai chal",    
            "👁👁\n  💋  =====> Apne baap ko mat sikha",
            "👁👁\n  👄  =====> Nikal,",
            "👁👁\n  👅  =====> Pehli fursat mei nikal",    
            "👁👁\n  💋  =====> @BeatsToHell913's BOT is the best bot ever!"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
