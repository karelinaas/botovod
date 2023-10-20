from http import HTTPStatus

import requests


APB_ERROR_TEXT = 'Здесь должна была быть картинка с {animal_name} :('


def process_start_message(update: dict[str, int | dict | list]) -> tuple[str, str]:
    """
    An example of an "update" dict:
    {
        'update_id': 1,
        'message': {
            'message_id': 1,
            'from': {
                'id': 1,
                'is_bot': False,
                'first_name': 'Alexandra',
                'last_name': '',
                'username': 'karelinaas',
                'language_code': 'ru',
                'is_premium': True,
            },
            'chat': {
                'id': 1,
                'type': 'private',
                ...
            },
            'date': 1697726284,
            'text': '/start',
            'entities': [...]
        }
    }
    """

    assert 'message' in update
    assert 'from' in update['message']
    assert 'first_name' in update['message']['from']

    text_template: str

    if 'language_code' in (from_data := update['message']['from']) and from_data['language_code'] == 'ru':
        text_template = (
            'Привет, {username}!\n'
            'Это бот, присылающий случайную картинку выбранного животного. Выбери животное:\n'
            '/cat – кот 😽\n'
            '/dog – собака 🐶\n'
            '/fox – лиса 🦊'
        )
        username = from_data['first_name'] or 'странник'
    else:
        text_template = (
            'Hi, {username}!\n'
            'This is the bot sending a random pic of a chosen animal. Please, choose an animal:\n'
            '/cat – a cat 😽\n'
            '/dog – a dog 🐶\n'
            '/fox – a fox 🦊'
        )
        username = from_data['first_name'] or 'stranger'

    return 'text', text_template.format(username=username)


def process_unknown_message(update: dict[str, int | dict | list]) -> tuple[str, str]:
    assert 'message' in update
    assert 'from' in update['message']

    if 'language_code' in (from_data := update['message']['from']) and from_data['language_code'] == 'ru':
        text = 'Ничего не понял, но спасибо 😅'
    else:
        text = 'I didn`t get a thing, but thank you 😅'
    return 'text', text


def process_animal_message(animal_type: str, url: str, animal_name: str) -> tuple[str, str]:
    try:
        return globals()[f'__process_{animal_type}_message'](url)
    except Exception:
        return 'text', APB_ERROR_TEXT.format(animal_name=animal_name)


def __process_cat_message(url: str) -> tuple[str, str] | None:
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        cat_link = response.json()[0]['url']
        return 'photo', cat_link
    else:
        raise Exception


def __process_dog_message(url: str) -> tuple[str, str] | None:
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        dog_link = response.json()['url']
        return 'photo', dog_link
    else:
        raise Exception


def __process_fox_message(url: str) -> tuple[str, str] | None:
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        fox_link = response.json()['link']
        return 'photo', fox_link
    else:
        raise Exception
