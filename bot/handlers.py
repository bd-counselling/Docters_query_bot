from telegram import Update
from telegram.ext import CallbackContext
from .filters import should_activate, classify_query
from .config import ADMIN_BASIC, ADMIN_TECH, ADMIN_SALES

def handle_group_message(update: Update, context: CallbackContext):
    text = update.message.text
    user = update.message.from_user
    username = f"@{user.username}" if user.username else user.full_name

    if not should_activate(text):
        return

    category = classify_query(text)

    if category == "basic":
        update.message.reply_text("👋 Thank you for your message. We'll forward it to our support team.")
        context.bot.send_message(
            chat_id=ADMIN_BASIC,
            text=f"📨 *New Basic Query*\nFrom: {username}\n\nMessage:\n{text}",
            parse_mode="Markdown"
        )

    elif category == "tech":
        update.message.reply_text("🛠️ Thanks for your query! Our tech team will get back to you shortly.")
        context.bot.send_message(
            chat_id=ADMIN_TECH,
            text=f"🛠 *Tech Query Received*\nFrom: {username}\n\nMessage:\n{text}",
            parse_mode="Markdown"
        )

    elif category == "sales":
        update.message.reply_text("💬 Thank you! Available — please contact support.")
        context.bot.send_message(
            chat_id=ADMIN_SALES,
            text=f"💼 *Sales Query*\nFrom: {username}\n\nMessage:\n{text}",
            parse_mode="Markdown"
        )

    else:
        update.message.reply_text("❓ Sorry, we couldn’t understand your query.")