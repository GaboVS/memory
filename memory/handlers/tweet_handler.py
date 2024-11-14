# memory/handlers/tweet_handler.py

from telegram import Update
from telegram.ext import ContextTypes
import re
import logging
from memory.services.db_service import DynamoDBService

logger = logging.getLogger(__name__)

db_service = DynamoDBService()

# Your updated regex pattern
TWEET_URL_REGEX = r'(https?://(twitter\.com|x\.com)/\w+/status/\d+)'

async def tweet_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message
    text = message.text
    timestamp = message.date.isoformat()
    logger.debug(f"Received message from user {user_id}: {text}")

    tweet_links = re.findall(TWEET_URL_REGEX, text)
    logger.debug(f"Found tweet links: {tweet_links}")

    if not tweet_links:
        await message.reply_text("Please send a valid tweet link.")
        logger.info("No valid tweet link found in the message.")
        return

    for match in tweet_links:
        tweet_link = match[0]  # The full matched URL
        tweet_id = tweet_link.split('/status/')[1].split('/')[0].split('?')[0]
        logger.debug(f"Extracted tweet ID: {tweet_id}")

        db_service.store_tweet(tweet_id, tweet_link, str(user_id), timestamp)
        await message.reply_text(f"Tweet stored: {tweet_link}")
        logger.info(f"Stored tweet {tweet_id} from user {user_id}")
