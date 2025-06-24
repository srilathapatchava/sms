import os
import django
from telegram.ext import Updater, CommandHandler
from core.models import TelegramUser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_backend_project.settings')
django.setup()

from decouple import config
BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')

def start(update, context):
    username = update.message.from_user.username
    TelegramUser.objects.get_or_create(username=username)
    update.message.reply_text(f"Hi @{username}! You've been registered.")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
