import asyncio
from pyrogram import Client as Rocky, filters
from database.functions import get_settings
from pyrogram.errors import ChatWriteForbidden


@Rocky.on_message(filters.group & filters.new_chat_members)
async def welcome(client, update):
    settings = await get_settings(update.chat.id)
    if settings["welcome"]:
        try:
            try:            
                welcometext = settings["welcometext"]
                new_members = update.from_user.mention
                dell = await update.reply_text(welcometext.format(first_name = update.from_user.first_name, last_name = update.from_user.last_name, username = f"@{update.from_user.username}" or None, group_name = update.chat.title, mention = new_members), disable_web_page_preview=True)
                await asyncio.sleep(1000)
                await dell.delete()
            except ChatWriteForbidden:
                pass
            except Exception as error:
                pass
        except Exception as error:       
            await update.reply_text(f"{error}")
            await welcome.reply_text(f"{welcome}")
