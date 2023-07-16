from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot("6165021357:AAFWTzbGtOMIbygwPR0A2QZZumlEsl7A12k")
dp = Dispatcher(bot)
@dp.message_handler(commands = ['start'])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб страницу', web_app= WebAppInfo(url = 'https://peretokin.github.io')))
    await message.answer('дарова', reply_markup = markup)
executor.start_polling(dp)
