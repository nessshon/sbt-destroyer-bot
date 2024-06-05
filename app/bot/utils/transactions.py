import time
from base64 import urlsafe_b64encode

from aiogram_tonconnect.tonconnect.models import TransactionMessage, Transaction
from pytoniq_core import begin_cell


class DestroyNFTTransaction(Transaction):

    def __init__(
            self,
            address: str,
            amount: int = 0.02,
    ) -> None:
        payload = urlsafe_b64encode(
            begin_cell()
            .store_uint(0x1f04537a, 32)
            .store_uint(0, 64)
            .end_cell()
            .to_boc()
        ).decode()
        super().__init__(
            messages=[
                TransactionMessage(
                    address=address,
                    payload=payload,
                    amount=str(int(amount * 1e9)),
                ),
            ],
            valid_until=int(time.time() + 300),
        )
