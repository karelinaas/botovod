from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, PhotoSize

from config import *
from .filters import NumbersInMessage


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
# Имя аргумента совпадает с ключом из словаря, возвращаемого __call__ !!!!!!
@dp.message(F.text.lower().startswith('найди числа'), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Нашел: {", ".join(str(num) for num in numbers)}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(text='Не нашел что-то :(')


# В случае с магическими фильтрами используем .as_()
# Напр., передача в хэндлер ID фото либо с минимальным разрешением
@dp.message(F.photo[0].as_('photo_min'))
async def process_photo_send(message: Message, photo_min: PhotoSize):
    print(photo_min)

    # будет примерно такой вывод
    # file_id='AgACAgIAAxkBAAIZpGPhTiRFNTUJD_rRLyfE1hEMQEVCAAL5xzEbMJgJS6e3JLN71804AQADAgADcwADLgQ'
    # file_unique_id='AQAD-ccxGzCYCUt4'
    # width=90
    # height=90
    # file_size=2862
