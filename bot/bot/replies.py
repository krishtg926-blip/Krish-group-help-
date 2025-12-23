from telegram import Update
from telegram.ext import ContextTypes

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Chat Fight Bot Activated!\n"
        "Type anything and I’ll fight back 😈"
    )
