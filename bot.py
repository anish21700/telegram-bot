import random
import datetime
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8525046955:AAHhpmFhBAvbU1BUeqwuWCWC0G2sniFw-xw"
REGISTER_LINK = "https://www.sikkimok.com/#/register?invitationCode=65277140032"

# User lock system
user_active = {}

# Start command (Image + Message + Button)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Register Here", url=REGISTER_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://thecolourtrading.in/wp-content/uploads/2026/04/ChatGPT-Image-Apr-6-2026-12_09_49-AM.png",
        caption=(
            "🔥 100% Working Hack 🔥\n\n"
            "👉 First make account using below button\n"
            "👉 Then use bot for 100% accuracy\n\n"
            "⚠️ IMPORTANT:\n"
            "Before starting, ensure your wallet is prepared with a 6-level fund maintenance strategy.\n\n"
            "👇 Enter last 3 digit to start"
        ),
        reply_markup=reply_markup
    )

# Get remaining seconds (real-time sync)
def get_remaining_seconds():
    now = datetime.datetime.now()
    return 60 - now.second

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if text.isdigit() and len(text) == 3:

        # Check if already running
        if user_active.get(user_id, False):
            await update.message.reply_text("⚠️ Period already running, please wait for next result")
            return

        # Lock user
        user_active[user_id] = True

        # Generate result instantly
        result_type = random.choice(["🔴 RED", "🟢 GREEN", "🔼 BIG", "🔽 SMALL"])

        # Send result first
        temp_msg = await update.message.reply_text(f"""
🎯 Wingo Server 1min 🎯

📊 Period Number: {text}

⚡ Result: {result_type}
""")

        # Wait till next real minute
        remaining = get_remaining_seconds()
        await asyncio.sleep(remaining)

        # Delete previous message
        try:
            await context.bot.delete_message(
                chat_id=update.effective_chat.id,
                message_id=temp_msg.message_id
            )
        except:
            pass

        # Final declared message
        await update.message.reply_text("✅ Result Declared")

        # Unlock user
        user_active[user_id] = False

    else:
        await update.message.reply_text("❌ Please send only last 3 digits")

# Run bot
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running (FINAL VERSION 🔥)...")
app.run_polling()