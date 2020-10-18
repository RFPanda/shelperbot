#!/usr/bin/python3
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-
import telebot
import config
import datetime
import requests
from bs4 import BeautifulSoup as BS
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['exm'])
def exm(message):
    bot.reply_to(message, "1. Математический анализ - Миронова\n\
2. Линейная алгебра - Комиссарова\n\
3. Основы программирования - Бикмурзина\n\
4. Информатика - Пикулева")

@bot.message_handler(commands=['week'])
def week(message):
    r = requests.get("https://localdrop.ga/r.php")
    html = BS(r.content, 'html.parser')
    rez = html.find("div", id="Week").text
    bot.reply_to(message, rez)

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "https://telegra.ph/Pin-4103-10-01")

@bot.message_handler(commands=['donate'])
def donate(message):
    markup = types.InlineKeyboardMarkup(row_width=1) 
    item1 = types.InlineKeyboardButton("Donate", url="https://linkli.ga/paytokhasanov")
    markup.add(item1)
    bot.send_message(message.chat.id,"На хостинг и кофе админу 💰", reply_markup=markup)
   
@bot.message_handler(commands=['grouplist'])
def group_list(message):
    bot.reply_to(message,"Группа 4103\n\n\
1.   Абдрахимов Шамиль Ильдарович\n\
2.   Абдулхаев Роберт Ринатович\n\
3.   Гараев Булат Маратович\n\
4.   Горбова Дарья Дмитриевна\n\
5.   Гудин Александр Александрович\n\
6.   Душин Александр Александрович\n\
7.   Карпиков Данила Владиславович\n\
8.   Костенко Максим Павлович\n\
9.   Мотыгуллин Нияз Данилович\n\
10.  Мусин Булат Русланович\n\
11.  Сергеева Екатерина Олеговна\n\
12.  Хакимов Рамиль Радикович\n\
13.  Хасанов Адель Ильназович\n\
14.  Хасанов Айнур Альфредович\n\
15.  Шакуров Рамиль Ринатович\n\
16.  Шаронов Владимир Алексеевич\n\
17.  Шашурин Павел Дмитриевич")

@bot.message_handler(commands=['book'])
def ss(message):
    markup = types.InlineKeyboardMarkup(row_width=2) 
    item1 = types.InlineKeyboardButton("Лин Ал - задачник", url="https://drive.google.com/file/d/1Icu-akxZmfyKzO9TPw8-z1STJV-vKOnh/view")
    item2 = types.InlineKeyboardButton("Лин Ал - учебник", url='https://drive.google.com/file/d/1AMuFvS9wLU7SmpAZww846jlAt37hHQmS/view')
    item3 = types.InlineKeyboardButton("Мат Анализ - задачник", url='https://drive.google.com/file/d/1OU5eVStHfZVBq1HhK3E5H8BNvIOJ97zc/view?usp=drivesdk')
    item4 = types.InlineKeyboardButton("Англ Яз - учебник", url='https://drive.google.com/file/d/1sKBjdYeY-RJWaWX8Qfl8vb2LtqS9FCS-/view?usp=drivesdk')
    item5 = types.InlineKeyboardButton("Физика - задачник", url="https://drive.google.com/file/d/1xfgMAdoKl4472jsDjr0tn5oVnwNEoV8y/view")
    markup.add(item1, item2,item3, item4, item5)
    bot.send_message(message.chat.id, '📚 Учебный материал:', reply_markup=markup)



