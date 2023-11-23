#!/usr/bin/env python
import os
import asyncio

import telegram
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
COMPUTER = os.getenv('COMPUTER')

bot = telegram.Bot(token=TELEGRAM_TOKEN)


async def send_message_async(message):
    """Отправляет сообщение в Telegram чат."""
    try:
        await bot.send_message(TELEGRAM_CHAT_ID, f'Computer {COMPUTER} - {message}')
        return 'ok'
    except telegram.error.Unauthorized:
        return 'Unauthorized'
    except telegram.error.BadRequest:
        return 'BadRequest'
    except telegram.error.TimedOut:
        return 'TimedOut'
    except telegram.error.NetworkError:
        return 'NetworkError'
    except telegram.error.ChatMigrated:
        return 'ChatMigrated'
    except telegram.error.TelegramError:
        return 'TelegramError'
    except Exception as error:
        return error


def send_message(message):
    return asyncio.run(send_message_async(message))


if __name__ == '__main__':
    """main code"""
    print(send_message('Test'))