from typing import Optional, AsyncGenerator

from upbank_client.api_wrapped import AsyncApiBundle
from upbank_client.client.utils import paginate

class AsyncClient:
    api: AsyncApiBundle

    def __init__(self, api: AsyncApiBundle):
        self.api = api

    async def get_all_transactions(
        self, product_category: Optional[BankingProductCategory] = None, batch_size: int = 100
    ) -> AsyncGenerator[BankingProductV4, None]:

        paginator = paginate(self.api.transactions.transactions_get)(
            product_category=product_category,
            page_size=batch_size,
        )

        async for page in paginator:
            for product in page.data.products:
                yield product

a = URL()