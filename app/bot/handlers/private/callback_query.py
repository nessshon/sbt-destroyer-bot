from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram_tonconnect import ATCManager
from aiogram_tonconnect.tonconnect.models import ConnectWalletCallbacks, SendTransactionCallbacks
from pytonapi.schema.nft import NftItem

from app.bot.handlers.private.windows import Window
from app.bot.manager import Manager
from app.bot.utils.states import UserState
from app.bot.utils.texts import TextMessage, TextButton
from app.bot.utils.transactions import DestroyNFTTransaction
from app.texts import SUPPORTED_LANGUAGES

router = Router()
router.callback_query.filter(F.message.chat.type == "private")


@router.callback_query(UserState.SELECT_LANGUAGE)
async def select_language_callback_query(
        call: CallbackQuery,
        manager: Manager,
        atc_manager: ATCManager,
) -> None:
    if call.data in list(SUPPORTED_LANGUAGES.keys()):
        await manager.send_loader_message()

        await manager.state.update_data(language_code=call.data)
        await atc_manager.update_interfaces_language(call.data)

        manager.text_message = TextMessage(call.data)
        manager.text_button = TextButton(call.data)

        await atc_manager.connect_wallet(
            callbacks=ConnectWalletCallbacks(
                before_callback=Window.select_language,
                after_callback=Window.main_menu,
            ),
            check_proof=True,
        )

    await call.answer()


@router.callback_query(UserState.MAIN_MENU)
async def main_menu_callback_query(call: CallbackQuery, manager: Manager, atc_manager: ATCManager) -> None:
    if call.data == "disconnect_wallet":
        await manager.send_loader_message()
        await atc_manager.disconnect_wallet()
        await manager.state.update_data(account_wallet=None)
        await Window.select_language(manager)

    elif call.data == "change_language":
        await Window.change_language(manager)

    await call.answer()


@router.callback_query(UserState.CHANGE_LANGUAGE)
async def change_language_callback_query(call: CallbackQuery, manager: Manager, atc_manager: ATCManager) -> None:
    if call.data in list(SUPPORTED_LANGUAGES.keys()):
        await manager.state.update_data(language_code=call.data)
        await atc_manager.update_interfaces_language(call.data)

        manager.text_message = TextMessage(call.data)
        manager.text_button = TextButton(call.data)

        await Window.main_menu(manager, account_wallet=atc_manager.user.account_wallet)

    await call.answer()


@router.callback_query(UserState.NFT_INFO)
async def nft_info_callback_query(call: CallbackQuery, manager: Manager, atc_manager: ATCManager) -> None:
    if call.data == "back":
        await Window.main_menu(manager, manager.account_wallet)

    elif call.data == "confirm":
        await manager.send_loader_message()

        state_data = await manager.state.get_data()
        nft_item = NftItem(**state_data.get("nft"))

        await atc_manager.send_transaction(
            transaction=DestroyNFTTransaction(
                address=nft_item.address.to_userfriendly(True),
            ),
            callbacks=SendTransactionCallbacks(
                before_callback=Window.nft_info,
                after_callback=after_callback,
            )
        )

    await call.answer()


async def after_callback(manager: Manager, **_) -> None:
    text = manager.text_message.get("nft_destroyed")

    await Window.main_menu(
        manager,
        account_wallet=manager.account_wallet,
        additional_text=text,
    )
