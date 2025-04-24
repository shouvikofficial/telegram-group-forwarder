from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os

BOT_TOKEN = os.getenv('7536291553:AAGxjHtUNXydahcGzzGwFS3RXMyWzCbaeAE')  # Get token from environment

SOURCE_CHANNEL_ID = -1002549325968  # Replace with your Channel ID
TARGET_GROUP_IDS = [
    -1002049245401,  # Replace with Group 1
    -1002233522556,  # Replace with Group 2
    -1002506072930   # Replace with Group 3
]

def forward_to_groups(update: Update, context: CallbackContext):
    if update.effective_chat.id == SOURCE_CHANNEL_ID:
        for group_id in TARGET_GROUP_IDS:
            try:
                context.bot.forward_message(
                    chat_id=group_id,
                    from_chat_id=SOURCE_CHANNEL_ID,
                    message_id=update.message.message_id
                )
            except Exception as e:
                print(f"Failed to forward to {group_id}: {e}")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.all, forward_to_groups))

updater.start_polling()
updater.idle()
