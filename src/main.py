import asyncio
import tweepy

from bot_twitter import TwitterBot
from bot_discord import DiscordBot
from logger import logger
from config import credentials_twitter, credentials_discord


async def start_twitter_bot(queue):
    stream = TwitterBot(credentials=credentials_twitter, log=logger, tweet=queue)

    await stream.add_rules(tweepy.StreamRule(stream.accounts))

    try:
        await stream.filter(expansions=["author_id", "referenced_tweets.id",
                                        "geo.place_id", "attachments.media_keys",
                                        "attachments.poll_ids"])
    except asyncio.CancelledError:
        stream.disconnect()


async def start_discord_bot(queue):
    bot = DiscordBot(credentials=credentials_discord, log=logger, tweet=queue)
    await bot.start(token=credentials_discord.DISCORD_TOKEN, reconnect=True)


async def twitter_monitor():
    queue = asyncio.Queue()

    tasks = [
        start_discord_bot(queue),
        start_twitter_bot(queue),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(twitter_monitor())
    except KeyboardInterrupt:
        print("Exiting due to KeyboardInterrupt")
