from aiogram import types, Dispatcher, Bot
from fastapi import FastAPI

from config import Config
from bot import bot, dp

app = FastAPI()

WEBHOOK_PATH = f"/bot/{Config.TOKEN}"
WEBHOOK_URL = Config.NGROK_TUNNEL_URL + WEBHOOK_PATH


@app.on_event("startup")
async def on_startup():
    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
