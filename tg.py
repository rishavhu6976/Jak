import psutil
import platform
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8682864637:AAGqRi5cuvfCe3jhdO0FEtQb9ItvFfcevx8"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 VPS Monitor Bot Active\nUse /stats to check server status."
    )

# Stats command
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    message = f"""
🖥️ VPS STATUS

⚡ CPU Usage: {cpu}%
🧠 RAM: {ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB
💾 Disk: {disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB

⏱️ Uptime: {str(uptime).split('.')[0]}

🖥️ OS: {platform.system()} {platform.release()}
"""

    await update.message.reply_text(message)

# Run bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stats", stats))

print("Bot is running...")
app.run_polling()
