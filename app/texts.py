from aiogram.utils.markdown import hide_link

# Add other languages and their corresponding codes as needed.
SUPPORTED_LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
}

TEXT_BUTTONS = {
    "ru": {
        "back": "‹ Назад",
        "retry": "↻ Повторить",
        "confirm": "✓ Подтвердить",

        "connect_wallet": "Подключить {wallet_name}",
        "open_wallet": "Перейти в {wallet_name}",
        "disconnect_wallet": "× Отключиться",

        "change_language": "↻ Изменить язык",
    },
    "en": {
        "back": "‹ Back",
        "retry": "↻ Retry",
        "confirm": "✓ Confirm",

        "connect_wallet": "Connect {wallet_name}",
        "open_wallet": "Go to {wallet_name}",
        "disconnect_wallet": "× Disconnect",

        "change_language": "↻ Change Language",
    }
}

TEXT_MESSAGES = {
    "ru": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://telegra.ph//file/db9c5c3febe75811e41af.jpg')}"
            "🤖 <b>Добро пожаловать!</b>\n\n"
            "Привет! Я помогу тебе избавиться от нежелательных SBT NFT в твоем кошельке.\n\n"
            "• Просто <b>отправь мне адрес NFT</b>, от которого хочешь избавиться, "
            "и подтверди транзакцию в своем кошельке. Всё просто и безопасно!\n\n"
            "<b>Подключен к:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "👋 <b>Привет!</b>\n\n"
            "Выбери язык:"
        ),
        "change_language": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>Выбери язык:</b>"
        ),
        "nft_not_owned": (
            "<blockquote>К сожалению, Вы не являетесь владельцем этого NFT!</blockquote>"
        ),
        "interface_not_supported": (
            "<blockquote>Интерфейс контракта не поддерживается! "
            "Пожалуйста, отправь адрес NFT Soulbound (SBT).</blockquote>"
        ),
        "invalid_address": (
            "<blockquote>Неверный адрес! Пожалуйста, попробуйте ещё раз.</blockquote>"
        ),
        "nft_info": (
            "<b>Внимание!</b>\n\n"
            "Подтверждая транзакцию, вы соглашаетесь с тем, что отказываетесь от прав на владение NFT {nft}.\n\n"
            "<b>Этот процесс нельзя будет отменить!</b>"
        ),
        "nft_destroyed": (
            "<blockquote>Транзакция успешно подтверждена кошельком! Дождитесь обработки транзакции, "
            "после обработки транзакции NFT будет удален из вашего кошелька.</blockquote>"
        ),
    },
    "en": {
        "loader_text": "⏳",
        "outdated_text": "...",

        "main_menu": (
            f"{hide_link('https://telegra.ph//file/db9c5c3febe75811e41af.jpg')}"
            "🤖 <b>Welcome!</b>\n\n"
            "I can help you get rid of unwanted SBT NFTs in your wallet.\n\n"
            "• Just <b>send me the address of the NFT</b> you want to remove "
            "and confirm the transaction in your wallet. It’s simple and secure!\n\n"
            "<b>Connected to:</b> {wallet}"
        ),
        "select_language": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "👋 <b>Hello!</b>\n\n"
            "Choose a language:"
        ),
        "change_language": (
            f"{hide_link('https://telegra.ph//file/aaba319da09f60e6def03.jpg')}"
            "<b>Choose a language:</b>"
        ),
        "nft_not_owned": (
            "<blockquote>Sorry, but this NFT is not owned by you!</blockquote>"
        ),
        "interface_not_supported": (
            "<blockquote>The contract interface is not supported! "
            "Please send the address of the Soulbound (SBT) NFT.</blockquote>"
        ),
        "invalid_address": (
            "<blockquote>Invalid address! Please try again.</blockquote>"
        ),
        "nft_info": (
            "<b>Attention!</b>\n\n"
            "By confirming the transaction, you agree to give up your ownership rights to this NFT {nft}.\n\n"
            "<b>This process cannot be undone!</b>"
        ),
        "nft_destroyed": (
            "<blockquote>The transaction has been successfully confirmed by the wallet! "
            "Wait for the processing of the transaction, "
            "then the NFT will be removed from your wallet.</blockquote>"
        ),
    }
}
