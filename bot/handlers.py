from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.api import save_user
from bot.keyboards import keyboard
from bot.states import Survey
from bot.survey import (
    COURSES,
    SPECIALIZATIONS,
    PRICE,
    LOCATIONS,
    LANGUAGES,
)

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):

    await state.clear()

    await message.answer(
        "👋 Welcome!\n\n"
        "Answer 5 questions so I can send you only the news that interests you.\n\n"
        "What year of study are you in?",
        reply_markup=keyboard(COURSES)
    )

    await state.set_state(Survey.course)


@router.message(Survey.course)
async def course(message: Message, state: FSMContext):

    await state.update_data(
        course=[message.text]
    )

    await message.answer(
        "What field are you interested in?",
        reply_markup=keyboard(SPECIALIZATIONS)
    )

    await state.set_state(Survey.specialization)


@router.message(Survey.specialization)
async def specialization(message: Message, state: FSMContext):

    await state.update_data(
        specialization=[message.text]
    )

    await message.answer(
        "Which conditions are acceptable for you to participate in?",
        reply_markup=keyboard(PRICE)
    )

    await state.set_state(Survey.price)


@router.message(Survey.price)
async def price(message: Message, state: FSMContext):

    await state.update_data(
        price=message.text
    )

    await message.answer(
        "Where would you like to attend events?",
        reply_markup=keyboard(LOCATIONS)
    )

    await state.set_state(Survey.location)


@router.message(Survey.location)
async def location(message: Message, state: FSMContext):

    await state.update_data(
        location=[message.text]
    )

    await message.answer(
        "What language would you like the programs to be in?",
        reply_markup=keyboard(LANGUAGES)
    )

    await state.set_state(Survey.language)


@router.message(Survey.language)
async def language(message: Message, state: FSMContext):

    await state.update_data(
        language=[message.text]
    )

    filters = await state.get_data()

    await save_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        filters=filters
    )

    await message.answer(
        "✅ Your preferences have been saved!\n\n"
        "From now on, I'll automatically send you only the news that matches your interests."
    )

    await state.clear()