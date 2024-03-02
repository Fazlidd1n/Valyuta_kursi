from aiogram import types
from bot.button.reply import *
from bot.text import *
from bot.state import *
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from db.model import User, session
from dispatcher import dp, bot
from datetime import date


@dp.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await bot.send_message(2045036931,
                           f"🟢 🔔\n Yangi foydalanuvchi : {msg.from_user.full_name}\n username : {msg.from_user.username}")
    await msg.answer(f"{msg.from_user.full_name}{begin_text}", reply_markup=main_menu())
    User.insert(Base, msg.from_user.id, msg.from_user.full_name, msg.from_user.username)
    print(f"👤 - {msg.from_user.full_name}")
    await state.set_state(Menu.menu)


@dp.message(Command("ismoilov"))
async def reklama_handler(msg: Message, state: FSMContext):
    if msg.from_user.id == 2045036931:
        await msg.answer("Reklama xabarini yuboring ⤵️")
        await state.set_state(Menu.reklama)
    else:
        await msg.answer("Siz admin emassiz ❗️")
        await state.set_state(Menu.menu)


@dp.message(Menu.reklama)
async def reklama_handler(msg: Message, state: FSMContext):
    users = session.query(User)
    for user in users:
        await msg.copy_to(user.user_id)
    await state.set_state(Menu.menu)


@dp.message(Menu.menu)
async def menu_handler(msg: Message, state: FSMContext):
    if msg.text == 'Valyuta kurslari 📊':
        await msg.answer(f"{date.today()}{courses}")
    elif msg.text == "Valyuta hisoplash 🧮":
        await msg.answer("Sizga kerak bo'lgan valyutani tanlang ⤵️", reply_markup=val_btn())
        await state.set_state(Menu.type)
    else:
        await msg.answer("Tugmalardan birini tanlang ⤵️", reply_markup=main_menu())
        await state.set_state(Menu.menu)


a = []


@dp.callback_query(
    lambda call: call.data in ('Aqsh', 'Euro', 'Rossiya', 'Angliya', 'Shveytsariya', 'Yaponiya', 'Qozog‘iston'),
    Menu.type)
async def val_type_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Xizmat turini tanlang ⤵️", reply_markup=val_type())
    a.append(call.data)
    await state.set_state(Menu.val)


@dp.callback_query(lambda val_type: val_type.data in ('buy', 'sell'), Menu.val)
async def val_handler(val_type: types.CallbackQuery, state: FSMContext):
    print(val_type.data)
    await val_type.message.answer(f"💵 {val_type.data} - pul miqdorini kiriting:\nMasalan: 100")
    if val_type.data == 'buy':
        a.append(0)
    elif val_type.data == 'sell':
        a.append(1)
    await state.set_state(Menu.cal)


@dp.message(Menu.cal)
async def cal_handler(msg: Message, state: FSMContext):
    if msg.text.isdigit():
        await msg.answer(f"✅ Natija : {int(msg.text) * calculate(a[-2], a[-1])} so'm")
        await state.set_state(Menu.menu)
    else:
        await msg.answer(f"❌ Valyutalani birini tanlang va son kiriting ❗️ ", reply_markup=val_btn())
        await state.set_state(Menu.val)
