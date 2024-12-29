from telegram.ext import Updater, MessageHandler, Filters

# Bot tokeningizni shu yerga yozing
BOT_TOKEN = "7881144852:AAH8Qy46oi02u9FlRls4TgyNiM2j6O24zKk"

# Guruh chat ID'sini shu yerga yozing
GROUP_CHAT_ID = "@All_country_kyc"

def forward_to_group(update, context):
    # Kiritilgan xabarni guruhga yuboradi
    context.bot.send_message(chat_id=GROUP_CHAT_ID, text=update.message.text)

# Botni sozlash
updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Faqat matnli xabarlarni tutadi va guruhga yo‘naltiradi
dispatcher.add_handler(MessageHandler(Filters.text, forward_to_group))

# Botni ishga tushirish
print("Bot ishlamoqda...")
updater.start_polling()
updater.idle()
