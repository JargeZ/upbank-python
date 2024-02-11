import asyncio
import os

import pytest

from upbank_client.api_wrapped import AsyncApiBundle
from upbank_client.client.async_client import AsyncClient
from upbank_spec import Configuration, ApiClient


@pytest.mark.asyncio
async def test_get_all_products():
    configuration = Configuration(
        host="https://api.up.com.au/api/v1",
        access_token=os.environ["BEARER_TOKEN"]
    )

    cl = AsyncClient(AsyncApiBundle(ApiClient(configuration)))

    async for trx in cl.get_all_transactions():
        print(f"\n\n"
              f"- {trx.attributes.description} -\n"
              f"| {trx.attributes.amount.value} {trx.attributes.amount.currency_code}\n"
              f"| {trx.attributes.settled_at}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_get_all_products())
    loop.close()
