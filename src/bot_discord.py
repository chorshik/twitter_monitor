import asyncio
import logging
from nextcord.ext import commands

from config import CredentialsDiscord


class DiscordBot(commands.Bot):
    def __init__(self, credentials: CredentialsDiscord, log: logging.Logger, tweet: asyncio.Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_channel = credentials.DISCORD_CHANNEL

        # Queue
        self.tweet = tweet

        # Logger
        self.logger = log

        # Background tasks
        self.bg_data = self.loop.create_task(self.get_data_from_twitter())

    async def get_data_from_twitter(self):
        while True:
            try:
                data = await self.tweet.get()
                channel = self.get_channel(self.id_channel)
                self.logger.info(f"DISCORD. channel: {channel}")
                self.logger.info(f"DISCORD. Data from twitter_bot: {data}")
                await channel.send(data)
                self.logger.info(f"DISCORD. Data from twitter_bot send to {channel}")
            except Exception as e:
                self.logger.critical(f"{e}")
                raise AssertionError(e)
