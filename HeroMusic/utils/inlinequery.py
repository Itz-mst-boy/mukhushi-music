from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴍᴜᴛᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Unmute Stream",
            description=f"ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Skip Stream",
            description=f"sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [ɴᴜᴍʙᴇʀ] ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ᴇɴᴅ sᴛʀᴇᴀᴍ",
            description="sᴛᴏᴘ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="sᴇᴇᴋ sᴛʀᴇᴀᴍ",
            description="sᴇᴇᴋ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ᴅᴜʀᴀᴛɪᴏɴ.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="ʟᴏᴏᴘ sᴛʀᴇᴀᴍ",
            description="ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ. | ᴜsᴀɢᴇ: /loop [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
