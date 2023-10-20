### See the English text below!
Небольшой контейнеризированный ботовод, вдохновленный курсом [Телеграм-боты на Python и AIOgram](https://stepik.org/course/120924/syllabus) от [@kmsint](https://github.com/kmsint) 🤓 

Репо создан в обучающих целях, для примера работы Telegram-ботов в Docker + просто посмотреть, как они пишутся и работают без установки Python и ко 🙃
Nothing fancy))

Реализовано 2 примера ботов: 
- `animal_pics_bot` - бот, отправляющий случайные картинки с выбранным животным (лиса, кот, собака)
- `echo_bot` - бот-повторюшка (отправляет вам в ответ ваше же сообщение)

#### Запуск
1. Создаём аккаунт бота через [BotFather](https://t.me/BotFather), подробная инструкция есть в курсе.
   Нам необходимо получить **токен** бота.
2. Создаём файл `.env` в корне проекта, заполняем его данными по примеру `.env.example` (по сути надо заполнить только `BOT_TOKEN`)
3. Билдим один раз: `docker-compose up -d --build`
4. Запускаем любой из ботов по желанию:
   - `docker-compose run --rm --entrypoint "bash -c 'python -m examples.animal_pics_bot.main'" bot` – картинки с животными
   - `docker-compose run --rm --entrypoint "bash -c 'python -m examples.echo_bot.main'" bot` – повторюшка

#### Использование
1. С помощью поиска в Telegram находим своего бота по названию, которое задали в BotFather.
2. Пишем ему сообщение `/start`, следуем инструкциям бота, наслаждаемся 😃

#### Доработка
Вы можете создавать своих ботов по примеру приведённых и запускать их аналогичным образом.

Не забудьте обновить `requirements.txt` и заново сделать `docker-compose up -d --build`, если добавляете новые библиотеки.

----------------------------------------------------------------------

### English text
A small containerized bot runner inspired by [@kmsint](https://github.com/kmsint) `s course [Telegram Bots in Python and AIOgram](https://stepik.org/course/120924/syllabus)  🤓

This repo was created for educational purposes, as an example of Dockerized Telegram Bots + just to see how they can be created and used without installing Python, etc. 🙃
Nothing fancy :)

There are 2 examples of implemented bots:
- `animal_pics_bot` - the bot that sends random pics with a chosen animal (a fox, a cat, a dog)
- `echo_bot` - the echo bot (replies you with the message you sent)

#### Launch
1. Create a bot account via [BotFather](https://t.me/BotFather), [instructions in English](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot).
   You have to get a bot **token**.
2. Create the `.env` file in the project root, fill it with required data, see `.env.example` (actually you only need to fill `BOT_TOKEN`)
3. Build it just one time: `docker-compose up -d --build`
4. Run any bot you wish:
   - `docker-compose run --rm --entrypoint "bash -c 'python -m examples.animal_pics_bot.main'" bot` – animals pics
   - `docker-compose run --rm --entrypoint "bash -c 'python -m examples.echo_bot.main'" bot` – echo bot

#### Usage
1. Find your bot via Telegram search. Use the name you provided to BotFather.
2. Send a message `/start`, follow the bot instructions, enjoy 😃

#### Development
You can create your own bots using the code examples and launch them in the described way.

If you add new libraries, don't forget to update `requirements.txt` and run `docker-compose up -d --build` once again.
