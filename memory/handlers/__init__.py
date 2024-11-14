# memory/handlers/__init__.py
from telegram.ext import CommandHandler, MessageHandler, filters
from memory.handlers.start_handler import start_handler
from memory.handlers.tweet_handler import tweet_handler

def setup_handlers(application):
    application.add_handler(CommandHandler('start', start_handler))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), tweet_handler))