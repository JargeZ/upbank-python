from typing import Optional, AsyncGenerator

from upbank_client.api_wrapped import AsyncApiBundle
from upbank_client.client.utils import paginate
from upbank_client.models import TransactionResource

class AsyncClient:
    api: AsyncApiBundle

    def __init__(self, api: AsyncApiBundle):
        self.api = api

    async def get_all_transactions(
        self, batch_size: int = 4
    ) -> AsyncGenerator[TransactionResource, None]:

        paginator = paginate(self.api.transactions.transactions_get)(
            page_size=batch_size,
        )

        async for page in paginator:
            for transaction in page.data:
                yield transaction
