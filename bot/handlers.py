from telegram.ext import CommandHandler, MessageHandler, filters
from bot.fight import fight_reply
from bot.replies import start_cmd

def register_handlers(app):
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fight_reply))
