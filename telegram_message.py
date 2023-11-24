#!/usr/bin/env python
import asyncio
import os

import telegram
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COMPUTER = os.getenv('COMPUTER')


async def send_message_async(message)->str:
    """Sending message in Telegram chat"""
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(TELEGRAM_CHAT_ID, f'Computer {COMPUTER} - {message}')
        return 'ok'
    except telegram.error.BadRequest:
        return 'BadRequest, check TELEGRAM_CHAT_ID'
    except telegram.error.TimedOut:
        return 'TimedOut'
    except telegram.error.NetworkError:
        return 'NetworkError'
    except telegram.error.ChatMigrated:
        return 'ChatMigrated'
    except telegram.error.TelegramError:
        return 'TelegramError, check  TELEGRAM_TOKEN'
    except Exception as error:
        return str(error)


def send_message(message)->str:
    if not TELEGRAM_TOKEN:
        return 'TELEGRAM_TOKEN not define!'
    if not TELEGRAM_CHAT_ID:
        return 'TELEGRAM_CHAT_ID no define!'
    return asyncio.run(send_message_async(message))


if __name__ == '__main__':
    """main code"""
    print(send_message('Test'))
