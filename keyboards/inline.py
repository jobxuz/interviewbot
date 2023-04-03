from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

startpython = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='♻ start python interview',callback_data='python'),
        ],
    ]
)


startdjango = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='♻ start django interview',callback_data='django'),
        ],
    ]
)


startdrf = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='♻ start drf interview',callback_data='drf'),
        ],
    ]
)

startjobinterview = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='♻ start job interview',callback_data='jobinterview'),
        ],
    ]
)


rek = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='✅ Ha',callback_data='ha'),
        InlineKeyboardButton(text="❌ Yo'q",callback_data="yuq")
    ],
    ]
)