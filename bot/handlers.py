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
        "👋 Добро пожаловать!\n\n"
        "Ответьте на 5 вопросов, чтобы я мог отправлять только интересные вам новости.\n\n"
        "На каком курсе вы учитесь?",
        reply_markup=keyboard(COURSES)
    )

    await state.set_state(Survey.course)


@router.message(Survey.course)
async def course(message: Message, state: FSMContext):

    await state.update_data(
        course=[message.text]
    )

    await message.answer(
        "Какая у вас специализация?",
        reply_markup=keyboard(SPECIALIZATIONS)
    )

    await state.set_state(Survey.specialization)


@router.message(Survey.specialization)
async def specialization(message: Message, state: FSMContext):

    await state.update_data(
        specialization=[message.text]
    )

    await message.answer(
        "Какие мероприятия вас интересуют?",
        reply_markup=keyboard(PRICE)
    )

    await state.set_state(Survey.price)


@router.message(Survey.price)
async def price(message: Message, state: FSMContext):

    await state.update_data(
        price=message.text
    )

    await message.answer(
        "Какая локация вас интересует?",
        reply_markup=keyboard(LOCATIONS)
    )

    await state.set_state(Survey.location)


@router.message(Survey.location)
async def location(message: Message, state: FSMContext):

    await state.update_data(
        location=[message.text]
    )

    await message.answer(
        "На каком языке вы хотите получать новости?",
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
        "✅ Анкета сохранена!\n\n"
        "Теперь я буду автоматически присылать только те новости, "
        "которые соответствуют вашим интересам."
    )

    await state.clear()