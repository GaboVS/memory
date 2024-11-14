# test_bot.py
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

async def start(update, context):
    logger.debug("Received /start command")
    await update.message.reply_text("Hello from the test bot!")

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    logger.info("Starting test bot...")
    application.run_polling()

if __name__ == '__main__':
    main()

