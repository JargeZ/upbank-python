from typing import Optional

from upbank_spec import ApiClient
from .transactions_api import AsyncTransactionsApi


class AsyncApiBundle:
    transactions: AsyncTransactionsApi

    def __init__(self, api_client: Optional[ApiClient] = None):
        self.api_client = api_client
        self.transactions = AsyncTransactionsApi(api_client)

    @property
    async def tr(self):
        async with self.api_client as api_client:
            return AsyncTransactionsApi(api_client)
