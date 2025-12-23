
from telegram.ext import ApplicationBuilder
from bot.config import BOT_TOKEN
from bot.handlers import register_handlers

app = ApplicationBuilder().token(BOT_TOKEN).build()
register_handlers(app)

print("🔥 Chat Fight Bot is running...")
app.run_polling()
