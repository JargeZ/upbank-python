import os
from typing import AsyncGenerator

from upbank_client.api_wrapped import AsyncApiBundle
from upbank_client.client.utils import paginate
from upbank_client.models import TransactionResource
from upbank_spec import ApiClient, Configuration


class AsyncClient:
    api: AsyncApiBundle

    def __init__(
        self,
        token: str | None = None,
        api_client: ApiClient | None = None,
    ):
        if token and api_client:
            raise ValueError("You can only provide one of token or api_client")

        if not api_client:
            api_client = ApiClient(
                Configuration(
                    host="https://api.up.com.au/api/v1",
                    access_token=token or os.environ.get("UPBANK_TOKEN"),
                )
            )

        self.api = AsyncApiBundle(api_client)

    async def get_all_transactions(self, batch_size: int = 100) -> AsyncGenerator[TransactionResource, None]:
        paginator = paginate(self.api.transactions.transactions_get)(
            page_size=batch_size,
        )

        async for page in paginator:
            for transaction in page.data:
                yield transaction

    async def get_transaction_details(self, transaction_id: str) -> TransactionResource:
        response = await self.api.transactions.transactions_id_get(id=transaction_id)
        return response.data
