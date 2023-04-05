
import telebot
from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help',])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате:\n<имя бота>\
           <в какую валюту перевести>\
    <количество переводимой валюты>\n Увидеть список всех доступных валют : /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text ='\n'.join((text,key,))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):

    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много пораметров.')


        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except CjnvertijnException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:

      text = f'Цена {amount} {quote} в {base} - {round(float(total_base)*float(amount), 2)}'
      bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

#{amount}