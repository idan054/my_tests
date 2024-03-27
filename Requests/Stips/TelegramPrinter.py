import telegram_send

async def telegram_printer(text):
    # print("----------------------------")
    print("Also available on Telegram!")
    # print(text)
    await telegram_send.send(messages=[text])
    print("----------------------------")