from create_bot import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from keyboard import back_FSM, main_menu_keyboard, back_keyboard
from datetime import datetime
import requests
from gs import append_data
from datetime import datetime
from database import Database

db = Database()

ADDRESS = "TGJdRBEsNkdh5JPNhFPd8RtKuDkZcmXp5M"

class check_payment(StatesGroup):
    get_amount = State()
    get_hash = State()

@dp.callback_query_handler(lambda call: call.data == "check_payment")
async def first_step(callback_query: types.CallbackQuery, state=None):
    await check_payment.get_amount.set()
    await callback_query.message.edit_text("Введите сумму транзакции:", reply_markup=back_FSM)
    await bot.answer_callback_query(callback_query.id)
    
@dp.callback_query_handler(lambda call: call.data == "back", state="*")
async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback_query.message.edit_text("Добрый день!", reply_markup=main_menu_keyboard)
   

@dp.message_handler(content_types=['text'], state=check_payment.get_amount)
async def get_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
    await bot.send_message(message.from_user.id, "Введите хэш транзакции:", reply_markup=back_keyboard)
    await check_payment.next()
    

@dp.message_handler(content_types=['text'], state=check_payment.get_hash)
async def get_hash(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        amount = data['amount']
        hash_text = message.text
        if db.check_hash(hash_text=hash_text) != []:
            await bot.send_message(message.from_user.id, "❗️Данная оплата уже проходила по другому пользователю❗️", reply_markup=back_keyboard)
        elif db.check_hash(hash_text=hash_text) == []:  
            try:
                data = requests.get(f"https://apilist.tronscan.org/api/transaction-info?hash={hash_text}").json()['trc20TransferInfo']
            except:
                await bot.send_message(message.from_user.id, text="Что-то пошло не так, обратитесь в поддержку", reply_markup=back_keyboard)
            get_amount = data[0]['amount_str']
            my_address = data[0]['to_address']
            if float(amount) == float(get_amount)/10**6 and ADDRESS == str(my_address):
                await bot.send_message(message.from_user.id, text="Вы успешно оплатили", reply_markup=back_keyboard)
                db.insert_hash(hash_text=hash_text)
                append_data(username=message.from_user.username, user_id=message.from_user.id, hash_text=hash_text, amount=amount, date_time=datetime.now().strftime('%d.%m.%Y г. %H:%M:%S'))
            else:
                await bot.send_message(message.from_user.id, text="Оплата не прошла, обратитесь в поддержку", reply_markup=back_keyboard)
    await state.finish()
       
       
def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(first_step, lambda call: call.data == "check_payment", state=None)
    dp.register_callback_query_handler(cancel_handler, lambda call: call.data == "back", state="*")
    dp.register_message_handler(get_amount, state=check_payment.get_amount)
    dp.register_message_handler(get_hash, state=check_payment.get_hash)
    