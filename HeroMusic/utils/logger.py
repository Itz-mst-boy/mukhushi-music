from config import LOG, LOG_GROUP_ID
from HeroMusic import app
from HeroMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        logger_text = f"""
**ᴍᴜᴋʜᴜsʜɪ ᴘʟᴀʏ ʟᴏɢ**

**ᴄʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**ᴜsᴇʀ:** {message.from_user.mention}
**ᴜsᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
**ᴜsᴇʀ ɪᴅ:** `{message.from_user.id}`
**ᴄʜᴀᴛ ʟɪɴᴋ:** {chatusername}

**ǫᴜᴇʀʏ:** {message.text}

**sᴛʀᴇᴀᴍᴛʏᴘᴇ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
