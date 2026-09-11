from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "📚 Bot komandalar:\n\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam\n"
    )