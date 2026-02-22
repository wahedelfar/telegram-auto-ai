from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
BOT_TOKEN = os.getenv("8017128234:AAHiTswqIn7dYfsrpHWz8vw_V_UgE71TrSE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال 🔥")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
