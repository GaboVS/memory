# memory/services/db_service.py
import boto3
from botocore.exceptions import ClientError
import logging
from config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_DEFAULT_REGION,
    DYNAMODB_TABLE_NAME,
)

logger = logging.getLogger(__name__)

class DynamoDBService:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_DEFAULT_REGION,
        )
        self.table = self.dynamodb.Table(DYNAMODB_TABLE_NAME)

    def store_tweet(self, tweet_id, tweet_link, user_id, timestamp):
        try:
            self.table.put_item(
                Item={
                    'tweet_id': tweet_id,
                    'tweet_link': tweet_link,
                    'user_id': user_id,
                    'timestamp': timestamp,
                }
            )
            logger.info(f"Stored tweet {tweet_id} for user {user_id}")
        except ClientError as e:
            logger.error(e.response['Error']['Message'])