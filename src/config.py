import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class CredentialsTwitter:
    KEY: str
    SECRET_KEY: str
    ACCESS_TOKEN: str
    ACCESS_SECRET_TOKEN: str
    CLIENT: str
    CLIENT_SECRET: str
    BEARER_TOKEN: str
    ACCOUNTS: list


@dataclass
class CredentialsDiscord:
    DISCORD_TOKEN: str
    DISCORD_CHANNEL: int


load_dotenv('.env')

credentials_twitter = CredentialsTwitter(os.getenv('KEY'),
                                         os.getenv('SECRET_KEY'),
                                         os.getenv('ACCESS_TOKEN'),
                                         os.getenv('ACCESS_SECRET_TOKEN'),
                                         os.getenv('CLIENT'),
                                         os.getenv('CLIENT_SECRET'),
                                         os.getenv('BEARER_TOKEN'),
                                         os.getenv('ACCOUNTS').split(','))

credentials_discord = CredentialsDiscord(os.getenv('DISCORD_TOKEN'),
                                         int(os.getenv('DISCORD_CHANNEL')))
