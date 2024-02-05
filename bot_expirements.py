import telebot
import db
import mybot
bot = mybot.bot


def add_user(id, name):
    db.dbadd_user(id, name)


def add_title(title, id, name):
    db.dbadd_exercise_title(title, id, name)


def add_exercise_name(title, id, name, exercise_name):
    db.dbadd_exercise_name(title, id, name, exercise_name)


def get_exercise_name(title, id):
    return db.dbget_exercise_name(title, id)


@bot.message_handler(commands=['start'])
def start(m):
    add_user(m.chat.id, m.from_user.first_name)
    bot.reply_to(m, 'Привет! Я помогу тебе с тренировками!')
    bot.send_message(m.chat.id, 'Нажми:\n/help, если что-то непонятно\n/add чтобы добавить информацию о тренировке\n/get получить информацию о тренировке\n/change изменить данные тренировки')


@bot.message_handler(commands=['help'])
def reply_help(m):
    bot.reply_to(m, 'Нажми /add чтобы добавить информацию о тренировке\nНажмите /get чтобы получить информацию о тренировке\nНажмите /change чтобы изменить данные тренировки')


@bot.message_handler(commands=['add'])
def reply_add(m):
    msg_title = bot.reply_to(m, 'Введи название тренировки')
    bot.register_next_step_handler(msg_title, step_set_title)


def step_set_title(m):
    global user_title
    user_title = m.text
    bot.send_message(m.chat.id, 'Название добавлено')
    msg_exercise_name = bot.send_message(m.chat.id, 'Введи название упражнений через запятую и пробел')
    bot.register_next_step_handler(msg_exercise_name, step_set_exercise_name)


def step_set_exercise_name(m):
    exercise_name = m.text
    exercise_name = exercise_name.split(', ')
    add_exercise_name(user_title, m.chat.id, m.from_user.first_name, exercise_name)
    bot.send_message(m.chat.id, 'Названия добавлены')


@bot.message_handler(commands=['get'])
def reply_add(m):
    msg_title = bot.reply_to(m, 'Введи название тренировки')
    bot.register_next_step_handler(msg_title, step_get_title)


def step_get_title(m):
    user_title = m.text
    exercise_name = get_exercise_name(user_title, m.chat.id)
    for name in exercise_name:
        bot.send_message(m.chat.id, name)


@bot.message_handler(commands=['stop'])
def reply_stop(m):
    bot.stop_bot()


bot.polling()
