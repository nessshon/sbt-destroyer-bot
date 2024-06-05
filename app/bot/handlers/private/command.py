from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_tonconnect import ATCManager

from app.bot.handlers.private.windows import Window
from app.bot.manager import Manager, SendMode

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command("start"))
async def start_command(message: Message, manager: Manager, atc_manager: ATCManager) -> None:
    if not manager.account_wallet:
        await Window.select_language(manager, send_mode=SendMode.SEND)

    else:
        await Window.main_menu(
            manager,
            account_wallet=atc_manager.user.account_wallet,
            send_mode=SendMode.SEND,
        )

    await manager.delete_message(message)
