import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from random import choice

TOKEN='6093228866:AAGvkQRlUIxecIwcOs9wonQVkSXom35DJkw'

bot=telebot.TeleBot(TOKEN)

keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Дайте совет учитель'))
keyboard.add(KeyboardButton('Досвидание учитель'))
keyboard.add(KeyboardButton('О проекте'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    text='Доброе утро ученик мой, с чем пожаловал на этот раз.'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


words=['Решение принимаешь ты один. Но помнить должен ученик, что делаешь это также и за других, кто стоит за твоим плечом',
       'Быть джедаем — значит смотреть правде в глаза и выбирать. Источай свет или тьму, ученик мой. Будь свечой или ночью',
       'Решился я уверенности, что можно выиграть войну любую. Ибо сражаясь в боях, проливая кровь уже теряем мы.',
       'Смерть — это естественная часть жизни. Радуйся за тех, кто вокруг тебя ученик, кто превращается в Силу. Оплакивать их не надо. Скучать по ним не надо.',
       'Чтобы врага победить, не обязательно убивать его. Ярость, горящую в нем, одолей, и он тебе больше не враг. Ярость — вот настоящий враг.',
       'Чтобы отвечать силой на силу, путь джедая не в этом. В этой войне существует опасность потерять того, кем мы являемся.',
       'На оружие полагаешься, но оружием нельзя выйграть, ученик, сражение. Разум твой всего сильнее.',
       'Всегда много путей достичь цель есть ученик. Испробовать все должны ты.']


@bot.message_handler(regexp=r'дайте совет учитель\.*')
def say_hello(message):
    bot.send_message(message.chat.id, random.choice(words))


@bot.message_handler(regexp=r'досвидание учитель\.*')
def say_bye(message):
    text='До встречи ученик мой. Да пребудет с тобой сила.'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(regexp=r'о проекте\.*')
def say_hello(message):
    bot.send_message(message.chat.id, 'выполнил: Шенцев Алексей Максимович. Цель проекта: вдохновить людей на своершение новых хороших поступков.')


bot.infinity_polling(none_stop=True, interval=0)
