from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import aiohttp

from tg_bot.keyboards.auth_kb import start_kb, main_menu_kb

router = Router()


class RegistrationStates(StatesGroup):
    waiting_for_email = State()
    waiting_for_confirmation = State()

@router.message(Command("start"))
async def start(message: Message):
    user_id = message.from_user.id

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8000/users/{user_id}") as response:
            if response.status == 404:
                await message.answer(
                    "Welcome! Please register to use BOT",
                    reply_markup=start_kb
                )

            else:
                await message.answer(
                    "Welcome back! Choose an option:",
                    reply_markup=main_menu_kb
                )

@router.message(F.text == "📝 Register")
async def register_handler(message: Message, state:FSMContext):
    await state.set_state(RegistrationStates.waiting_for_email)
    await message.answer("Please enter your email:")

@router.message(RegistrationStates.waiting_for_email)
async def email_handler(message: Message, state:FSMContext):
    email = message.text
    username = message.from_user.username
    user_id = message.from_user.id

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"http://localhost:8000/users/",
            json={
                "email": email,
                "username": username,
                "password": str(user_id)
            }
        ) as response:
            if response.status == 200:
                await state.clear()
                await message.answer(
                    "Registration successful! You can now use the todo list",
                    reply_markup=main_menu_kb
                )
            else:
                await message.answer("Registration failed! Please try again!")
