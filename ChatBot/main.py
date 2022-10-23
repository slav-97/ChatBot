import telebot
from telebot import types
# Создаем экземпляр бота
#bot = telebot.TeleBot('Здесь впиши токен, полученный от @botfather')
# id_channel = "@slavusya192bot"
# bot = telebot.TeleBot('5664010376:AAGCgdKGg9L0kVAzV02gLKI3QVz5BV5NvJA')
id_channel = "@botsmaterial228"
bot = telebot.TeleBot('5664010376:AAGCgdKGg9L0kVAzV02gLKI3QVz5BV5NvJA')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    linkSite = types.InlineKeyboardButton('Посетить наш сайт', url='https://024.by/')
    addText = types.InlineKeyboardButton('Получить инструкцию', callback_data='textCallback')
    markup.add(linkSite, addText)
    mess = f'Привет, {message.from_user.first_name}. Ты можешь поделиться с нами интересными новостями, фотографиями, а также видео. При необходимости можешь перейти на наш сайт, а также ознакомиться с инструкцией по использованию нашего бота.'
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'textCallback':
            bot.send_message(call.message.chat.id, 'Напиши нам в чат, чтобы поделиться своей историей. Чтобы отправить нам изображение - перетащите его в окно чата либо добавьте его через вложения, таким же образом можно прикрепить видео')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text","new_chat_members"])
#@bot.message_handler(content_types=["new_chat_members"])
def echo_msg(message):
    # bot.send_message(id_channel, "Текст от\n*{name} {last}*\n{text}".format(name=message.chat.first_name,
    #                                                                         last=message.chat.last_name,
    #                                                                         text=message.text),
    #                  parse_mode="Markdown")
    bot.send_message(id_channel, "Текст от\n[{} {}](tg://user?id={})\n{}".format(
        message.from_user.first_name, message.from_user.last_name, message.from_user.id, message.text),
                      disable_web_page_preview=True, parse_mode="Markdown")
    # bot.send_message(message.chat.id,
    #                  "*{name} {last}*\n\nСпасибо, мы обязательно ознакомимся с тем, что вы нам написали".format(
    #                      name=message.chat.first_name, last=message.chat.last_name, text=message.text),
    #                  parse_mode="Markdown")
    bot.send_message(message.chat.id,
                    "[{} {}](tg://user?id={})\n\nСпасибо, мы обязательно ознакомимся с тем, что вы нам написали".format(
                         message.from_user.first_name, message.from_user.last_name, message.from_user.id, message.text),
                     disable_web_page_preview=True, parse_mode="Markdown")

@bot.message_handler(content_types=["photo"])
def echo_msg(message):
    photo_id = message.photo[0].file_id
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    name = message.photo[0].file_id + ".jpg"
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    # bot.send_message(id_channel,
    #                      "Фото\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name),
    #                       parse_mode="Markdown")  # от кого идет сообщение и его содержание
    bot.send_message(id_channel,
                     "Изображение от\n[{} {}](tg://user?id={})".format(
                         message.chat.first_name, message.chat.last_name, message.from_user.id),
                     disable_web_page_preview=True, parse_mode="Markdown")  # от кого идет сообщение и его содержание
    bot.send_photo(id_channel, photo_id)
    # bot.send_message(message.chat.id,
    #                   "*{name} {last}*\n\nОтправлено".format(name=message.chat.first_name, last=message.chat.last_name,
    #                                                   text=message.text),
    #                  parse_mode="Markdown")
    bot.send_message(message.chat.id,
                     "[{} {}](tg://user?id={})\n\nСпасибо за инфу".format(
                         message.chat.first_name, message.chat.last_name, message.from_user.id, message.text),
                     disable_web_page_preview=True, parse_mode="Markdown")

@bot.message_handler(content_types=["document"])
def echo_msg(message):
    document_id = message.document.file_id
    file_info2 = bot.get_file(document_id)
    downloaded_file2 = bot.download_file(file_info2.file_path)
    name2 = message.document.file_id + ".docx"
    with open(name2, 'wb') as new_file:
        new_file.write(downloaded_file2)
    #document2 = open(name2, 'rb')
    # bot.send_message(id_channel,
    #                      "Фото\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name),
    #                       parse_mode="Markdown")  # от кого идет сообщение и его содержание
    #
    bot.send_message(id_channel,
                     "Документ от\n[{} {}](tg://user?id={})".format(
                         message.chat.first_name, message.chat.last_name, message.from_user.id),
                    disable_web_page_preview=True, parse_mode="Markdown")  # от кого идет сообщение и его содержание
    bot.send_document(id_channel, document_id)
    # bot.send_message(message.chat.id,
    #                   "*{name} {last}*\n\nОтправлено".format(name=message.chat.first_name, last=message.chat.last_name,
    #                                                   text=message.text),
    #                  parse_mode="Markdown")
    bot.send_message(message.chat.id,
                     "[{} {}](tg://user?id={})\n\nСпасибо за файл".format(
                        message.chat.first_name, message.chat.last_name, message.from_user.id, message.text),
                    disable_web_page_preview=True, parse_mode="Markdown")

@bot.message_handler(content_types=["video"])
def echo_msg(message):
    raw2 = message.video.file_id
    name3 = raw2 + ".mp4"
    file_info3 = bot.get_file(raw2)
    downloaded_file3 = bot.download_file(file_info3.file_path)
    with open(name3, 'wb') as new_file:
        new_file.write(downloaded_file3)
    video2 = open(name3, 'rb')
    # bot.send_message(id_channel,
    #                  "Видео\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name),
    #                  parse_mode="Markdown")
    bot.send_message(id_channel,
                     "Видео от\n[{} {}](tg://user?id={})".format(
                         message.chat.first_name, message.chat.last_name, message.from_user.id),
                     disable_web_page_preview=True, parse_mode="Markdown")
    bot.send_video(id_channel, video2)
    # bot.send_message(message.chat.id,
    #                  "*{name} {last}*\n\nОтправлено".format(name=message.chat.first_name, last=message.chat.last_name,
    #                                                   text=message.text), parse_mode="Markdown")
    bot.send_message(message.chat.id,
                     "[{} {}](tg://user?id={})\n\nСпасибо за видео".format(
                         message.chat.first_name, message.chat.last_name, message.from_user.id, message.text),
                     disable_web_page_preview=True, parse_mode="Markdown")
# Запускаем бота
bot.polling(none_stop=True, interval=0)
#development programming

