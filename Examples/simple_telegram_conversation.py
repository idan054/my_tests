import telegram
import telegram.ext
import re
from random import randint

# The API Key we received for our bot
API_KEY = "1716216836:AAHaYm_taR2b4sIEPpn6CXOduv6P9HNU5Jo"
# Create an updater object with our API Key
updater = telegram.ext.Updater(API_KEY)
# Retrieve the dispatcher, which will be used to add handlers
dispatcher = updater.dispatcher
# Our states, as integers
WELCOME = 0
QUESTION = 1

# The entry function
def start(last_update, context):
    # send the question, and show the keyboard markup (suggested answers)
    last_update.message.reply_text("שלום לך! תרצה לקבל הודעה כשמשתמש סטיפס מחובר?",
        reply_markup=telegram.ReplyKeyboardMarkup([['Yes', 'No']], one_time_keyboard=True)
    )
    # go to the WELCOME state
    return WELCOME


# in the WELCOME state, check if the user wants to answer a question
def welcome(last_update, context):
    if last_update.message.text.lower() in ['yes', 'y']:
        # send question, and go to the QUESTION state
        last_update.message.reply_text(f"סבבה, אנא שלח לי קישור של המשתמש סטיפס (יש להכנס דרך האתר)")
        return QUESTION
    else:
        # go to the CANCEL state
        return CANCEL

# in the QUESTION state
def question(last_update, context):
    if "stips.co.il/profile/" in last_update.message.text:
        # correct answer, ask the user if he found tutorial helpful, and go to the CORRECT state
        last_update.message.reply_text("הקישור התקבל")
        last_update.message.reply_text("כדי להוסיף משתמשים נוספים לחץ\n /is_online")
        return CORRECT
    else:
        # wrong answer, reply, send a new question, and loop on the QUESTION state
        last_update.message.reply_text("נראה שזה לא הקישור הנכון...\n"
                                      "הקישור צריך להראות כך:ֿֿֿֿֿֿ\n stips.co.il/profile/123456\n"
                                      "אנא נסה שנית או לחץ /cancel ליציאה")
        return QUESTION

def cancel(last_update, context):
    # get the user's first name
    first_name = last_update.message.from_user['first_name']
    last_update.message.reply_text(
        f"הפעולה בוטלה, {first_name}", reply_markup=telegram.ReplyKeyboardRemove()
    )
    return telegram.ext.ConversationHandler.END

# a regular expression that matches yes or no
yes_no_regex = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)
# Create our ConversationHandler, with only one state
handler = telegram.ext.ConversationHandler(
      entry_points=[telegram.ext.CommandHandler('is_online', start)],
      states={
            WELCOME: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(yes_no_regex), welcome)],
            QUESTION: [telegram.ext.MessageHandler(~telegram.ext.Filters.command, question)],
      },
      fallbacks=[telegram.ext.CommandHandler('cancel', cancel)],
      )
# add the handler to the dispatcher
dispatcher.add_handler(handler)
# start polling for updates from Telegram
updater.start_polling()
# block until a signal (like one sent by CTRL+C) is sent
updater.idle()