
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8308301984:AAFFioBRotihpg3_UkPBJ8Z5PowpJmmjO9o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Money Maker Bot is Running!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")

app.run_polling()
