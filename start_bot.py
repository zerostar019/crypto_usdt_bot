from aiogram.utils import executor
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import main_menu_keyboard, bill_keyboard_one, back_keyboard, bill_keyboard_second
import FSM_check_one


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите подписку:", reply_markup=main_menu_keyboard)



@dp.callback_query_handler(lambda call: call.data == "pay first")
async def get_paid_one(callback_query: types.CallbackQuery):
    await callback_query.answer(callback_query.id)
    await callback_query.message.edit_text(text='Нажмите на текст ниже, чтобы скопировать адрес кошелька:\n\n `TGJdRBEsNkdh5JPNhFPd8RtKuDkZcmXp5M` \n\nПосле успешной оплаты нажмите кнопку "Проверить оплату"',
                                           reply_markup=bill_keyboard_one, parse_mode="MarkdownV2")


@dp.callback_query_handler(lambda call: call.data == "pay second")
async def get_paid_three(callback_query: types.CallbackQuery):
    await callback_query.answer(callback_query.id)
    await callback_query.message.edit_text(text='Нажмите на текст ниже, чтобы скопировать адрес кошелька:\n\n `TGJdRBEsNkdh5JPNhFPd8RtKuDkZcmXp5M` \n\nПосле успешной оплаты нажмите кнопку "Проверить оплату"',
                                           reply_markup=bill_keyboard_second, parse_mode="MarkdownV2")
    
FSM_check_one.register_handlers(dp)


@dp.callback_query_handler(lambda call: call.data == "help_")
async def get_help(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("В случае возникновения вопросов, обратитесь по адресу @savvagrig", reply_markup=back_keyboard)
    await callback_query.answer(callback_query.id)
    
@dp.callback_query_handler(lambda call: call.data == "back_menu")
async def back_menu(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, "Выберите подписку:", reply_markup=main_menu_keyboard)
    await callback_query.answer(callback_query.id)
 

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)