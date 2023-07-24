# coding=utf-8
import telebot
from ImageProcessing import *
import os

TOKEN = '6289380877:AAGMpvzsn_PVN7-2aQIrG2QvCQs-XTHt4Cc'

bot = telebot.TeleBot(TOKEN)
bot_alias = '@' + bot.get_me().username

@bot.message_handler(commands=['start'])
def startPrivet(message):
    texts = "Здраствуй, это бот который может обработать фотографию.\nПришлите фотографию документом!"
    bot.send_message(chat_id=message.chat.id, text=texts)


@bot.message_handler(content_types=['document'])
def handleDoc(message):
    print(message.chat.id)
    save_dir = os.getcwd()
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    file_name = message.from_user.username + file_name
    print(file_name)
    with open(save_file + "/"+ file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Ещё немного...')
    url = image_processing(file_name)
    with open(url, 'rb') as doc:
        bot.send_document(message.chat.id, doc)
##332467990
@bot.message_handler(content_types=['photo'])
def handleImg(message):
    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = file_info.file_path
    file_name = file_name[file_name.rindex('/')+1:]
    file_name = message.from_user.username + file_name
    print(file_name)
    src = save_file + "/" + file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Ещё немного...')
    url = image_processing(file_name)
    print(file_name)
    with open(url, 'rb') as doc:
        bot.send_document(message.chat.id, doc)

print('start bot')
bot.polling(none_stop=True, timeout=100)
##bot.infinity_polling(True)
##while True:
##    try:
##        bot.polling()
##    except:
##        print('restart')