@bot.message_handler(commands=['r'])
def ras(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("На сегодня", callback_data='today')
    item2 = types.InlineKeyboardButton("На завтра", callback_data='next')
    item3 = types.InlineKeyboardButton("Полностью", callback_data='all')
    markup.add(item1, item2,item3)
    bot.send_message(message.chat.id, '📃 Расписание:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

            if call.data == 'today':
                date = datetime.datetime.today()
                if date.weekday() == 0:
                    bot.send_message(call.message.chat.id, "<b>📌Понедельник📌</b>\n\n \
➤ ⌛08:00 лек Линейная алгебра и аналитическая геометрия 403 7 зд.\n \
➤ неч ⌛09:40 лек Основы программирования 403 7 зд.\n \
➤ чет ⌛09:40 лек Информатика и основы информационных технологий 403 7 зд.\n \
➤ ⌛11:20 лек Философия 419 7 зд.\n \
➤ чет ⌛13:30 лек Введение в профессиональную деятельность 403 7 зд." \
                                                            , parse_mode='html')
                elif date.weekday() == 1:
                    bot.send_message(call.message.chat.id, "<b>📌Вторник📌</b>\n\n\
➤ ⌛08:00 пр Физическая культура - КАИ ОЛИМП\n \
➤ ⌛09:40 лек Математический анализ 419 2 зд.\n \
➤ неч ⌛11:20 пр Физика 301а 2 зд.",\
                                                            parse_mode='html')
                elif date.weekday() == 2:
                    bot.send_message(call.message.chat.id, "<b>📌Среда📌</b>\n\n \
➤ неч ⌛09:40 л.р. Физика 309 2 зд.\n \
➤ неч ⌛11:20 пр Философия 506 2 зд.\n \
➤ чет ⌛11:20 пр Математический анализ 424 2 зд.\n \
➤ ⌛13:30 пр Математический анализ 424 2 зд." \
                                                            ,parse_mode='html')
                elif date.weekday() == 3:
                    bot.send_message(call.message.chat.id, "<b>📌Четверг📌</b>\n\n \
➤ ⌛09:40 пр Линейная алгебра и аналитическая геометрия 329 7 зд.\n \
➤ чет ⌛11:20 л.р. Основы программирования 343 7 зд.\n \
➤ неч ⌛11:20 л.р. Информатика и основы информационных технологий 437 7 зд." \
                                                            ,parse_mode='html')
                elif date.weekday() == 4:
                    bot.send_message(call.message.chat.id, "<b>📌Пятница📌</b>\n\n\
➤ чет ⌛08:00 пр Физическая культура -КАИ ОЛИМП\n \
➤ неч ⌛08:00 лек Физическая культура и спорт лекционный зал №2 2 зд.\n\
➤ ⌛09:40 пр Иностранный язык 241 8 зд.\n \
➤ неч ⌛11:20 пр Иностранный язык 241 8 зд.\n \
➤ чет ⌛11:20 лек Физика 230 2 зд.", \
                                                            parse_mode='html')
                elif date.weekday() == 5:
                    bot.send_message(call.message.chat.id, "<b>📌Суббота📌</b>\n\n➤ Выходной!", parse_mode='html')
                elif date.weekday() == 6:
                    bot.send_message(call.message.chat.id, "<b>📌Воскресенье📌</b>\n\n➤ Выходной!", parse_mode='html')
            elif call.data == 'next':
                date1 = datetime.datetime.today()
                delta = datetime.timedelta(days = 1)
                date = date1 + delta
                if date.weekday() == 0:
                    bot.send_message(call.message.chat.id, "<b>📌Понедельник📌</b>\n\n \
➤ ⌛08:00 лек Линейная алгебра и аналитическая геометрия 403 7 зд.\n \
➤ неч ⌛09:40 лек Основы программирования 403 7 зд.\n \
➤ чет ⌛09:40 лек Информатика и основы информационных технологий 403 7 зд.\n \
➤ ⌛11:20 лек Философия 419 7 зд.\n \
➤ чет ⌛13:30 лек Введение в профессиональную деятельность 403 7 зд." \
                                                            , parse_mode='html')
                elif date.weekday() == 1:
                    bot.send_message(call.message.chat.id, "<b>📌Вторник📌</b>\n\n \
➤ ⌛08:00 пр Физическая культура - КАИ ОЛИМП\n \
➤ ⌛09:40 лек Математический анализ 419 2 зд.\n \
➤неч ⌛11:20 пр Физика 301а 2 зд.", \
                                                            parse_mode='html')
                elif date.weekday() == 2:
                    bot.send_message(call.message.chat.id, "<b>📌Среда📌</b>\n\n\
➤ неч ⌛09:40 л.р. Физика 309 2 зд.\n \
➤ неч ⌛11:20 пр Философия 506 2 зд.\n \
➤ чет ⌛11:20 пр Математический анализ 424 2 зд.\n \
➤ ⌛13:30 пр Математический анализ 424 2 зд."\
                                                            ,parse_mode='html')
                elif date.weekday() == 3:
                    bot.send_message(call.message.chat.id, "<b>📌Четверг📌</b>\n\n \
➤ ⌛09:40 пр Линейная алгебра и аналитическая геометрия 329 7 зд.\n \
➤ чет ⌛11:20 л.р. Основы программирования 343 7 зд.\n \
➤ неч ⌛11:20 л.р. Информатика и основы информационных технологий 437 7 зд."\
                                                            ,parse_mode='html')
                elif date.weekday() == 4:
                    bot.send_message(call.message.chat.id, "<b>📌Пятница📌</b>\n\n \
➤ чет ⌛08:00 пр Физическая культура -КАИ ОЛИМП\n \
➤ неч ⌛08:00 лек Физическая культура и спорт лекционный зал №2 2 зд.\n \
➤ ⌛09:40 пр Иностранный язык 241 8 зд.\n \
➤ неч ⌛11:20 пр Иностранный язык 241 8 зд.\n \
➤ чет ⌛11:20 лек Физика 230 2 зд." \
                                                            ,parse_mode='html')
                elif date.weekday() == 5:
                    bot.send_message(call.message.chat.id, "Суббота - выходной! Но вот тебе расписание на понедельник!")
                    bot.send_message(call.message.chat.id, "<b>📌Понедельник📌</b>\n\n \
➤ ⌛08:00 лек Линейная алгебра и аналитическая геометрия 403 7 зд.\n \
➤ неч ⌛09:40 лек Основы программирования 403 7 зд.\n \
➤ чет ⌛09:40 лек Информатика и основы информационных технологий 403 7 зд.\n \
➤ ⌛11:20 лек Философия 419 7 зд.\n \
➤ чет ⌛13:30 лек Введение в профессиональную деятельность 403 7 зд." \
                                                            ,parse_mode='html')
                elif date.weekday() == 6:
                    bot.send_message(call.message.chat.id, "Воскресенье - выходной! Но вот тебе расписание на понедельник!")
                    bot.send_message(call.message.chat.id, "<b>📌Понедельник📌</b>\n\n \
➤ ⌛08:00 лек Линейная алгебра и аналитическая геометрия 403 7 зд.\n \
➤ неч ⌛09:40 лек Основы программирования 403 7 зд.\n \
➤ чет ⌛09:40 лек Информатика и основы информационных технологий 403 7 зд.\n \
➤ ⌛11:20 лек Философия 419 7 зд.\n \
➤ чет ⌛13:30 лек Введение в профессиональную деятельность 403 7 зд." \
                                                            ,parse_mode='html')
            elif call.data == 'all':
                bot.send_message(call.message.chat.id, "📌<b>Понедельник📌</b>\n\n\
➤ ⌛08:00 лек Линейная алгебра и аналитическая геометрия 403 7 зд.\n\
➤ неч ⌛09:40 лек Основы программирования 403 7 зд.\n\
➤ чет ⌛09:40 лек Информатика и основы информационных технологий 403 7 зд.\n\
➤ ⌛11:20 лек Философия 419 7 зд.\n\
➤ чет ⌛13:30 лек Введение в профессиональную деятельность 403 7 зд.\
\n\n<b>📌Вторник📌</b>\n\n\
➤ ⌛08:00 пр Физическая культура - КАИ ОЛИМП\n\
➤ ⌛09:40 лек Математический анализ 419 2 зд.\n\
➤неч ⌛11:20 пр Физика 301а 2 зд.\
\n\n<b>📌Среда📌</b>\n\n\
➤ неч ⌛09:40 л.р. Физика 309 2 зд.\n\
➤ неч ⌛11:20 пр Философия 506 2 зд.\n\
➤ чет ⌛11:20 пр Математический анализ 424 2 зд.\n\
➤ ⌛13:30 пр Математический анализ 424 2 зд.\
\n\n<b>📌Четверг📌</b>\n\n\
➤ ⌛09:40 пр Линейная алгебра и аналитическая геометрия 329 7 зд.\n\
➤ чет ⌛11:20 л.р. Основы программирования 343 7 зд.\n\
➤ неч ⌛11:20 л.р. Информатика и основы информационных технологий 437 7 зд.\
\n\n<b>📌Пятница📌</b>\n\n\
➤ чет ⌛08:00 пр Физическая культура -КАИ ОЛИМП\n\
➤ неч ⌛08:00 лек Физическая культура и спорт лекционный зал №2 2 зд.\n\
➤ ⌛09:40 пр Иностранный язык 241 8 зд.\n\
➤ неч ⌛11:20 пр Иностранный язык 241 8 зд.\n\
➤ чет ⌛11:20 лек Физика 230 2 зд.\
\n\n<b>📌Суббота📌</b>\n\n➤ Выходной!"\
                                                            , parse_mode='html')
            #elif call.data == "test":
            #    bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Моё почтение!")
             
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Расписание:' ,reply_markup=None)
            
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Грация!")
    except Exception as e:
        print(repr(e))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я понимаю лишь те команды которым меня научили. 🥺")


bot.polling(none_stop=True)