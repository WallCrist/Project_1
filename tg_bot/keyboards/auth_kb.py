from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Register")]
    ],
    resize_keyboard=True)

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 My Todos")],
        [KeyboardButton(text="➕ Add Todo"), KeyboardButton(text="✅ Done Todo")]
    ],
    resize_keyboard=True)
