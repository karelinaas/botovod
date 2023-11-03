from aiogram import Bot, Dispatcher

from config import *
from .filters import *
from .magic_filters import IsAdmin

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(command_slash_start_filter)
async def process_command_start(message: Message):
    await message.answer('Это команда /start')


# Этот хэндлер будет срабатывать на команду "|start"
@dp.message(command_pipe_start_filter)
async def process_command_start_2(message: Message):
    await message.answer('И это команда /start')


# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(ADMIN_IDS))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)
