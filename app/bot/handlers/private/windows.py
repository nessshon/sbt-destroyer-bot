from aiogram_tonconnect.tonconnect.models import AccountWallet
from pytonapi.schema.nft import NftItem

from app.bot.manager import Manager, SendMode
from app.bot.utils import keyboards
from app.bot.utils.states import UserState
from app.bot.utils.urls import TonviewerUrl, GetgemsNFTUrl


class Window:

    @staticmethod
    async def select_language(manager: Manager, send_mode: SendMode = SendMode.EDIT, **_) -> None:
        text = manager.text_message.get("select_language")
        reply_markup = keyboards.select_language()

        await manager.send_message(text, reply_markup=reply_markup, send_mode=send_mode)
        await manager.state.set_state(UserState.SELECT_LANGUAGE)

    @staticmethod
    async def change_language(manager: Manager, send_mode: SendMode = SendMode.EDIT, **_) -> None:
        text = manager.text_message.get("change_language")
        reply_markup = keyboards.select_language()

        await manager.send_message(text, reply_markup=reply_markup, send_mode=send_mode)
        await manager.state.set_state(UserState.CHANGE_LANGUAGE)

    @staticmethod
    async def main_menu(
            manager: Manager,
            account_wallet: AccountWallet,
            send_mode: SendMode = SendMode.EDIT,
            additional_text: str = None,
            **_,
    ) -> None:
        text = manager.text_message.get("main_menu").format(
            wallet=TonviewerUrl(account_wallet.address.to_userfriendly()).hlink_short,
        )
        if additional_text:
            text += "\n\n" + additional_text
        reply_markup = keyboards.main_menu(manager.text_button)

        await manager.send_message(text, reply_markup=reply_markup, send_mode=send_mode)
        await manager.state.set_state(UserState.MAIN_MENU)

    @staticmethod
    async def nft_info(manager: Manager, send_mode: SendMode = SendMode.EDIT, **_) -> None:
        state_data = await manager.state.get_data()

        nft_item = NftItem(**state_data.get("nft"))

        if not nft_item.metadata and nft_item.metadata.get("name"):
            name = "Unknown"
        else:
            name = nft_item.metadata.get("name")

        text = manager.text_message.get("nft_info").format(
            nft=GetgemsNFTUrl(address=nft_item.address.to_userfriendly(True), name=name).hlink_name,
        )
        reply_markup = keyboards.nft_info(manager.text_button)

        await manager.send_message(text, reply_markup=reply_markup, send_mode=send_mode)
        await manager.state.set_state(UserState.NFT_INFO)
