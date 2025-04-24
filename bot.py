import os
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

BOT_TOKEN = os.getenv("7536291553:AAGxjHtUNXydahcGzzGwFS3RXMyWzCbaeAE")  # This gets your token from Render

SOURCE_CHANNEL_ID = -1002549325968  # Replace with your channel ID
TARGET_GROUP_IDS = [-1002049245401, -1002233522556, -1002506072930]  # Replace with your 3 groups

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
