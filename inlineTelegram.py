import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler,Filters, RegexHandler
from TelegramCricbuzz import Cricket, sendID

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

button1=0
SS = 1
def start(bot, update):
    names = Cricket()
    names1 = names.match()
    nameList = names1[0]
    idlist = names1[1]
    #print(nameList)
    #print(idlist)
    keyboard = [[InlineKeyboardButton(nameList[0], callback_data=idlist[0])],
                [InlineKeyboardButton(nameList[1], callback_data=idlist[1])],
                [InlineKeyboardButton(nameList[2], callback_data=idlist[2])],
                [InlineKeyboardButton(nameList[3], callback_data=idlist[3])],
                [InlineKeyboardButton(nameList[4], callback_data=idlist[4])]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    print("start")
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

    

def button(bot, update):
    query = update.callback_query 
    if query.data == "None":
        bot.edit_message_text(text="Select appropriate option",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
        
        
    else:
        try:
            ScoreData = sendID(query.data)
            scoreData = ScoreData.LiveScore()
            runs = scoreData[0]
            bat1 = scoreData[1]
            bat2 = scoreData[2]
            bowl1 = scoreData[3]
            bowl2 = scoreData[4]
            stat =  scoreData[5]
            bot.edit_message_text(text="{}{}{}{}{}{} \n".format(runs, bat1, bat2, bowl1, bowl2, stat),
                                  chat_id=query.message.chat_id,
                                  message_id=query.message.message_id)
            
        except Exception as e:
            print(e)
    #return ConversationHandler.END
        
def scoreboard(bot, update):
    print("Works")
    
def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Thank you.')
    #updater.stop()
    
    
    return ConversationHandler.END

    

updater = Updater("457762085:AAE9eFQrFHOq-OJoEyMLCx2O85kGpl3sEY4")

def CricMain():
    # Create the Updater and pass it your bot's token.
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    print("Pre-Stage - 5")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sb", scoreboard))
    dp.add_handler(CommandHandler("cancel", cancel))
    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
##    conv_handler = ConversationHandler(
##        entry_points=[MessageHandler(Filters.text, start)],
##        states={
##            
##            button1: [MessageHandler(Filters.text, button)],
##            
##        },  
##        fallbacks=[CommandHandler('cancel', cancel)]
##    )


    #dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(button))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    #updater.idle()

if __name__ == '__main__':
    while True:
        print('worked')
        CricMain()



