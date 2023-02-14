from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# MAIN KEYBOARD

pay_one_month_button = InlineKeyboardButton(text="на 1 мес - 50$", callback_data="pay first")
pay_three_month_button = InlineKeyboardButton(text="на 3 мес - 130$", callback_data="pay second")
help_button = InlineKeyboardButton(text="Помощь", callback_data="help_")
main_menu_keyboard = InlineKeyboardMarkup().add(pay_one_month_button, pay_three_month_button).add(help_button)

# FIRST PAYMENT MENU KEYBOARD

check_payment_one = InlineKeyboardButton(text="Проверить оплату", callback_data="check_payment_one")
back_menu = InlineKeyboardButton(text="Назад", callback_data="back_menu")
bill_keyboard_one = InlineKeyboardMarkup().add(check_payment_one, back_menu)

# SECOND PAYMENT MENU KEYBOARD

check_payment_second = InlineKeyboardButton(text="Проверить оплату", callback_data="check_payment_second")
bill_keyboard_second = InlineKeyboardMarkup().add(check_payment_second, back_menu)


# JUST BACK KEYBOARD

back_keyboard = InlineKeyboardMarkup().add(back_menu)

# FSM KEYBOARD

back_FSM = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Отмена", callback_data="back"))