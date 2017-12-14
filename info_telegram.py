from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging
import time



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#GENDER, PHOTO, LOCATION, BIO = range(4)
PHOTO = 0

def start(bot, update):
    update.message.reply_text(
        'Okay! Send me some images.')
    return PHOTO



def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    ss = time.time()
    photo_file.download('C:\\Users\\chinkasoni\\AppData\\Local\\Programs\\Python\\Python36\\TelegramImages\\user_photo'+str(ss)+'.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')

    


def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Thank you.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def images():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("457762085:AAE9eFQrFHOq-OJoEyMLCx2O85kGpl3sEY4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('photo', start)],

        states={

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
