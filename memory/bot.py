# memory/bot.py

import logging
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from memory.handlers import setup_handlers

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(application)
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()