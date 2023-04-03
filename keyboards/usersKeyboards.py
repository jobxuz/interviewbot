from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BoshMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="interviews"),

        ],

    ],
    resize_keyboard=True
)


interview = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="Django"),
            KeyboardButton(text="DRF"),

        ],
        [
            KeyboardButton(text="Job interview"),

        ],
    ],

    resize_keyboard=True
)


endstate = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="end interview"),

        ],

    ],
    resize_keyboard=True
)
