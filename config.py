import os


API_URL = os.environ.get('API_URL', 'https://api.telegram.org/bot')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_IDS = os.environ.get('ADMIN_IDS', '').split(',')
