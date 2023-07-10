from aiogram import Bot, Dispatcher, types
from config import Config

bot = Bot(Config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
