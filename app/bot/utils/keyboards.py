from typing import Dict

from aiogram.types import InlineKeyboardMarkup as Markup
from aiogram.types import InlineKeyboardButton as Button
from aiogram.utils.keyboard import InlineKeyboardBuilder as Builder
from aiogram_tonconnect.utils.keyboards import InlineKeyboard as AiogramTonconnectInlineKeyboardBase

from .texts import TextButton
from ...texts import TEXT_BUTTONS, SUPPORTED_LANGUAGES


class AiogramTonconnectInlineKeyboard(AiogramTonconnectInlineKeyboardBase):

    @property
    def texts_buttons(self) -> Dict[str, Dict[str, str]]:
        return TEXT_BUTTONS


def select_language() -> Markup:
    builder = Builder().row(
        *[
            Button(text=text, callback_data=callback_data)
            for callback_data, text in SUPPORTED_LANGUAGES.items()
        ], width=3
    )
    return builder.as_markup()


def main_menu(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [Button(text=text_button.get("change_language"), callback_data="change_language"),
             Button(text=text_button.get("disconnect_wallet"), callback_data="disconnect_wallet")],
        ]
    )


def nft_info(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [Button(text=text_button.get("back"), callback_data="back"),
             Button(text=text_button.get("confirm"), callback_data="confirm")],
        ]
    )
