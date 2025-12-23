import random
from telegram import Update
from telegram.ext import ContextTypes

FIGHT_LINES = [
    "😏 Itna gussa? Internet slow hai kya?",
    "🔥 Bhai thoda cool reh, AC on karle",
    "😂 Ye fight hai ya comedy show?",
    "😈 Aaj mood kharab lag raha hai tera",
    "💀 Bhai rehne de, tu jeet nahi paayega"
]

async def fight_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        reply = random.choice(FIGHT_LINES)
        await update.message.reply_text(reply)
