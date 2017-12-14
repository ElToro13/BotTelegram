from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,ParseMode,InlineKeyboardButton,InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler,CallbackQueryHandler)

import logging
import time
from WebNews import News_Bot
from uuid import uuid4


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#GENDER, PHOTO, LOCATION, BIO = range(4)
News = 0

def start(bot, update):
    print("Pre-Stage - 5A")
    update.message.reply_text(
        'Send me some Keywords')
    return News

def NEWS(bot, update):  
    print("Stage - 5")
    #user = update.message.from_user
    #print(update.message.text)
    print(type(update.message.text))
    Output=[]
    Output = News_Bot(update.message.text)
        
    #print(Output)
    #update.message.reply_text(Output)
    link= []
    title=[]
    for news in Output:
        
        try:
            ss1,ss2 = news.split("#")
            link.append(ss2)
            title.append(ss1)
        except:
            pass
    #print(link)
    try:
        keyboard = [[InlineKeyboardButton(title[0], url=link[0])],[InlineKeyboardButton(title[1], url=link[1])],[InlineKeyboardButton(title[2], url=link[2])]
                    ,[InlineKeyboardButton(title[3], url=link[3])],[InlineKeyboardButton(title[4], url=link[4])]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)
    except:
        update.message.reply_text('News Unavailable')
        

            
def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')
def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Thank you.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def NEEWS():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("457762085:AAE9eFQrFHOq-OJoEyMLCx2O85kGpl3sEY4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    print("Pre-Stage - 5")
    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, start)],#CommandHandler('News', start)],

        states={

            News: [MessageHandler(Filters.text, NEWS),
                    CommandHandler('skip', skip_photo)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )


    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(button))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



