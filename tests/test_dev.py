import asyncio

import pytest

from upbank_client.client.async_client import AsyncClient


@pytest.mark.asyncio
async def test_get_all_products():
    cl = AsyncClient()

    async for trx in cl.get_all_transactions():
        details = await cl.get_transaction_details(trx.id)
        details.attributes.amount
        print(f"\n\n"
              f"- {trx.attributes.description} -\n"
              f"| {trx.attributes.amount.value} {trx.attributes.amount.currency_code}\n"
              f"| {details.json()}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_get_all_products())
    loop.close()
