import telebot 
from telebot import types 

TOKEN = "6826991262:AAGPop1oewiEfVYO2QVb9-ID68ntq2RWks4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
       markup = types.ReplyKeyboardMarkup()
       button_1 = types.KeyboardButton("Перейти на сайт")
       markup.row(button_1)
       button_2 = types.KeyboardButton("Изменить цвет" )
       markup.row(button_2)
       button_3 = types.KeyboardButton("Удалить фото" )
       markup.row(button_3)
       bot.reply_to(message , "Какое красивое фото" )
       bot.send_message(message.chat.id , 'Privet' , reply_markup=markup)
       bot.register_next_step_handler(message , on_click)
       
def on_click(message):
       if message.text == "Перейти на сайт":
              bot.send_message(message.chat.id , "Website is open")
       elif message.text == "Удалить фото":
              bot.send_message(message.chat.id , "Photo deleted")
              

@bot.message_handler(content_types=['photo'])
def get_photo(message):
       markup = types.InlineKeyboardMarkup()
       button_1 = types.InlineKeyboardButton("Купить руль на бэху" , url = "https://cars.av.by/bmw/x5m/106369602")
       markup.row(button_1)
       button_2 = types.InlineKeyboardButton("Изменить цвет" , callback_data='edit')
       markup.row(button_2)
       button_3 = types.InlineKeyboardButton("Удалить фото" , callback_data='delete')
       markup.row(button_3)
       bot.reply_to(message , "Какое красивое фото" , reply_markup=markup)
       
@bot.callback_query_handler(func = lambda callback : True)
def callback_message(callback):
       if callback.data == 'delete':
              bot.delete_message(callback.message.chat.id , callback.message.message_id - 1)
       elif callback.data == 'edit':
              bot.edit_message_text('Edit text' , callback.message.chat.id , callback.message.message_id)             



bot.polling(non_stop=True)
       
