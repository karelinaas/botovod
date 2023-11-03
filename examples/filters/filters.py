from aiogram.filters import ChatMemberUpdatedFilter, Command, CommandStart, KICKED
from aiogram.types import Message


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'


def custom_filter(some_list: list) -> bool:
    return sum(
        item for item in some_list if isinstance(item, int) and not item % 7
    ) <= 83


anonymous_filter = lambda x: isinstance(x, str) and x.lower().count('я') >= 23

# Так же, как F, можно обращаться к свойствам:
# (F - это просто упрощенная запись для анонимных функций)
# lambda message: message.photo
# lambda message: message.content_type in ...
# lambda message: message.text == 'привет'
# lambda message: not message.text.startswith('bot')

# Этот фильтр будет срабатывать на команду "/start"
command_slash_start_filter = Command(commands='start')
# Этот фильтр будет срабатывать на команду "|start"
command_pipe_start_filter = Command(commands='start', prefix='|')

# Отдельный фильтр конкретно на команду старт
command_start_special_filter = CommandStart()

# Отлавливать изменения в статусах пользователей:
# - пользователь вступил в канал или группу
# - пользователь покинул канал или группу
# - пользователь стал админом группы или канала
# - пользователь перестал быть админом группы или канала
# - пользователь заблокировал бота
# - пользователь разблокировал бота
# - пользователь удален из группы или канала администратором
# - ...
# Этот хэндлер будет срабатывать на блокировку бота пользователем
member_kicked_filter = ChatMemberUpdatedFilter(member_status_changed=KICKED)

# Фильтр, который будет пропускать только апдейты от пользователя с ID = 173901673
concrete_user_filter = lambda message: message.from_user.id == 173901673
# или F.from_user.id == 173901673
