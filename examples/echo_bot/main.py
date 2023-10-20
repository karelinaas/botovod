# Из библиотеки aiogram импортируем классы Bot и Dispatcher
from aiogram import Bot, Dispatcher, F
# Из aiogram.filters импортируем класс Command, чтобы фильтровать апдейты по наличию в них команд
from aiogram.filters import Command
# Из aiogram.types импортируем класс Message. Апдейты этого типа мы будем ловить эхо-ботом.
from aiogram.types import ContentType, Message

from config import *

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    # message.answer отправляет в чат сообщение, а message.reply отправляет ответ на сообщение
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help". ЕСЛИ его зарегистрировать!!!
async def send_echo_extended(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

    # Для аудио используется message.answer_audio(...)
    # Для видео - message.answer_video(...)
    # Для стикеров message.answer_sticker(...)


async def send_sticker_echo(message: Message):
    print(message)
    await message.reply_sticker(message.sticker.file_id)


# Альтернативный вариант регистрации хэндлеров (вместо декораторов)
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
# Можно проще:
# dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)

# dp.message.register(process_start_command, Command(commands='start'))
# dp.message.register(process_help_command, Command(commands='help'))
# send_echo по логике должен находиться в самом конце списка, т.к. он перехватывает любые сообщения
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
