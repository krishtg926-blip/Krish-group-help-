from telegram.ext import ApplicationBuilder
from bot.config import BOT_TOKEN
from bot.handlers import register_handlers

app = ApplicationBuilder().token(7751407989:AAGpWMHsaWsGWtOkbr8veqOQ3wPqoi1xL60).build()
register_handlers(app)

print("🔥 Chat Fight Bot is running...")
app.run_polling()
