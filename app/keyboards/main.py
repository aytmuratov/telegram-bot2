from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Yordam"),
            KeyboardButton(text="ℹ️ Ma'lumot"),
        ],
    ],
    resize_keyboard=True
)