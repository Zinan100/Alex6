from pyrogram import Client as Mr_bots, filters
from pyrogram.types import Message
from utils import save_group_settings



@Mr_bots.on_message((filters.private | filters.group) & filters.command('setwelcome'), group=8)
async def setwelcome(client, message):
    sts = await message.reply("⏳️")
    await asyncio.sleep(0.3)
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f" 𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽. /connect {message.chat.id} 𝙸𝙽 𝙿𝙼")
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙸𝙰𝙼 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..!", quote=True)
                return
        else:
            await message.reply_text("𝙸𝙰𝙼 𝙽𝙾𝚃 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙰𝙽𝚃 𝙶𝚁𝙾𝚄𝙿..!", quote=True)
            return

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    member = await client.get_chat_member(grp_id, userid)
    if (member.status != enums.ChatMemberStatus.ADMINISTRATOR and member.status != enums.ChatMemberStatus.OWNER and userid not in ADMINS):
        return

    if len(message.command) < 2:
        return await sts.edit("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳..!", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴", callback_data="welcome") ]] ))

    pr0fess0r_99 = message.text.split(" ", 1)[1]
    await save_group_settings(grp_id, 'welcometext', pr0fess0r_99)
    await sts.edit(f"""𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝙾𝚁 {title} 𝚃𝙾\n\n{pr0fess0r_99}""", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]] ))
