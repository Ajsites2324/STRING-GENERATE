from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⚜ Start Generating Session ⚜", callback_data="generate")],
        [InlineKeyboardButton(text=" ◀️Back◀️ ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("⚜🛡️ Support 🛡️⚜", url="https://t.me/TPN_CHATROOM")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("👨‍💻 Repo 👨‍💻", url="https://t.me/modern_elements")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton(" ⚔️About⚔️", callback_data="about")
        ],
        [InlineKeyboardButton("✨❤️💥Owner💥❤️✨ ", url="https://t.me/PAPA_BOL_SAKTEHO")],
    ]

    # Help Message
    HELP = """
» Click the below button or use /generate command to start generating session!
» Click the required button; [Pyrogram/Telethon]
» Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
👨‍💻 **About Me** 

A telegram bot to generate pyrogram and telethon string session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
            **Regarding ~ **@TPN_CHATROOM
"""
