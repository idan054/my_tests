import telegram_send

def telegram_printer(text):
    # print("----------------------------")
    print("Also available on Telegram!")
    # print(text)
    telegram_send.send(messages=[text])
    print("----------------------------")