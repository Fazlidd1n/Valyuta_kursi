from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from db.model import Course, Base


def main_menu():
    val = KeyboardButton(text='Valyuta kurslari 📊')
    cal = KeyboardButton(text='Valyuta hisoplash 🧮')
    design = [
        [val, cal]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def val_type():
    buy = InlineKeyboardButton(text='Sotib olish', callback_data='buy')
    sell = InlineKeyboardButton(text='Sotish', callback_data='sell')
    design = [
        [buy, sell],
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


def val_btn():
    aqsh = InlineKeyboardButton(text='🇺🇸 AQSH', callback_data='Aqsh')
    eur = InlineKeyboardButton(text='🇪🇺 EVRO', callback_data='Euro')
    rus = InlineKeyboardButton(text='🇷🇺 Rossiya', callback_data='Rossiya')
    gbp = InlineKeyboardButton(text='🇬🇧 Angliya', callback_data='Angliya')
    chf = InlineKeyboardButton(text='🇨🇭 Shveytsariya', callback_data='Shveytsariya')
    jpy = InlineKeyboardButton(text='🇯🇵 Yaponiya', callback_data='Yaponiya')
    kzt = InlineKeyboardButton(text='🇰🇿 Qozog‘iston', callback_data="Qozog‘iston")
    design = [
        [aqsh, eur, rus],
        [gbp, chf, jpy],
        [kzt, ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


course_datas = Course.select(Base)


def calculate(val, num):
    l = {
        'Aqsh': course_datas.get("USD")[num],
        'Euro': course_datas.get("EUR")[num],
        'Rossiya': course_datas.get("RUB")[num],
        'Angliya': course_datas.get("GBP")[num],
        'Shveytsariya': course_datas.get("CHF")[num],
        'Yaponiya': course_datas.get("JPY")[num],
        'Qozog‘iston': course_datas.get("KZT")[num]
    }
    return l.get(val)

##
# @dp.message(Command('start', 'restart'))
# async def start_restart_handler(msg: Message, state: FSMContext) -> None:
#     # start and start func buttons for bot
#     start = BotCommand(command='start', description='Botga start berish')
#     restart = BotCommand(command='restart', description='Botga qayta start berish')
#     await msg.bot.set_my_commands(commands=[start, restart])
#
#     user_data = {
#         'telegram_id': msg.from_user.id,
#         'first_name': msg.from_user.first_name,
#         'last_name': msg.from_user.last_name,
#         'username': msg.from_user.username
#     }
#     user: User | None = session.execute(select(User).where(User.telegram_id == msg.from_user.id)).fetchone()
#     if not user:
#         query = insert(User).values(**user_data)
#         session.execute(query)
#         session.commit()
#         await msg.answer('Salom 🤗')
#     else:
#         user = user[0]
#         if not user.last_name:
#             if not user.first_name:
#                 await msg.answer('Salom, foydalanuvchi!')
#             await msg.answer(f'Salom, {user.first_name}!')
#         else:
#             await msg.answer(f'Salom, {user.first_name} {user.last_name}')
#
#     if user:
#         if user.phone_number:
#             if msg.from_user.id in ADMINS_ID:
#                 await msg.answer("Menyuni tanlang 👇", reply_markup=admin_start_buttons())
#             else:
#                 await msg.answer("Menyuni tanlang 👇", reply_markup=start_buttons())
#             await state.set_state(UserStates.main_menu)
#         else:
#             await msg.answer('Siz bu botdan foydalanish uchun raqamingizni kiriting 👇',
#                              reply_markup=phone_number_buttons())
#             await state.set_state(UserStates.phone_number)
#     else:
#         await msg.answer('Siz bu botdan foydalanish uchun raqamingizni kiriting 👇',
#                          reply_markup=phone_number_buttons())
#         await state.set_state(UserStates.phone_number)
#
#
# # Telefon raqam ro'yhatdan o'tish
# @dp.message(UserStates.phone_number, F.contact)
# async def phone_number_handler(msg: Message, state: FSMContext):
#     phone_number = msg.contact.phone_number
#     query = update(User).where(User.telegram_id == msg.from_user.id).values(phone_number=phone_number)
#     session.execute(query)
#     session.commit()
#     for admin in ADMINS_ID:
#         await bot.send_contact(admin, phone_number, first_name=msg.from_user.full_name)
#     if msg.from_user.id in ADMINS_ID:
#         await msg.answer("Menyuni tanlang 👇", reply_markup=admin_start_buttons())
#     else:
#         await msg.answer("Menyuni tanlang 👇", reply_markup=start_buttons())
#     await state.set_state(UserStates.main_menu)
