from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from db.model import Course,Base


def main_menu():
    val = KeyboardButton(text='Valyuta kurslari 📊')
    cal = KeyboardButton(text='Valyuta hisoplash 🧮')
    design = [
        [val, cal]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def val_btn():
    aqsh = InlineKeyboardButton(text='🇺🇸 AQSH', callback_data='Aqsh')
    eur = InlineKeyboardButton(text='🇪🇺 EVRO', callback_data='Euro')
    rus = InlineKeyboardButton(text='🇷🇺 Rossiya', callback_data='Rossiya')
    design = [
        [aqsh, eur, rus]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)

course_datas = Course.select(Base)
def calculate(val):
    l = {
        'Aqsh': course_datas.get("USD"),
        'Euro': course_datas.get("EUR"),
        'Rossiya': course_datas.get("RUB")
    }
    return l.get(val)
