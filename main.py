from telegram.ext import Updater, MessageHandler, Filters
from bot.handlers import handle_group_message
from bot.config import BOT_TOKEN

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_group_message))

    print(" Samaira bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()