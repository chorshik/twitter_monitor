import asyncio
import logging
import json
from tweepy.asynchronous import AsyncStreamingClient, AsyncClient

from config import CredentialsTwitter


class TwitterBot(AsyncStreamingClient):
    def __init__(self, credentials: CredentialsTwitter, log: logging.Logger, tweet: asyncio.Queue):
        super().__init__(bearer_token=credentials.BEARER_TOKEN)
        self.client = AsyncClient(consumer_key=credentials.KEY,
                                  consumer_secret=credentials.SECRET_KEY,
                                  access_token=credentials.ACCESS_TOKEN,
                                  access_token_secret=credentials.ACCESS_SECRET_TOKEN,
                                  bearer_token=credentials.BEARER_TOKEN)

        # Queue
        self.tweet = tweet

        # Logger
        self.logger = log

        # Accounts
        self.accounts = ""
        self.set_accounts(credentials.ACCOUNTS)
        self.logger.info(f"TWITTER_BOT. Set accounts: {self.accounts}")

    def set_accounts(self, accounts):
        for i, account in enumerate(accounts):
            if i == len(accounts) - 1:
                self.accounts += f"from: {account}"
            else:
                self.accounts += f"from: {account} OR "

    async def on_data(self, data):
        row_data = json.loads(data)

        data = row_data["data"]
        includes = row_data["includes"]

        id_tweet = data["id"]
        username = includes["users"][0]["username"]

        link_on_tweet = f"https://twitter.com/{username}/status/{id_tweet}"
        self.logger.info(f"TWITTER_BOT. New tweet: {link_on_tweet} from {username}")
        await self.tweet.put(link_on_tweet)
