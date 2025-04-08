import telebot
from telebot import types
# Вставьте ваш токен сюда
TOKEN = '7676791138:AAHB4b3SHxMvIZHTMBVHzoMTP2xzCaRubTs'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("человек-человек")
    button2 = types.KeyboardButton("человек-техника")
    button3 = types.KeyboardButton("человек-знак")
    button4 = types.KeyboardButton("человек-природа")
    button5 = types.KeyboardButton("человек-исскувство")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Привет! я хочу помочь тебе с выбором будущей профессии и узнать о ней.")
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите раздел климова в клавиатуре", reply_markup=markup)

@bot.message_handler(commands=['Chelovek'])
def start(message):
    # Создаем клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Врач")
    button2 = types.KeyboardButton("Адвокат")
    button3 = types.KeyboardButton("Учитель")
    button4 = types.KeyboardButton("Менеджер проектов")
    button5 = types.KeyboardButton("Психолог")
    markup.add(button1, button2, button3, button4, button5)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите профессию:", reply_markup=markup)

@bot.message_handler(commands=['Tech'])
def start(message):
    # Создаем клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Врач")
    button2 = types.KeyboardButton("Адвокат")
    button3 = types.KeyboardButton("Учитель")
    button4 = types.KeyboardButton("Менеджер проектов")
    markup.add(button1, button2, button3, button4)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите профессию:", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "человек-человек":
        bot.send_message(message.chat.id, "данный раздел посвещён профессиям которые работают с людьми")
        bot.send_message(message.chat.id, "введите эту команду: /Chelovek")
    elif message.text == "Врач":
        bot.send_message(message.chat.id, "- **Описание профессии**: Эти специалисты занимаются диагностикой и лечением заболеваний у пациентов.")
        bot.send_message(message.chat.id, "- **Образование**: Необходима степень в области медицины и прохождение резидентуры.")
        bot.send_message(message.chat.id, "- **Средняя заработная плата**: Варируется от 1,0–3,0 млнв год в зависимости от специальности.")
    elif message.text == "Адвокат":
        bot.send_message(message.chat.id, "- **Описание профессии**: Адвокат — специалист по юридической защите граждан или организаций, в частности, в суде. Это независимый профессиональный помощник по правовым вопросам. ")
        bot.send_message(message.chat.id, "- **Образование**: Для получения статуса адвоката в Российской Федерации нужно высшее юридическое образование по специальности «Юриспруденция» или «Правоведение» ")
        bot.send_message(message.chat.id, "- **Средняя заработная плата**: Около 1 200 000–3 000 000 рублей в год")
    elif message.text == "Учитель":
        bot.send_message(message.chat.id, "-**Описание профессии**:Учитель — это специалист в области образования, который занимается обучением и воспитанием детей, подростков или взрослых. ")
        bot.send_message(message.chat.id, "-**Образование**:Высшее образование ,Педагогическое образование — знание методик преподавания, психологии и педагогики.")
        bot.send_message(message.chat.id, "-**Средняя заработная плата**:Около 480,000–720,000 рублей в год")
    elif message.text == "Менеджер проектов":
        bot.send_message(message.chat.id, "- **Описание профессии**: Менеджеры проектов организуют и управляют проектами от начала до завершения, координируя команды и ресурсы.")
        bot.send_message(message.chat.id, "- **Образование**: Образование в области управления или специфическое обучение проектному управлению.")
        bot.send_message(message.chat.id, "- **Средняя заработная плата**: Около 800,000–2,0 млн в год.")
    elif message.text == "Психолог":
        bot.send_message(message.chat.id, "Zov")
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, "Вы нажали Кнопку 2!")
    elif message.text == "Кнопка 3":
        bot.send_message(message.chat.id, "Вы нажали Кнопку 3!")
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, "Вы нажали Кнопку 2!")
    elif message.text == "Кнопка 3":
        bot.send_message(message.chat.id, "Вы нажали Кнопку 3!")
    else:
        bot.send_message(message.chat.id, "Я не знаю такой команды.")
# Запуск бота
bot.polling()