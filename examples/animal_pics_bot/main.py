# Этот бот написан без применения библиотеки aiogram и лонг поллинга.
# Так что он немного туповат))

# This bot is done without aiogram and long-polling.
# So it's kind of stupid.

if __name__ == '__main__':
    import time

    import requests

    from config import *
    from . import utils
    from .constants import *

    counter: int = 0
    cat_response: requests.Response
    cat_link: str
    offset = -2

    while counter < 100:
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates['result']:
            for update in updates['result']:
                offset = update['update_id']
                chat_id = update['message']['from']['id']
                message_text = update['message']['text'].replace('/', '')

                if message_text == 'start':
                    param_name, param_value = utils.process_start_message(update)
                elif message_text in APB_AVAILABLE_COMMANDS:
                    param_name, param_value = utils.process_animal_message(
                        message_text,
                        *APB_AVAILABLE_COMMANDS[message_text]
                    )
                else:
                    param_name, param_value = utils.process_unknown_message(update)

                method_name = 'sendPhoto' if param_name == 'photo' else 'sendMessage'

                requests.get(f'{API_URL}{BOT_TOKEN}/{method_name}?chat_id={chat_id}&{param_name}={param_value}')

        time.sleep(1)
        counter += 1
