from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admincommands = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="admin panel"),
            KeyboardButton(text="interviews")
        ],

    ],
    resize_keyboard=True
)

adminusers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="users"),
        ],
        [
            KeyboardButton(text="reklama"),
        ],
        [
            KeyboardButton(text="back")
        ],
    ],
    resize_keyboard=True
)

admin_interview = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Job interview"),
            KeyboardButton(text="DRF"),

        ],
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Django"),
            #KeyboardButton(text="DRF"),

        ],
[
            KeyboardButton(text="PHP"),
            KeyboardButton(text="Laravel"),
        ],
        [
            KeyboardButton(text="Java"),
        ],
        [
            KeyboardButton(text="🗯️ Fikr bildirish"),

        ],
        [
            KeyboardButton(text="back"),

        ],
    ],

    resize_keyboard=True
)
