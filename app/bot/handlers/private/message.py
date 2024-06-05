from aiogram import Router, F
from aiogram.types import Message
from pytoniq_core import Address

from app.bot.handlers.private.windows import Window
from app.bot.manager import Manager
from app.bot.utils.states import UserState

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(UserState.MAIN_MENU)
async def main_menu_message(message: Message, manager: Manager) -> None:
    if message.content_type == "text":
        try:
            address = Address(message.text)
            await manager.send_loader_message()
            account = await manager.tonapi.accounts.get_info(address.to_str())

            if "sbt" in account.interfaces:
                nft = await manager.tonapi.nft.get_item_by_address(address.to_str())
                if nft.owner.address.to_userfriendly() != manager.account_wallet.address.to_userfriendly():
                    text = manager.text_message.get("nft_not_owned")
                    await Window.main_menu(
                        manager,
                        account_wallet=manager.account_wallet,
                        additional_text=text,
                    )
                else:
                    await manager.state.update_data(nft=nft.dict())
                    await Window.nft_info(manager)

            else:
                text = manager.text_message.get("interface_not_supported")
                await Window.main_menu(
                    manager,
                    account_wallet=manager.account_wallet,
                    additional_text=text,
                )

        except (Exception,):
            text = manager.text_message.get("invalid_address")
            await Window.main_menu(
                manager,
                account_wallet=manager.account_wallet,
                additional_text=text,
            )

    await manager.delete_message(message)


@router.message()
async def default_message(message: Message, manager: Manager) -> None:
    await manager.delete_message(message)
