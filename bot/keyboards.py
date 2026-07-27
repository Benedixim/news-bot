from aiogram.utils.keyboard import ReplyKeyboardBuilder


def keyboard(items):

    builder = ReplyKeyboardBuilder()

    for item in items:
        builder.button(text=item)

    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True
    )