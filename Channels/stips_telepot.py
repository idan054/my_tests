import telebot # pip3 install PyTelegramBotAPI
from pprint import pprint

bot = telebot.TeleBot("1716216836:AAHaYm_taR2b4sIEPpn6CXOduv6P9HNU5Jo")
# print(bot.get_me())
# print(bot.get_updates(limit=1))

@bot.message_handler(commands=['is_online'])
def send_welcome(message):
    # bot.reply_to(message, "Howdy, how are you doing?")
    user_id = message.from_user.id
    bot.send_message(user_id,
                    "קבל התראה כשמשתמש סטיפס מחובר!\n"
                    "שלח לי קישור לפרופיל של המשתמש (יש להכנס לאתר)"
                     )
    bot.send_photo(user_id, "https://i.ibb.co/gWj7tB1/stips-copy-link.jpg")

# @bot.poll_handler()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    pprint(message)

def handle_messages(messages):
	for message in messages:
		# Do something with the message
		bot.reply_to(message, 'Hi')
bot.set_update_listener(handle_messages)
bot.polling()

